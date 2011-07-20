import twitter
import time
from helpers import *
import simplejson,urllib

api = twitter.Api(username='sanitizeduser',password='sanitizedpassword')
SEARCH_BASE = 'http://search.twitter.com/search.json'

def reset_api():
	api.SetCredentials(username='sanitizeduser',password='sanitizedpassword')
	
def overLimitCheck(api,user):
	rateinfo = api.GetRateLimitStatus()
	if rateinfo['remaining_hits'] > user.reserved_api_hits:
		return False
	else:
		return True

def search(query, results=100, page = 1, max_id = None, **kwargs):
	kwargs.update({
		'q': query,
		'page': page,
		'rpp': results
	})
	if max_id != None:
		kwargs.update({
			'max_id': max_id
		})
	url = SEARCH_BASE + '?' + urllib.urlencode(kwargs)
	print url
	result = simplejson.load(urllib.urlopen(url))
	return result

def get_reach(user):
	my_followers = api.SocialGraphGetFollowers(user)
	my_follower_count = len(my_followers)
	second_order_follower_counts = []
	for follower in my_followers:
		#debug
		print "Getting stats for %s" % follower
		try:
			followers = api.SocialGraphGetFollowers(follower)
			second_order_follower_counts = second_order_follower_counts + followers
		except Exception, e:
			time.sleep(5)
			try:
				followers = api.SocialGraphGetFollowers(follower)
				second_order_follower_counts = second_order_follower_counts + followers
			except Exception, e:
				time.sleep(5)
				pass
			pass
	print "Presorted follower_count = %s" % len(second_order_follower_counts)
	second_order_follower_counts = unique(second_order_follower_counts)
	return my_follower_count, second_order_follower_counts