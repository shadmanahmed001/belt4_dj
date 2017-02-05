from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from datetime import datetime, date

def index(request):
		return render(request,"belt4_app/main.html")

def login(request):
	if request.method == 'POST':
		result = User.objects.login(request.POST)
		if result['status']:
			request.session['user_id'] = result['user_id']
			request.session['name'] = result['user_name']
			return redirect ('/appointments')
		else:
			for errorStr in result['errors']:
				messages.error(request, errorStr)
				return redirect ('/')

def register(request):
	if request.method == 'POST':
		result = User.objects.register(request.POST)
		if result['status']:
			request.session['user_id'] = result['user_id']
			request.session['name'] = result['name']
			return redirect ('/appointments')
		else:
			for errorStr in result['errors']:
				messages.error(request, errorStr)
	return redirect ('/')

def logout(request):
	request.session.clear()
	return redirect ('/')
