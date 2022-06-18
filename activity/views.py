from django.shortcuts import render

def calendarView(request):
    return render(request, 'activities/calendar.html')
