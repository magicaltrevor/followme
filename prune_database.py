from followme_scanner import *
from followme_processor import *

PRUNE_DAYS = 7


if __name__ == '__main__':
	friends = get_expired_rejected_friends(PRUNE_DAYS)
	if friends != None:
		destroy_expired_rejections(friends)