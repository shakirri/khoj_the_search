from rest_framework.response import Response
from rest_framework.decorators import api_view
from khoj.models import UserData
from .serializers import UserDataSerializer

@api_view(['GET'])
def getData(request):
    userdata = UserData.objects.all()
    serializer = UserDataSerializer(userdata, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = UserDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    