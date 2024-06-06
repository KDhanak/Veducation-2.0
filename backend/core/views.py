from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Publication
from .serializers import PublicationSerializer

# Create your views here.


@api_view(['GET'])
def getData(request):
    items = Publication.objects.all()
    serializer = PublicationSerializer(items, many=True)
    return Response(serializer.data)
