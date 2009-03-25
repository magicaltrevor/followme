class AccountsController < ApplicationController
  layout "accounts"
  active_scaffold :accounts_to_monitor do |config|
    config.columns = [:username, :password, :search_term, :search_pages, :reserved_api_hits, :min_friends, :min_followers, :min_tweets, :ratio, :max_ratio, :number_of_days_to_follow_back, :paused]
    config.nested.add_link("Follower Queue", [:follow_queues])
    config.nested.add_link("Stats", [:stats])
    list.columns.exclude :password
    show.columns.exclude :password
    columns[:password].form_ui = :password
  end
end
