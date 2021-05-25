from json.encoder import JSONEncoder
from typing import Dict
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum, Count

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from .model.Student import Student
from .model.Account import Account
from .model.Attendance import Attendance
from .model.Info import Info
from .model.Schedule import Schedule

from .serializer import StudentSerializer
from .serializer import AccountSerializer
from .serializer import AttendanceSerializer
from .serializer import InfoSerializer
from .serializer import ScheduleSerializer
from .serializer import StudentAtendanceSerializer
import json

# Create your views here.
@api_view(['GET'])
def home(request):
    students = Student.objects.prefetch_related('attendance').prefetch_related('schedule').order_by('id')
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

#login
@api_view(['GET'])
def login(request, user,password):
    account = Account.objects.filter(user=user, password=password)
    serializer = AccountSerializer(account, many=True)
    err = json.dumps('error')
    if len(serializer.data) == 0:
        return Response(err)
    else:     
        return Response(serializer.data)

#checkStudent
@api_view(['GET'])
def checkStudent(request, codestudent, idschedule):
    student = Student.objects.filter(codestudent=codestudent, schedule_id=idschedule,attendance_id__isnull=False)
    #serializer = StudentSerializer(student, many=True)
    if(student.count()==0):
        a = json.dumps(False)
    else:
        a = json.dumps(True) 
    return Response(a)

#getInfo
@api_view(['GET'])
def getInfo(request, id):
    info = Info.objects.filter(id=id).values()
    #info = Info.objects.raw('SELECT * FROM core_info WHERE id=%s',id)
    serializer = InfoSerializer(info, many=True)
    return Response(serializer.data)

#getHistory
@api_view(['GET'])
def getHistory(request):
    student = Student.objects.prefetch_related('attendance').prefetch_related('schedule')
    serializer = StudentAtendanceSerializer(student, many=True)
    return Response(serializer.data)

#getHistoryClass
@api_view(['GET'])
def getHistoryClass(request, id):
    student = Attendance.objects.filter(schedule_id=id)
    serializer = AttendanceSerializer(student, many=True)
    return Response(serializer.data)

#getSchedule
@api_view(['GET'])
def getSchedule(request, id, serial):
    if serial == ' ':
        schedule = Schedule.objects.filter(account_id=id)
    else :
        schedule = Schedule.objects.filter(account_id=id, serial=serial)
    serializer = ScheduleSerializer(schedule, many=True)
    return Response(serializer.data)

#getStudentLoginAttend
@api_view(['GET'])
def getStudentLoginAttend(request, id, codeclass):
    student = Student.objects.prefetch_related('attendance').prefetch_related('schedule').filter(attendance_id__isnull=False, schedule_id=codeclass, codestudent=id)
    serializer = StudentAtendanceSerializer(student, many=True)
    return Response(serializer.data)

#getStudentResult
@api_view(['GET'])
def getStudentResult(request, id):
    student = Student.objects.filter(attendance_id=id).order_by('-status')
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)

#getStudentAttend
@api_view(['GET'])
def getStudentAttend(request,id):
    student = Student.objects.filter(attendance__isnull=False, schedule=id).annotate(total=Count('id'))
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)

#createStudent
@api_view(['POST'])
def createStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#updateStudentStatus
@api_view(['PATCH'])
def updateStudent(request, codestudent):
    student = Student.objects.get(codestudent=codestudent)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)