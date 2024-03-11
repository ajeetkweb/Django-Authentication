from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated




# Create your views here.

# function-based views


#create new user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


# get list of users
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])

def list_users(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many = True)
    return Response(serializer.data)


# get, update and delete single user
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_details(request, pk):

    if request.method == 'GET':

        try:
            user = User.objects.get(pk = pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        except User.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        user = User.objects.get(pk = pk)
        user.delete()
        return Response({'Message': 'User Deleted'})
    
        
    if request.method == 'PUT':
        user = User.objects.get(pk = pk)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data': serializer.data,'Message': 'User updated'})
        



# CLASS-BASED VIEWS
        
# list all users or create new user
class ListUsers(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
 
    # list all users
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)

    
    #create new user
    def post(self, request):

        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

# get, update and delete single user
class UserInfo(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        try:
            user = User.objects.get(pk = pk)
            return user
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer  = UserSerializer(user)
        return Response(serializer.data)

        

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response({'Message': 'User deleted'})
        



# generic views


class ListCreateUserViews(ListCreateAPIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateUserAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer






    

