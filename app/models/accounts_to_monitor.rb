class AccountsToMonitor < ActiveRecord::Base
  has_many :follow_queues, :conditions => ['rejected = ?', 0]
  has_many :stats, :order => "pass_date"
  belongs_to :user
  
  validates_presence_of :username
  validates_uniqueness_of :username, :on => :create, :message => "This client already exists in our system."
  validates_presence_of :password
  validates_presence_of :search_term
  validates_length_of :search_term, :within => 1..140, :message => "Search term must be at least 1 character but no more than 140"
  validates_presence_of :min_friends
  validates_presence_of :min_followers
  validates_presence_of :min_tweets
  validates_presence_of :ratio
  validates_presence_of :max_ratio
  validates_presence_of :reserved_api_hits
  validates_presence_of :number_of_days_to_follow_back
  
  def name
    "#{username}"
  end
  
end
