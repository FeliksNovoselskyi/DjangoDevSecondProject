from django.shortcuts import render

# Create your views here.
def auth_reg_func(request):
    return render(request, 'Authorization_Registration/authorization_registration.html')
