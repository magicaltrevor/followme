 CREATE TABLE `stats` (
  `id` int(11) NOT NULL auto_increment,
  `accounts_to_monitor_id` int(11) default NULL,
  `pass_date` datetime default NULL,
  `followers` int(11) default NULL,
  `friends` int(11) default NULL,
  PRIMARY KEY  (`id`),
  KEY `accounts_to_monitor_index` (`accounts_to_monitor_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1