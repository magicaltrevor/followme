class FollowQueuesController < ApplicationController
  layout "accounts"
  active_scaffold :follow_queue do |config|
    config.columns = [:username, :tweets, :friends, :followers, :followed_date, :followed_back_date, :unfollowed, :twitter_id, :rejected]
    config.create.columns = [:username, :tweets, :friends, :followers, :rejected, :unfollowed, :twitter_id]
  end
end
