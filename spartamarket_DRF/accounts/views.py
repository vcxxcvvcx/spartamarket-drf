from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer,UserSerializer

# Create your views here.


@api_view(['POST'])
@transaction.atomic
def signup(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            profile_data = request.data.get('profile', {})
            profile_serializer = ProfileSerializer(data=profile_data)
            if profile_serializer.is_valid():
                profile_serializer.save(user=user)
                return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
            user.delete()  
            return Response({'message': 'Error during registration', 'errors': profile_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Error during registration', 'errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_detail_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)
