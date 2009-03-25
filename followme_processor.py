import simplejson, urllib
import time
from models import *
from helpers import *
from twitter_functions import *
from datetime import datetime
from datetime import *; from dateutil.relativedelta import *

def get_accounts_to_process():
	return User.select()
	
def get_friends_from_queue(user):
	friends = FollowQueue.select((FollowQueue.q.accounts_to_monitor_id == user.id) & (FollowQueue.q.followed_date == None) & (FollowQueue.q.followed_back_date == None) & (FollowQueue.q.rejected == 0))
	return friends

def get_friends_from_queue_no_follow(user):
	friends = FollowQueue.select((FollowQueue.q.accounts_to_monitor_id == user.id) & (FollowQueue.q.followed_back_date == None) & (FollowQueue.q.unfollowed == 0) & (FollowQueue.q.followed_date != None))
	return friends
	
def get_friends_from_queue_follow(user):
	friends = FollowQueue.select((FollowQueue.q.accounts_to_monitor_id == user.id) & (FollowQueue.q.followed_back_date != None) & (FollowQueue.q.unfollowed == 0) & (FollowQueue.q.followed_date != None))
	return friends
	
def get_expired_rejected_friends(days_ago):
	expiration_date = datetime.now()+relativedelta(days=-days_ago)
	friends = FollowQueue.select((FollowQueue.q.rejected_date < expiration_date))
	return friends

def destroy_expired_rejections(friends):
	for friend in friends:
		friend.destroySelf()
	
def process_follow_back(user, friends):
		reset_api()
		for friend in friends:
			if is_friend_following_me(user, friend):
				friend.followed_back_date = datetime.now()
				friend.set()
			else:
				if (datetime.now() - friend.followed_date).days > user.number_of_days_to_follow_back:
					api.SetCredentials(username=user.username, password=user.password)
					if overLimitCheck(api,user) == False:
						try:
							api.DestroyFriendship(friend.username)
							friend.unfollowed = True
							friend.set()
						except Exception, e:
							friend.destroySelf()
							pass
					
def is_friend_following_me(user, friend):
	reset_api()
	if friend.twitter_id == None:
		temp = api.GetUser(friend.username)
		friend.twitter_id = temp.id
	my_followers = api.SocialGraphGetFollowers(user=user.username)
	if friend.twitter_id in my_followers:
		return True
	else:
		return False

def process_manual_unfollow(user):
	friends = FollowQueue.select((FollowQueue.q.accounts_to_monitor_id == user.id) & (FollowQueue.q.followed_back_date != None) & (FollowQueue.q.unfollowed == 1))
	for friend in friends:
		api.SetCredentials(username=user.username, password=user.password)
		if overLimitCheck(api,user) == False:
			try:
				api.DestroyFriendship(friend.username)
				friend.followed_back_date = None
				friend.set()
			except Exception, e:
				friend.destroySelf()
				pass
										
def follow_friends(user, friends):
	for friend in friends:
		if is_friend_following_me(user, friend):
			friend.followed_back_date = datetime.now()
			friend.set()
		else:
			api.SetCredentials(username=user.username, password=user.password)
			if overLimitCheck(api,user) == False:
				try:
					api.CreateFriendship(friend.username)
					friend.followed_date = datetime.now()
					friend.set()
				except Exception, e:
					friend.destroySelf()
					pass
				
def process_user(user):
	friends = get_friends_from_queue(user)
	if friends != None:
		follow_friends(user, friends)
	friends = get_friends_from_queue_no_follow(user)
	if friends != None:
		process_follow_back(user, friends)
	process_manual_unfollow(user)
	
