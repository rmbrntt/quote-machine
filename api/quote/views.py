from rest_framework.viewsets import ModelViewSet
from .serializers import QuoteSerializer
from .models import Quote


class QuoteModelViewSet(ModelViewSet):

    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()