from followme_scanner import *
from followme_processor import *


if __name__ == '__main__':
	users = get_accounts_to_process()
	for user in users:
		try:
			process_user(user)
		except Exception, e:
			pass
	users = get_accounts_flagged_for_mass_unfollow()
	for user in users:
		try:
			unfollow_nonfollowers(user)
		except Exception, e:
			pass