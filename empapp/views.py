from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
# from django.contrib.auth.models import User
from empapp.models import User,Leave
from .serializers import AuthTokenSerializer, UserSerializer, EmployeeSerializer, LeaveSerializer
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view


class CustomAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'first_name': user.first_name,
            'last_name' : user.last_name,
            'user_id': user.pk,
            'email': user.email,
            'admin':user.is_superuser,

        })
class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  
            'auth': str(request.auth), 
        }
        return Response(content)


@api_view(["GET", "POST", "PUT","DELETE"])
@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = User.objects.filter(is_superuser=False)
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Employee Added Successfully!!" , safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method=='PUT':
         employee_data = JSONParser().parse(request)
         employee=User.objects.get(id=employee_data['id'])
         serializer=UserSerializer(employee, data=employee_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.",  safe=False)

    elif request.method=='DELETE':
        employee=User.objects.get(id=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)


@csrf_exempt
def SaveFile(request ):
    file=request.FILES.get('media')
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)

@api_view(["GET", "POST", "PUT","DELETE"])
@csrf_exempt
def leaveApi(request,id=0):
    if request.method=='GET':
        employees = Leave.objects.all()
        employees_serializer = LeaveSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Leave Approved!!" , safe=False)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method=='PUT':
         employee_data = JSONParser().parse(request)
         employee=Leave.objects.get(id=employee_data['id'])
         serializer=LeaveSerializer(employee, data=employee_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.",  safe=False)

    elif request.method=='DELETE':
        employee=Leave.objects.get(id=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)