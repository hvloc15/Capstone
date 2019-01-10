from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from api.views import OCR, UploadImage

urlpatterns = [
    url(r'^ocr/',OCR.as_view(), name='ocr'),
    url(r'^upload/',UploadImage.as_view(), name='upload'),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
