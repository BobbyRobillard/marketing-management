from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def homepage_view(request):
    return redirect('marketing:homepage')
