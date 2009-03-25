from followme_scanner import *
from followme_processor import *
import time

if __name__ == '__main__':
	while True:
		users = get_accounts_to_monitor()
		for user in users:
			try:
				autofollowscan(user)
			except Exception, e:
				pass
		print "Resting for 30 minutes"
		time.sleep(1800)