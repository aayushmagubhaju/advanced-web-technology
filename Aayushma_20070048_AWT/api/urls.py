from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ItemList, ItemDetail, LocationList, LocationDetail, FileDetail, FileList

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>', ItemDetail.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>', LocationDetail.as_view()),
    #path('file/', FileList.as_view()),
    #path('file/<int:pk>', FileDetail.as_view())
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)