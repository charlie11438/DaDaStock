from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/api$',views.inventoryAPIView),
	url(r'^$',views.inventoryView)
]