from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo_app.views import TodoModeViewSet

router = DefaultRouter()

router.register('api', TodoModeViewSet, basename='todo_api')

urlpatterns = [
    path(r'', include(router.urls))
]
