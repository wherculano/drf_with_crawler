from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .serializers import NotebookSerializer
from ..models import Notebook


class NotebookViewSet(ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    http_method_names = ['get', 'post', 'head']
    filter_backends = [OrderingFilter]
    search_fields = ['modelo', 'valor', 'hdd', 'avaliacoes', 'nota', 'descricao']

