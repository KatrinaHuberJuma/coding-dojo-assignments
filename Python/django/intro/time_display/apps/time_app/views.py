from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "date": strftime("%b %d, %Y"),
        "time": strftime("%H:%M %p")
    }
    return render(request,'time_app/index.html', context)