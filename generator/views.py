from django.shortcuts import render

from django.http import HttpResponse

import random

# Create your views here.

def about1(request):
	return render(request, 'generator/about1.html')


def home(request):
	return render(request, 'generator/home.html')

def password(request):

	character = list('abcdefghijklmlopqrstuvwxyz')

	if request.GET.get('uppercase'):

		character.extend(list('ABCDEFGHIJHLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):

		character.extend(list('@#$%^&*()!'))


	if request.GET.get('Number'):

		character.extend(list('0123456789'))


	length = int(request.GET.get('length',12))

	reqpass = ''
	for x in range(length):
		reqpass += random.choice(character)

	return render(request, 'generator/password.html',{'password':reqpass})
