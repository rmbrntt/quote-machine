from rest_framework.serializers import ModelSerializer
from .models import Quote


class QuoteSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Quote

