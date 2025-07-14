from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import SignupSerializer, ProfileSerializer

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method=='GET':
        serializer=ProfileSerializer(request.user)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=ProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
