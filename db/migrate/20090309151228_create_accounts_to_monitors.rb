class CreateAccountsToMonitors < ActiveRecord::Migration
  def self.up
    create_table :accounts_to_monitors do |t|

      t.timestamps
    end
  end

  def self.down
    drop_table :accounts_to_monitors
  end
end
