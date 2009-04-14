class AddTweetToFollowerQueues < ActiveRecord::Migration
  def self.up
    add_column :follow_queues, :tweet, :text
  end

  def self.down
    remove_column :follow_queues, :tweet
  end
end
