# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, user_id):
    return render(request, 'chat/room.html', {
        'user_id': mark_safe(json.dumps(user_id))
    })
