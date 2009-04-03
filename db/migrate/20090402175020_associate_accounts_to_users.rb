class AssociateAccountsToUsers < ActiveRecord::Migration
  def self.up
    add_column :accounts_to_monitors, :user_id, :integer
  end

  def self.down
    remove_column :accounts_to_monitors, :user_id
  end
end
