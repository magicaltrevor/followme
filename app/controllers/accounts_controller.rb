class AccountsController < ApplicationController
  before_filter :login_required
  layout "accounts"
  MASTER_ACCOUNTS = [1]
  active_scaffold :accounts_to_monitor do |config|
    config.columns = [:username, :password, :search_term, :search_pages, :search_language, :reserved_api_hits, :max_follows_per_hour, :min_friends, :min_followers, :min_tweets, :ratio, :max_ratio, :number_of_days_to_follow_back, :trigger_unfollow_event, :paused]
    config.nested.add_link("Follower Queue", [:follow_queues])
    config.nested.add_link("Stats", [:stats])
    list.columns.exclude :password, :user_id
    show.columns.exclude :password, :user_id
    update.columns.exclude :user_id
    columns[:password].form_ui = :password
    columns[:username].description = "Twitter username of the account you wish to manage."
    columns[:password].description = "Password for this twitter account."
    columns[:search_pages].description = "The number of pages deep you want the search to go. (Max 25)"
    columns[:search_language].description = "The language you want to search on (en for english only, sp for spanish only, etc.)"
    columns[:reserved_api_hits].description = "The number of api hits you wish to reserve for the user. This means this bot will leave at least this many api hits available at all times."
    columns[:max_follows_per_hour].description = "The maximum number of people in the follow queue the script will follow per hour. (Default and recommendation is 25)."
    columns[:min_friends].description = "The minimum number of twitter friends a target must have to meet your criteria (Recommendation: 100)"
    columns[:min_followers].description = "The minimum number of twitter followers a target must have to meet your criteria (Recommendation: 100)"
    columns[:min_tweets].description = "The minimum number of updates or 'tweets' a target must have to meet your criteria (Recommendation: 100)"
    columns[:ratio].description = "The ratio of followers to friends represented in percentage. 100% is 1:1 ratio.\n If this field is set to 100 the user must have at least as many followers as friends. Followers can exceed friends but cannot be any lower. Recommendation is 90"
    columns[:max_ratio].description = "The ratio of friends to followers represented in percentage. 100% is 1:1 ratio.\n If this field is set to 100 the user must have at least as many friends as followers. Friends can be LESS than followers but cannot exceed it. Higher that 100 means that they can have more friends than followers.Recommendation is 105"
    columns[:number_of_days_to_follow_back].description = "The number of days for the target to follow you back once followed."
    columns[:trigger_unfollow_event].description = "If this is set to true, the next pass for processing (done hourly), will automatically unfollow ANYONE in your friends list who isn't following you back and permanently adds them to a list so that they will not be added by this script again."
    columns[:paused].description = "If set to 1, this pauses this twitter account from all search activity. Any targets left in the queue will be followed and automatic unfollowing will still occur but no new people will be queued."
  end
  
  def conditions_for_collection
    ['user_id = ?', current_user.id] unless MASTER_ACCOUNTS.include?(current_user.id)
  end
  
  protected
  
  def before_update_save(record)
    before_create_save(record)
  end
  
  def before_create_save(record)
    record.user_id = current_user.id
  end
end
