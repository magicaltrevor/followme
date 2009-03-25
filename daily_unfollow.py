from followme_scanner import *
from followme_processor import *


if __name__ == '__main__':
	users = get_accounts_to_monitor()
	for user in users:
		try:
			friends = get_friends_from_queue_follow(user)
			if friends != None:
				process_follow_back(user, friends)
		except Exception, e:
			pass