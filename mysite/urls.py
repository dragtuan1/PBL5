
from django.contrib import admin
from django.urls import path, include

from core.views import login,checkStudent,getInfo,getSchedule,getHistoryClass,getHistory,getStudentLoginAttend,getStudentResult,getStudentAttend,home
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('student', student_list)
# router.register('student/<int:pk>/', getStudentResult)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('login/<str:user>&<str:password>', login),
    path('student/<int:id>/', getStudentResult),
    path('student/<int:id>&<int:codeclass>/', getStudentLoginAttend),
    path('student/attend/<int:id>/', getStudentAttend),
    path('checkStudent/<str:codestudent>&<str:idschedule>', checkStudent),
    path('info/<str:id>/', getInfo),
    path('class/<str:id>/', getHistoryClass),
    path('schedule/<str:id>&<str:serial>/', getSchedule),
    path('class/', getHistory),
    path('home/', home)
    
]
