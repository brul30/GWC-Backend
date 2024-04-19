from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
#from .serializers import ProductSerializer


from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import ProfileSerializer
from .models import Profile


# Create your views here.
@api_view(['GET'])
def createNote(request):
    course_title = request.query_params.get('course_title')
    
    if not course_title:
        return Response({"message": "Course title parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    profiles = Profile.objects.filter(course_title__iexact=course_title)  # Using __iexact for case-insensitive matching
    if not profiles.exists():
        return Response({"message": "No notes found for the provided course title."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)



    