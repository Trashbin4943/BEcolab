from rest_framework import status,generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class=MovieListSerializer

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class=MovieDetailSerializer

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def movie_comments(request,movie_pk):
    movie=get_object_or_404(Movie, pk=movie_pk)

    if request.method == "GET":
        comments=Comment.objects.filter(pk=movie_pk)
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'error':'Authentication required'},
                            status=status.HTTP_401_UNAUTHORIZED)
        serializer=CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, movie=movie)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    