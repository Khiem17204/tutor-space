from django.shortcuts import render

# Create your views here.
def lobby(request):
    return render(request, 'base/lobby.html')

def rooom(request):
    return render(request, 'base/room.html')

