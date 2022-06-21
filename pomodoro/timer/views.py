from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404


class MainView(View):
    """ 
    This class represent main site of whole app.
    """

    def get(self, request):
        return render(request, 'main.html')

    def post(self, request):
        return
