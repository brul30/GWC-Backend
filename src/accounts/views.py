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



# @api_view(['GET'])
# def get_Data(request):
#     #person = {'name':'danis'}
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)

#     return Response(serializer.data)



from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    username = request.data['username']
    return Response({f'user created: {username}'})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def subscriptionStatus(request):
    #Do logic here for accoutn subscription using the stripe account
    return Response("no SubscriptinStatus yet")