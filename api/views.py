from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from api.serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from algorithms.utils import read_opencv_image
from api.renderer import ApiJSONRenderer
import pytesseract


class OCR(APIView):
    parser_classes = (MultiPartParser, FormParser)
    renderer_classes = (ApiJSONRenderer,)

    def post(self, request):
        file_serializer = ImageSerializer(data=request.data)
        file_serializer.is_valid(raise_exception=True)
        image = read_opencv_image(file_serializer.validated_data.get("image"))
        text = pytesseract.image_to_string(image, lang="vie")
        print(text)
        return Response({"message":text}, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({"message":"OK"}, status=status.HTTP_200_OK)


class UploadImage(APIView):
    parser_classes = (MultiPartParser, FormParser)
    renderer_classes = (ApiJSONRenderer,)

    def post(self, request):
        file_serializer = ImageSerializer(data=request.data)
        file_serializer.is_valid(raise_exception=True)
        file_serializer.save()
        return Response({"message":file_serializer.data}, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({"message": "OK"}, status=status.HTTP_200_OK)

