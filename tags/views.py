from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tags.models import Tags
from tags.serializers import WriteTagsSerializer, ReadTagsSerializer
from django.utils.text import slugify

'''
USE CASE 1
```one use of serializer is to do json data validation from client side
Serializer(data=request.data)
USE CASE 2
second use of serializer is to convert orm object into json from server side
Serializer(instance=object)```
'''

class CreateTagView(APIView):
   
    def post(self, request):
        # IMPORTANT !!!
        # USE CASE 1
        # for client side data validation we use data = request data
        serializer = WriteTagsSerializer(data=request.data)
        if serializer.is_valid():
            # if the serializer is valid we create the tag from valid data
            name = serializer.validated_data.get('name')
            tag_object = Tags.objects.create(
                name=name,
                slug=slugify(name)
            )
            # IMPORTANT !!!
            # USE CASE 2
            # for read operation we use instance = tag object, to convert orm data into json
            json_data = ReadTagsSerializer(instance=tag_object).data
            return Response(json_data, status=status.HTTP_201_CREATED)
        else:
            # return the serializer error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)