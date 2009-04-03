import simplejson, urllib
import time
from models import *
from helpers import *
from twitter_functions import *
from datetime import datetime
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
							add_to_follow_queue(my_subject, user.id)
						else:
							add_to_follow_queue(my_subject, user.id, rejected=True)
					except Exception, e:
						pass
				
def user_pause_check(user):
	api.SetCredentials(username=user.username, password=user.password)
	user_info = api.GetUser(user.username)
	new_stat = Stats(accounts_to_monitor_id=user.id,pass_date=datetime.now(),followers=int(user_info.followers_count),friends=int(user_info.friends_count))
	new_stat.set()
	if user.paused == 0:
		if int(user_info.friends_count) - int(user_info.followers_count) > PAUSE_RATIO:
			reset_api()
			return True
		else:
			reset_api()
			return False
	else:
		return True
	

def add_to_follow_queue(subject,user_id,rejected=False):
	if rejected == True:
		new_queue = FollowQueue(username=str(subject.screen_name),accounts_to_monitor_id=user_id,followed_date=None,rejected=rejected,followers=int(subject.followers_count),friends=int(subject.friends_count),tweets=int(subject.statuses_count),followed_back_date=None,unfollowed=False,twitter_id=subject.id,rejected_date=datetime.now())
	else:
		new_queue = FollowQueue(username=str(subject.screen_name),accounts_to_monitor_id=user_id,followed_date=None,rejected=rejected,followers=int(subject.followers_count),friends=int(subject.friends_count),tweets=int(subject.statuses_count),followed_back_date=None,unfollowed=False,twitter_id=subject.id,rejected_date=None)
	new_queue.set()

def ignore_duplicates(subject,user):
	if FollowQueue.select((FollowQueue.q.username == subject) & (FollowQueue.q.accounts_to_monitor_id == user.id)).count() > 0:
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

