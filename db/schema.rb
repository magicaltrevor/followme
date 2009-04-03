# This file is auto-generated from the current state of the database. Instead of editing this file, 
# please use the migrations feature of Active Record to incrementally modify your database, and
# then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your database schema. If you need
# to create the application database on another system, you should be using db:schema:load, not running
# all the migrations from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended to check this file into your version control system.

ActiveRecord::Schema.define(:version => 20090403123716) do

  create_table "accounts_to_monitors", :force => true do |t|
    t.string  "username"
    t.string  "password"
    t.integer "min_tweets"
    t.integer "min_followers"
    t.integer "min_friends"
    t.string  "search_term"
    t.integer "ratio"
    t.integer "max_ratio"
    t.integer "reserved_api_hits"
    t.integer "number_of_days_to_follow_back"
    t.integer "paused",                                     :default => 0
    t.integer "search_pages",                               :default => 5
    t.integer "max_follows_per_hour",                       :default => 25
    t.integer "user_id"
    t.string  "search_language",               :limit => 2
  end

  add_index "accounts_to_monitors", ["paused"], :name => "paused_users"

  create_table "follow_queues", :force => true do |t|
    t.string   "username"
    t.integer  "accounts_to_monitor_id"
    t.datetime "followed_date"
    t.integer  "rejected"
    t.integer  "followers"
    t.integer  "friends"
    t.integer  "tweets"
    t.datetime "followed_back_date"
    t.integer  "unfollowed"
    t.integer  "twitter_id"
    t.datetime "rejected_date"
  end

  add_index "follow_queues", ["accounts_to_monitor_id"], :name => "accounts_to_monitor_id"
  add_index "follow_queues", ["followed_date"], :name => "followed_date"
  add_index "follow_queues", ["rejected", "accounts_to_monitor_id"], :name => "rejected_accounts_to_monitor_id"
  add_index "follow_queues", ["rejected", "rejected_date"], :name => "rejected_on"
  add_index "follow_queues", ["rejected"], :name => "rejected"
  add_index "follow_queues", ["username", "accounts_to_monitor_id"], :name => "username_accounts_to_monitor_id"

  create_table "stats", :force => true do |t|
    t.integer  "accounts_to_monitor_id"
    t.datetime "pass_date"
    t.integer  "followers"
    t.integer  "friends"
  end

  add_index "stats", ["accounts_to_monitor_id"], :name => "accounts_to_monitor_index"

  create_table "users", :force => true do |t|
    t.string   "login",                     :limit => 40
    t.string   "name",                      :limit => 100, :default => ""
    t.string   "email",                     :limit => 100
    t.string   "crypted_password",          :limit => 40
    t.string   "salt",                      :limit => 40
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "remember_token",            :limit => 40
    t.datetime "remember_token_expires_at"
  end

  add_index "users", ["login"], :name => "index_users_on_login", :unique => true

end
