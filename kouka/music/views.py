from django.shortcuts import render
from django.views import generic
from django.contrib.auth import logout
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class MypageView(generic.TemplateView):
    template_name = 'mypage.html'

