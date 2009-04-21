import simplejson, urllib
import time
from models import *
from helpers import *
from BeautifulSoup import BeautifulSoup
from twitter_functions import *
from datetime import datetime
from django.utils.encoding import smart_str, smart_unicode

PAUSE_RATIO = 10

def get_accounts_to_monitor():
	return User.select()

def autofollowscan(user):
	count = 0
	pages = []
	if user_pause_check(user) == False:
		while count < user.search_pages:
			count += 1
			if user.search_language:
				pages.append(search(user.search_term, 100, count, None, lang=user.search_language))
			else:
				pages.append(search(user.search_term, 100, count, None))
		for search_recs in pages:
			for rec in search_recs['results']:
				if ignore_duplicates(rec['from_user'], user) == False:
					try:
						my_subject, status = follow_screen(user, rec['from_user'])
						if status:
							add_to_follow_queue(my_subject, user.id, rec['text'])
						else:
							add_to_follow_queue(my_subject, user.id, rec['text'], rejected=True)
					except Exception, e:
						print e, status
						pass
				
def user_pause_check(user):
        followers_count = 0
        friends_count = 0
        user_info = urllib.urlopen("http://twitter.com/%s" % user.username)
        soup = BeautifulSoup(user_info)
        spans = soup.findAll('span')
        for i in spans:
                if i.has_key('id'):
                        if i['id'] == "follower_count":
                                followers_count = i.contents[0].replace(",","")
                        if i['id'] == "following_count":
                                friends_count = i.contents[0].replace(",","")
		followers_count = int(followers_count)
		friends_count = int(friends_count)
        new_stat = Stats(accounts_to_monitor_id=user.id,pass_date=datetime.now(),followers=followers_count,friends=friends_count)
        new_stat.set()
        if user.paused == 0:
                if friends_count - followers_count > PAUSE_RATIO:
                        reset_api()
                        return True
                else:
                        reset_api()
                        return False
        else:
                return True
	

def add_to_follow_queue(subject,user_id, my_tweet, rejected=False, unfollowed=False):
	if rejected == True:
		new_queue = FollowQueue(username=str(subject.screen_name),accounts_to_monitor_id=user_id,followed_date=None,rejected=rejected,followers=int(subject.followers_count),friends=int(subject.friends_count),tweets=int(subject.statuses_count),followed_back_date=None,unfollowed=unfollowed,twitter_id=subject.id,rejected_date=datetime.now(),tweet=None)
	else:
		new_queue = FollowQueue(username=str(subject.screen_name),accounts_to_monitor_id=user_id,followed_date=None,rejected=rejected,followers=int(subject.followers_count),friends=int(subject.friends_count),tweets=int(subject.statuses_count),followed_back_date=None,unfollowed=unfollowed,twitter_id=subject.id,rejected_date=None,tweet=smart_str(my_tweet))
	new_queue.set()

def ignore_duplicates(subject,user,twitter_id=None):
	if twitter_id == None:
		if FollowQueue.select((FollowQueue.q.username == subject) & (FollowQueue.q.accounts_to_monitor_id == user.id)).count() > 0:
			return True
		else:
			return False
	else:
		if FollowQueue.select((FollowQueue.q.twitter_id == twitter_id) & (FollowQueue.q.accounts_to_monitor_id == user.id)).count() > 0:				
			return True
		else:
			return False

def follow_screen(user, subject):
	reset_api()
	min_tweets = user.min_tweets
	min_followers = user.min_followers
	min_friends = user.min_friends
	ratio = user.ratio
	max_ratio = user.max_ratio
	twitter_subject = api.GetUser(subject)
	if check_stats(min_tweets,min_followers,min_friends,ratio,max_ratio,twitter_subject):
		print "Yeah, %s would follow %s\nStats: followers:%s\nfriends:%s\ntweets:%s\nratio:%s" % (user.username,twitter_subject.screen_name,twitter_subject.followers_count,twitter_subject.friends_count,twitter_subject.statuses_count,str((1.0*int(twitter_subject.friends_count)/int(twitter_subject.followers_count))*100))
		return twitter_subject, True
	else:
		print "No, %s would not follow. %s does not meet the criteria.\nStats: followers:%s\nfriends:%s\ntweets:%s\nratio:%s" % (user.username,twitter_subject.screen_name,twitter_subject.followers_count,twitter_subject.friends_count,twitter_subject.statuses_count,str((1.0*int(twitter_subject.friends_count)/int(twitter_subject.followers_count))*100))
		return twitter_subject, False

def check_stats(min_tweets,min_followers,min_friends,ratio,max_ratio,twitter_subject):
	if int(twitter_subject.followers_count) > min_followers and int(twitter_subject.friends_count) > min_friends and int(twitter_subject.statuses_count) and (1.0*int(twitter_subject.friends_count)/int(twitter_subject.followers_count))*100 > ratio and (1.0*int(twitter_subject.friends_count)/int(twitter_subject.followers_count))*100 < max_ratio:
		return True
	else:
		return False

