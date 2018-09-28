from django.shortcuts import render,redirect   
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
	return HttpResponse('a html')
