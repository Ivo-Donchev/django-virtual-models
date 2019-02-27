from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from .models import Club


class MyDBApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()

    def get(self, *args, **kwargs):
        clubs = Club.objects.all()

        data = self.OutputSerializer(clubs, many=True).data

        return Response(data)
