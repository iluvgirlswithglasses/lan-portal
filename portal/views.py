from django.shortcuts import render
from os import listdir
from os.path import isdir, isfile, join

STATIC_URL = "portal/static/f/"

def get(request):
	# this portal works like a discord server
	# you put your directories - which work as channels - here
	lst = {}
	for channel in sorted(listdir(STATIC_URL)):
		f = STATIC_URL + channel
		if isdir(f) and len(listdir(f)) > 0:
			# and then you put your content into the channel
			lst[channel] = sorted([x for x in listdir(f) if isfile(join(f, x))])
	# then everything is done
	return render(request, "homepage.html", {
		"lst": lst,
	})
