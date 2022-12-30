from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from members.models import Member


class MembersView(APIView):
    def get(self, request):
        print(f"This is your get request : {request}")
        response = {"status": True, "message": "get endpoint called!"}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        print("@@@@@@@@@@@@@@@@@@@", request.data)
        print(f"This is your post request : {request}")
        response = {"status": True, "message": "post endpoint called!"}
        return Response(data=response, status=status.HTTP_200_OK)

    def put(self, request):
        print(f"This is your put request : {request}")
        response = {"status": True, "message": "put endpoint called!"}
        return Response(data=response, status=status.HTTP_200_OK)

    def patch(self, request):
        print(f"This is your patch request : {request}")
        response = {"status": True, "message": "patch endpoint called!"}
        return Response(data=response, status=status.HTTP_200_OK)

    def delete(self, request):
        print(f"This is your delete request : {request}")
        response = {"status": True, "message": "delete endpoint called!"}
        return Response(data=response, status=status.HTTP_200_OK)

def members(request):
    return HttpResponse("Hello world!")

def members_name(request):
    return HttpResponse("Name Is Dk")
