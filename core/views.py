from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UsuariosAPIView(APIView):
    def get(self, request):

        dados_usuarios = [
            {
                "nome": "Carlos",
                "email": "Carlos@email.com"
            },
            {
                "nome": "Joao",
                "email": "joao@email.com"
            }
        ]

        return Response(dados_usuarios, status=status.HTTP_200_OK)