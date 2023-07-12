from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    queryset = Advertisement.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        search = self.request.GET
        if search:
            if search.get('status'):
                queryset = queryset.filter(status = search.get('status'))
            elif search.get('created_at_after'):
                queryset = queryset.filter(created_at__gte = search.get('created_at_after'))
            else:
                queryset = queryset.filter(created_at__lte = search.get('created_at_before'))

        return queryset

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly(),]
        return []
