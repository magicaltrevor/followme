class FollowQueue < ActiveRecord::Base
  belongs_to :accounts_to_monitor
end
