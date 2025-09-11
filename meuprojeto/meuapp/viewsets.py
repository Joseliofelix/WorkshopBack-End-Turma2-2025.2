from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Cep
from .serializers import CepSerializer
import requests

class CepViewSet(viewsets.ModelViewSet):
    queryset = Cep.objects.all()
    serializer_class = CepSerializer

    def retrieve(self, request, pk=None):
        try:
            cep_obj = Cep.objects.get(cep=pk)
            serializer = self.get_serializer(cep_obj)
            return Response(serializer.data)
        except Cep.DoesNotExist:
            url = f"https://viacep.com.br/ws/{pk}/json/"
            response = requests.get(url)

            if response.status_code == 200 and not response.json().get('erro', False):
                data = response.json()
                cep_obj = Cep.objects.create(
                    cep=pk,
                    logradouro=data.get('logradouro', ''),
                    bairro=data.get('bairro', ''),
                    cidade=data.get('localidade', ''),
                    estado=data.get('uf', '')
                )
                serializer = self.get_serializer(cep_obj)
                return Response(serializer.data)
            else:
                return Response({"detail": "CEP não encontrado."}, status=status.HTTP_404_NOT_FOUND)
