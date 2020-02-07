# Create your views here.
from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

def index(request):
    # only very first time
    if request.session.get('gold') == None:
        request.session['gold'] = 0
    if request.session.get('activity') == None:
        request.session['activity'] = []

    context = {
        'gold': request.session['gold'],
        'activity' : request.session['activity'],
    }
    return render(request, 'index.html', context)
    

def process_money(request,place):
    # Create Date/Time portion of activity str
    datetime_str = strftime("%Y/%m/%d %I:%M %p")
    
    # Calculate random range, append to activity str
    if place == "farm":
        difference = random.randrange(10,21)
        request.session['activity'].append("Earned {} gold from the farm! {}".format(difference, datetime_str))
    elif place == "cave":
        difference = random.randrange(5,11)
        request.session['activity'].append("Earned {} gold from the cave! {}".format(difference, datetime_str))
    elif place == "house":
        difference = random.randrange(2,6)
        request.session['activity'].append("Earned {} gold from the house! {}".format(difference, datetime_str))
    elif place == "casino":
        difference = random.randrange(-50,1)
        request.session['activity'].append("Entered a casino and lost {} gold... Ouch.. {}".format(difference*-1, datetime_str))
    
    # make adjustments to new total gold
    request.session['gold'] += difference
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activity'] = []
    return redirect('/')