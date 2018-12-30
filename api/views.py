from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from api.serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from algorithms.utils import read_opencv_image


class OCR(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_serializer = ImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            #image = read_opencv_image(file_serializer.validated_data.get("image"))
            return Response( "Success", status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
