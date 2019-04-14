-- CLEAR ALL
drop table sequence_events;
drop table video_events;
drop table document_events;
drop table link_events;
drop table check_answer_events;
drop table certificate_events;
drop table enrollment_evnts;
drop table others;
drop table report_1;
drop table users;


-- USERS
create table users (
  id serial primary key,
  username varchar(128)
);


-- EVENTS
create table sequence_events (
  id serial primary key,
  user_id integer references users (id),
  course varchar,
  event_time timestamp,
  type varchar(128),
  new integer,
  old integer
);

create table video_events (
  id serial primary key,
  user_id integer references users (id),
  course varchar,
  event_time timestamp,
  type varchar(128),
  timecode varchar(128)
);

create table document_events (
  id serial primary key,
  user_id integer references users (id),
  course varchar,
  event_time timestamp,
  type varchar(128),
  new integer,
  old integer
);

create table link_events (
  id serial primary key,
  user_id integer references users (id),
  course varchar,
  event_time timestamp,
  current_url varchar,
  target_url varchar
);

create table check_answer_events (
  id serial primary key,
  user_id integer references users (id),
  course varchar,
  event_time timestamp,
  type varchar(128),
  attempts integer,
  success boolean
);

create table certificate_events (
  id serial primary key,
  user_id integer references users (id),
  course varchar,
  event_time timestamp,
  course_id varchar
);

create table enrollment_evnts (
  id serial primary key,
  user_id integer references users (id),
  course varchar,
  event_time timestamp,
  type varchar(128)
);

create table others (
  id serial primary key,
  user_id integer references users (id),
  event_time timestamp
);


-- REPORTS
create table report_1 (
  id serial primary key,
  user_id integer references users (id),
  course varchar,
  per_start date,
  per_end date
);
insert into report_1 (user_id, course) values (null, null);
