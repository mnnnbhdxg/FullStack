<<<<<<< HEAD
from django.shortcuts import render,redirect   
=======
from django.shortcuts import render,redirect   # 加入 redirect 套件
>>>>>>> dbfc639cce0f305cb6b8c739e1110e5f2ca24dd6
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
<<<<<<< HEAD
	return HttpResponse('a html')
=======
	return render(request, 'guestbookver1.html')
>>>>>>> dbfc639cce0f305cb6b8c739e1110e5f2ca24dd6
