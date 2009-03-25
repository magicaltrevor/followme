from sqlobject import *
db_conn = 'mysql://root@localhost/followme'


class User(SQLObject):
	_connection = db_conn
	class sqlmeta:
		table = "accounts_to_monitors"
	username = StringCol()
	password = StringCol()
	search_term = StringCol()
	min_tweets = IntCol()
	min_followers = IntCol()
	min_friends = IntCol()
	ratio = IntCol()
	max_ratio = IntCol()
	reserved_api_hits = IntCol()
	number_of_days_to_follow_back = IntCol()
	paused = IntCol()
	search_pages = IntCol()
	
class FollowQueue(SQLObject):
	_connection = db_conn
	class sqlmeta:
		table = "follow_queues"
	username = StringCol()
	accounts_to_monitor_id = IntCol()
	followed_date = DateTimeCol()
	rejected = IntCol()
	followers = IntCol()
	friends = IntCol()
	tweets = IntCol()
	followed_back_date = DateTimeCol()
	unfollowed = IntCol()
	twitter_id = IntCol()
	rejected_date = DateTimeCol()
	
class Stats(SQLObject):
	_connection = db_conn
	class sqlmeta:
		table="stats"
	accounts_to_monitor_id = IntCol()
	pass_date = DateTimeCol()
	followers = IntCol()
	friends = IntCol()