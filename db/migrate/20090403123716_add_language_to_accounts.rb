class AddLanguageToAccounts < ActiveRecord::Migration
  def self.up
    add_column :accounts_to_monitors, :search_language, :string, :limit => 2
  end

  def self.down
    remove_column :accounts_to_monitors, :search_language
  end
end
