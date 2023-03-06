from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'taskcatalog'

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
