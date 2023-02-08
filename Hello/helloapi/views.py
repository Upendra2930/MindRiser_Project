from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from helloapi.serializers import ContactSerializer, FeedBackSerializer, UserInfoSerializer
from home.models import Contact, FeedBack,UserInfo

# Create your views here.
# class ContactApiView(APIView):
#     def get(self, request):
#         data = Contact.objects.all()
#         serializer = ContactSerializer(data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



#     def post (self, request):
#         pass

@api_view(['GET','POST'])
def Contact_list(request):
    if request.method == 'GET':

        contact =Contact.objects.all()
        serializer = ContactSerializer(contact ,many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

#From this is for project]
@api_view(['GET','POST'])
def User_Info(request):
    if request.method == 'GET':

        user = UserInfo.objects.all()
        serializer = UserInfoSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def user_detail(request,user):
    try:
        user = UserInfo.objects.get(pk=user)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method =='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    