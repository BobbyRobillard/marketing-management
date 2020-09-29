from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


@csrf_exempt
def homepage(request):
    return render(request, "website/fuck-off.html", {})
    # if request.method == "POST":
        # account_sid = 'AC0e95b3f3b8dfcca7d7298a04cc5ccae0'
        # auth_token = '64a3ac149f7d0f03f950fc71ad7425c3'
        # client = Client(account_sid, auth_token)
        #
        # message = client.messages.create(
        #              body="FISH ON!!!" + str(request.POST),
        #              from_='+13344234972',
        #              to='+15613025285'
        #           )
    # return redirect('https://instagram-mailing.com/confirmation.html')
