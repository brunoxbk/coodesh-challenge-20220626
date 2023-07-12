from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Home(APIView):
    def get(self, request, format=None):
        return Response({
            "status": 200,
            "mensagem": "Fullstack Challenge 20201026"
        })
