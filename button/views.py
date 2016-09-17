from django.shortcuts import render, get_object_or_404
from .models import Button

def button_preview(request, id):
    button = get_object_or_404(Button, id=id)
    return render(request, 'button/button.html', {'button': button})