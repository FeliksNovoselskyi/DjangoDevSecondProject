from django.shortcuts import render
from .forms import RegForm

# Create your views here.
def auth_func(request):
    return render(request, 'Authorization_Registration/authorization.html')

def reg_func(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        
        if form.is_valid():
            form.save()
    else:
        form = RegForm()
        
        
        
    return render(request, 'Authorization_Registration/registration.html', {'form': form})
