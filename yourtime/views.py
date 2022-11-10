from django.shortcuts import render
import datetime

def cr_time(request):
    now = datetime.datetime.now()
    now = now.ctime()
    return render(request, 'yourtime/cr_time.html',{
        'crtime' : now
    })