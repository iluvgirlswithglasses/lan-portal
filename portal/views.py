from django.shortcuts import render
import os

def get(request):
    # this portal works like a discord server
    # you put your directories - which work as channels - here
    STATIC_URL = os.getcwd() + "/portal/static/f/"
    lst = {}
    for channel in sorted(os.listdir(STATIC_URL)):
        if len(os.listdir(STATIC_URL + channel)) > 0:
            # and then you put your content into the channel
            lst[channel] = sorted(os.listdir(STATIC_URL + channel))
    # then everything is done
    return render(request, "homepage.html", {
        "lst": lst,
    })
