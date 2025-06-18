from rest_framework import serializers

from common.models import MediaFile

class MediaFileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'file']
        