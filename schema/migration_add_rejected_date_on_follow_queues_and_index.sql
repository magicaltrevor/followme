alter table follow_queues add column `rejected_date` datetime default NULL;
alter table follow_queues add index `rejected_on` (`rejected`,`rejected_date`);