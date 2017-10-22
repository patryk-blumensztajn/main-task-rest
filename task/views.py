from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, MaterialEdit
from django.contrib.auth.decorators import login_required
from .models import Profile, Material
from django.contrib import messages
import requests
from django.template import RequestContext
from django.template.loader import render_to_string
import tempfile
import json


#This view returns main page, on which you can browse company list
@login_required(login_url='/task/login/')
def dashboard(request):
	data = requests.get('http://193.142.112.220:8337/companyList')
	context = RequestContext(request, {
	})
	return render(request,
				  'task/dashboard.html',
				  {'section':'dashboard','context':context, 'data':data})

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authentication - login successful!.')
				else:
					return HttpResponse('This account is blocked.')
			else:
				return HttpResponse('Type correct login and password.')
	else:
		form = LoginForm()
	return render(request, 'task/login.html',{'form':form})

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			return render(request,'task/register_done.html', {'new_user':new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request,'task/register.html', {'user_form':user_form})

# Thanks to passed id from request, the view delete selected material
@login_required(login_url='/task/login/')
def delete(request, id):
	data = requests.get('http://193.142.112.220:8337/companyList').json()
	materials = Material.objects.all()
	context = RequestContext(request, {
	})
	query = Material.objects.get(id=id) #id=id cos... to drugie id
	query.delete()
	return render(request,
				  'task/dashboard.html',
				  {'section':'dashboard','context':context, 'data':data})

# Edit user's profile
@login_required(login_url='/task/login/')
def edit(request):
	if request.method =='POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES) 
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request,'Profile update'\
							         ' successful!.')
		else:
			messages.error(request, 'Something went wrong...')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request,'task/edit.html',{'user_form':user_form, 'profile_form':profile_form})

#Returns companys materials
@login_required(login_url='/task/login/')
def detail(request, id):
	data = requests.get('http://193.142.112.220:8337/materialList?companyID='+id).json()
	context = RequestContext(request, {
	})
	return render(request,
				  'task/board.html',
				  {'section':'board','context':context, 'data':data})

# Returns material details
@login_required(login_url='/task/login/')
def material_detail(request, id, material_id):
	materials = Material.objects.all()
	data = requests.get('http://193.142.112.220:8337/materialDetails?ID='+material_id).json() 
	context = RequestContext(request, {
	})
	return render(request,
				  'task/dash.html',
				  {'section':'dashboard','context':context, 'data':data,'materials':materials})

#Edit material
@login_required(login_url='/task/login/')
def material_edit(request, id):
	materials = Material.objects.all()
	data = requests.get('http://193.142.112.220:8337/materialDetails?ID='+id).json() 
	context = RequestContext(request, {
	})
	if request.method == 'POST':
		myform = MaterialEdit(request.POST, request.FILES)
		if myform.is_valid():
			form = myform.save(commit=False)
			form.id = data['ID']
			form.materials = materials
			form.save()
			return render(request,
				  'task/dash.html',
				  {'section':'dashboard','context':context, 'data':data,'materials':materials})
	else:
		myform = MaterialEdit()
	return render(request,
				  'task/edit_material.html',
				  {'section':'dashboard','context':context, 'data':data,'myform':myform,'materials':materials})







