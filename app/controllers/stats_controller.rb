class StatsController < ApplicationController
  layout "accounts"
  active_scaffold :stat do |config|
    config.columns = [:pass_date, :followers, :friends]
    config.create.link.label = ""
    config.update.link.label = ""
    config.delete.link.label = ""
    config.create.columns = []
  end
end
