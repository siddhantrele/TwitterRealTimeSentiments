from django.shortcuts import render
from django.http import JsonResponse
from .models import Tweet
from django.db.models import Avg
import scraper_settings
import datetime

# Create your views here.
def render_home(request):
	track_terms=scraper_settings.TRACK_TERMS
	return render(request, 'OutputSentiment/homepage.html',{'terms':track_terms})

def get_chart_data(request):
	tweet=Tweet.objects.filter(created_date__gte=datetime.datetime.now() - datetime.timedelta(seconds=10)).aggregate(Avg('sentiment'))
	if tweet['sentiment__avg'] is None:
		tweet['sentiment__avg']=0.0
	return JsonResponse(tweet)