drop table users;
create table users (
  id serial primary key,
  username varchar(128)
);

drop table courses;
create table courses (
  id serial primary key,
  course varchar(512)
);

drop table sequence_events;
create table sequence_events (
  id serial primary key,
  username varchar(128),
  user_id integer,
  event_time timestamp,
  type varchar(128),
  new integer,
  old integer
);

drop table video_events;
create table video_events (
  id serial primary key,
  username varchar(128),
  user_id integer,
  event_time timestamp,
  type varchar(128),
  timecode varchar(128)
);

drop table document_events;
create table document_events (
  id serial primary key,
  username varchar(128),
  user_id integer,
  event_time timestamp,
  type varchar(128),
  new integer,
  old integer
);

drop table link_events;
create table link_events (
  id serial primary key,
  username varchar(128),
  user_id integer,
  event_time timestamp,
  current_url varchar,
  target_url varchar
);

drop table check_answer_events;
create table check_answer_events (
  id serial primary key,
  username varchar(128),
  user_id integer,
  event_time timestamp,
  type varchar(128),
  problem_id varchar,
  attempts integer,
  success boolean
);

drop table certificate_events;
create table certificate_events (
  id serial primary key,
  username varchar(128),
  user_id integer,
  event_time timestamp,
  course_id varchar
);

drop table enrollment_evnts;
create table enrollment_evnts (
  id serial primary key,
  username varchar(128),
  user_id integer,
  event_time timestamp,
  type varchar(128),
  course_id varchar
);
