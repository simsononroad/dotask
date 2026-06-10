from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib import messages
from django.utils.http import re

def index(request):
    return render(request,"index.html")