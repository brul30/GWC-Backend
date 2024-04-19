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
'''```
I am gonna need 2 endpoints:
1) GET /pictures/ - returns all notes_pdf  realted to that course_title
    - this is gonna be used for the front
    - I will receive the course_title id as a parameter
    - and return all notes_pdf related to that course_title

2) POST /pictures/ - creates a new note_pdf related to that course_title
    - this is gonna be used for the front
    - I will receive the course_title id and the notes_pdf
    - and I will return code 200 if everything went fine, or code 400 if something went wrong.


```'''

@api_view(['GET'])
def getNotes(request):
    course_title = request.query_params.get('course_title')
    
    if not course_title:
        return Response({"message": "Course title parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    profiles = Profile.objects.filter(course_title__iexact=course_title)  # Using __iexact for case-insensitive matching
    if not profiles.exists():
        return Response({"message": "No notes found for the provided course title."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
def addNotes(request):
    user_id = request.data.get('user_id')
    course_title = request.data.get('course_title')
    notes_pdf = request.data.get('notes_pdf')
    instructor = request.data.get('instructor')
    semester = request.data.get('semester')
    year= request.data.get('year')

    if not all([user_id, course_title, notes_pdf,instructor,semester,year]):
        return Response({"message": "Missing data"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
