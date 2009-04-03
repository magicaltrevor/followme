class AddMaxFollowsPerHourToAccounts < ActiveRecord::Migration
  def self.up
    add_column :accounts_to_monitors, :max_follows_per_hour, :integer, :default=>25
  end

  def self.down
    remove_column :accounts_to_monitors, :max_follows_per_hour
  end
end
