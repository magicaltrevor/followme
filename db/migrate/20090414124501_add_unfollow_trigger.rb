class AddUnfollowTrigger < ActiveRecord::Migration
  def self.up
    add_column :accounts_to_monitors, :trigger_unfollow_event, :boolean, :default => false
  end

  def self.down
    remove_column :accounts_to_monitors, :trigger_unfollow_event
  end
end
