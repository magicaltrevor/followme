module AccountsHelper
  def username_column(record)
    link_to(h(record.username), "http://www.twittercounter.com/compare/#{record.username}/week", :popup => true)
  end
end
