class CreateFollowQueues < ActiveRecord::Migration
  def self.up
    create_table :follow_queues do |t|

      t.timestamps
    end
  end

  def self.down
    drop_table :follow_queues
  end
end
