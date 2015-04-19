# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template  # отвечает за получения шаблона

# Create your views here.
def menu(request):
    return render_to_response('menu.html')