class AccountsController < ApplicationController
  before_filter :login_required
  layout "accounts"
  MASTER_ACCOUNTS = [1]
  active_scaffold :accounts_to_monitor do |config|
    config.columns = [:username, :password, :search_term, :search_pages, :search_language, :reserved_api_hits, :max_follows_per_hour, :min_friends, :min_followers, :min_tweets, :ratio, :max_ratio, :number_of_days_to_follow_back, :paused]
    config.nested.add_link("Follower Queue", [:follow_queues])
    config.nested.add_link("Stats", [:stats])
    list.columns.exclude :password, :user_id
    show.columns.exclude :password, :user_id
    update.columns.exclude :user_id
    columns[:password].form_ui = :password
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
