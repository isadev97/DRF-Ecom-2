from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from tags.models import Tags
from tags.serializers import WriteTagsSerializer, ReadTagsSerializer
from django.utils.text import slugify
from django.core.cache import cache
from tags.utils import StandardResultsSetPagination

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
        # for client side data validation we use Serializer(data=request.data)
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
            # for read operation we use instance = tag object, to convert orm data into json, Serializer(instance=object)
            json_data = ReadTagsSerializer(instance=tag_object).data
            return Response(json_data, status=status.HTTP_201_CREATED)
        else:
            # return the serializer error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# read operations
# write operations
# high number of read operations and less number of write operations is ideal for a cache


class DetailTagView(APIView):

    def get(self, request, slug):
        try:
            cache_key = "tags" + str(slug)
            cached_data = cache.get(cache_key)
            if cached_data is not None:
                print("coming from cache")
                return Response(cached_data, status=status.HTTP_200_OK)
            tag_object = Tags.objects.get(slug=slug)
            response_data = ReadTagsSerializer(instance=tag_object).data 
            print("not coming from cache")
            print("generating the data")
            print("store it in the cache")
            cache.set(cache_key, response_data)
            return Response(response_data, status=status.HTTP_200_OK)
        except Tags.DoesNotExist:
            return Response({"message": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tags.MultipleObjectsReturned:
            return Response({"message": "Multiple tags exist for the given slug"}, status=status.HTTP_400_BAD_REQUEST)


class ListTagView(APIView):
    
    def get(self, request):
        try:
            queryset = Tags.objects.all()
            response_data = ReadTagsSerializer(instance=queryset, many=True).data
            return Response(response_data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Unable to fetch tags list"}, status=status.HTTP_400_BAD_REQUEST)
        

class DetailTagV2View(RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = ReadTagsSerializer
    lookup_field = "slug"

class ListTagV2View(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = ReadTagsSerializer
    pagination_class = StandardResultsSetPagination
    