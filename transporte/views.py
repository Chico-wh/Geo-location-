from rest_framework import viewsets, permissions
from .models import Linha, Ponto, Motorista, Localizacao
from .serializers import LinhaSerializer, PontoSerializer, MotoristaSerializer, LocalizacaoSerializer

# --- VIEWSETS ---

class LinhaViewSet(viewsets.ModelViewSet):
    queryset = Linha.objects.all()
    serializer_class = LinhaSerializer
    permission_classes = [permissions.AllowAny]  # público (passageiro)

class PontoViewSet(viewsets.ModelViewSet):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer
    permission_classes = [permissions.AllowAny]  # público (passageiro)

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status as http_status

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], url_path='atualizar-status')
    def atualizar_status(self, request, pk=None):
        motorista = self.get_object()
        novo_status = request.data.get('status')

        if novo_status:
            motorista.status = novo_status
            motorista.save()
            return Response({'status': 'atualizado com sucesso'}, status=http_status.HTTP_200_OK)
        return Response({'erro': 'status não fornecido'}, status=http_status.HTTP_400_BAD_REQUEST)
class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer

    def get_permissions(self):
        # Passageiros podem ver; motoristas autenticados podem criar
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
