class AccountsToMonitor < ActiveRecord::Base
  has_many :follow_queues, :conditions => ['rejected = ?', 0]
  has_many :stats, :order => "pass_date"
end
