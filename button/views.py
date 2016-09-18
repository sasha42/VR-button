from django.shortcuts import render, get_object_or_404
from .models import Button

from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def button_preview(request, id):
    button = get_object_or_404(Button, id=id)
    return render(request, 'button/button.html', {'button': button})
    #return HttpResponse("This page is safe to load in a frame on any site.")