from django.shortcuts import render
from django.http import JsonResponse


def welcome_view(request):
    response_data = {
        'message': 'Welcome to home'
    }
    return JsonResponse(response_data)