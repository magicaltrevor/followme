alter table accounts_to_monitors add column `paused` int(11) default 0;
alter table accounts_to_monitors add column `search_pages` int(11) default 5;
alter table accounts_to_monitors add index `paused_users` (paused);