from rest_framework.viewsets import ModelViewSet
from todo_app.models import TodoModel
from todo_app.serializers import TodoModelSerializer


class TodoModeViewSet(ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer
    permission_classes = []
