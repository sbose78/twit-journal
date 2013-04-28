import os
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
import urllib2
#import simplejson as sjson


def home(request):
    return render_to_response('home/index.html')

def get_user_data(request,username):

	twit_data=getFeed(username,'WL:')
	#print twit_data
	a={}
	a['a']="s"
	return HttpResponse(json.dumps(twit_data),mimetype="application/json")

def getFeed(username,type_of_tweet):
	twit_data=urllib2.urlopen('https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name='+ username+'&count=20')
	twit_data=json.loads(twit_data.read())
	twit_data = parseTweet(twit_data,type_of_tweet)
	return twit_data

def parseTweet(twit_data,type_of_tweet):
	# twit_data = 'WL:'

	my_tweet=list()
	for tweet in twit_data :
		journal_listing ={}

		'''
		tweet_string= str(tweet['text'])
		if tweet_string[:3] != type_of_tweet :
			continue
		else:
			pass
		print tweet_string[:3]
		'''

		should_i_add_this=decide(tweet)

		if should_i_add_this == True :
			journal_listing['tweet']=tweet['text']
			journal_listing['date']=tweet['created_at']
			journal_listing['id']=tweet['id_str']

			my_tweet.append(journal_listing)
			#print tweet['text']
		else:
			pass
	return my_tweet

def decide(tweet):
	if 'www.google.com' not in str(tweet['source']) and tweet['in_reply_to_screen_name'] is None:
		return True
	else :
		return False
	return False
