from rest_framework import serializers
from tags.models import Tags

# serializer is used for data validation and tag creating
# write operation into the database
class WriteTagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tags
        fields = ['name',]

# serializer is used to convert orm data into json
# read operation from the database
class ReadTagsSerializer(serializers.ModelSerializer):
    
    created_at = serializers.DateTimeField(format="%d/%m/%y")
    
    class Meta:
        model = Tags
        fields = ['id', 'name', 'slug', 'created_at']