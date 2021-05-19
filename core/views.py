from json.encoder import JSONEncoder
from typing import Dict
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum, Count
from django.core import serializers
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
import json
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
def home(request):
    students = Student.objects.prefetch_related('attendance').prefetch_related('schedule').order_by('id')
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)

#login
def login(request, user,password):
    account = Account.objects.filter(user=user, password=password)
    serializer = AccountSerializer(account, many=True)
    return JsonResponse(serializer.data,safe=False)

#checkStudent
def checkStudent(request, codestudent, idschedule):
    student = Student.objects.filter(codestudent=codestudent, schedule_id=idschedule,attendance_id__isnull=False)
    #serializer = StudentSerializer(student, many=True)
    if(student.count()==0):
        a = json.dumps(False)
    else:
        a = json.dumps(True) 
    return JsonResponse(a,safe=False)

#getInfo
def getInfo(request, id):
    info = Info.objects.filter(id=id).values()
    #info = Info.objects.raw('SELECT * FROM core_info WHERE id=%s',id)
    serializer = InfoSerializer(info, many=True)
    return JsonResponse(serializer.data, safe=False) 

#getHistory
def getHistory(request):
    student = Student.objects.prefetch_related('attendance').prefetch_related('schedule')
    serializer = StudentAtendanceSerializer(student, many=True)
    return JsonResponse(serializer.data,safe=False)

#getHistoryClass
def getHistoryClass(request, id):
    student = Attendance.objects.filter(schedule_id=id)
    serializer = AttendanceSerializer(student, many=True)
    return JsonResponse(serializer.data,safe=False) 

#getSchedule
def getSchedule(request, id, serial):
    if serial == ' ':
        schedule = Schedule.objects.filter(account_id=id)
    else :
        schedule = Schedule.objects.filter(account_id=id, serial=serial)
    serializer = ScheduleSerializer(schedule, many=True)
    return JsonResponse(serializer.data, safe=False) 

#getStudentLoginAttend
def getStudentLoginAttend(request, id, codeclass):
    student = Student.objects.prefetch_related('attendance').prefetch_related('schedule').filter(attendance_id__isnull=False, schedule_id=codeclass, codestudent=id)
    serializer = StudentAtendanceSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)

#getStudentResult
def getStudentResult(request, id):
    student = Student.objects.filter(attendance_id=id).order_by('-status')
    serializer = StudentSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)

#getStudentAttend
def getStudentAttend(request,id):
    student = Student.objects.filter(attendance__isnull=False, schedule=id).annotate(total=Count('id'))
    serializer = StudentSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False) 
