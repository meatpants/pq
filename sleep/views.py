from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Sleep

class IndexView(generic.ListView):
	template_name = 'sleep/index.html'
	context_object_name = 'sleep_list'
	
	def get_queryset(self):
		return Sleep.objects.all()


 