from rest_framework import serializers

from app.models import Notebook


class NotebookSerializer(serializers.ModelSerializer):
    hdd = serializers.JSONField(Notebook.hdd)

    class Meta:
        model = Notebook
        fields = ('modelo', 'descricao', 'valor', 'hdd', 'avaliacoes', 'nota')
