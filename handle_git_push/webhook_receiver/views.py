from django.shortcuts import render

# Create your views here.


def handle_webhook(request):

    if request.method == 'POST':
        print(request)

