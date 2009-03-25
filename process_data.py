from followme_scanner import *
from followme_processor import *


if __name__ == '__main__':
	users = get_accounts_to_monitor()
	for user in users:
		try:
			process_user(user)
		except Exception, e:
			pass
			