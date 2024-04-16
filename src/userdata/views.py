from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['POST'])
def signup(request):
    name = request.data['name']
    return Response({f'your name is: {name}'})