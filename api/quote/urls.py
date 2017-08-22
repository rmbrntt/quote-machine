from django.conf.urls import url
from .views import QuoteModelViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    url(r'^quotes/?$', QuoteModelViewSet.as_view({'get': 'list', 'post': 'create'})),
]