from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):

    def validate(self, data):
        image = data.get("image", None)

        if image is None:
            return serializers.ValidationError(
                "An image should be provided",
            )
        if image.size > 15 * 1024 * 1024:
            raise serializers.ValidationError(
                "Image file is too large ( > 15mb )."
            )
        if image.content_type not in ['image/jpeg', 'image/png', 'image/jpg']:
            raise serializers.ValidationError(
                "Sorry, we do not support that image type. Please try uploading a jpeg, jpg or png file.",
            )

        return data

    class Meta():
        model = Image
        fields = ('image',)
