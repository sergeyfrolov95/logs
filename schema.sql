delete table users;
create table users (
  id serial primary key,
  username varchar(128)
);

delete table courses;
create table courses (
  id serial primary key,
  course varchar(512)
);

delete table sequence_events;
create table sequence_events (
  id serial primary key,
  user_id varchar(128),
  event_time timestamp,
  type varchar(128),
  new integer,
  old integer
);

delete table video_events;
create table video_events (
  id serial primary key,
  user_id integer,
  event_time timestamp,
  type varchar(128),
  timecode varchar(128)
);

delete table document_events;
create table document_events (
  id serial primary key,
  user_id integer,
  event_time timestamp,
  type varchar(128),
  new integer,
  old integer
);

delete table link_events;
create table link_events (
  id serial primary key,
  user_id integer,
  event_time timestamp,
  current_url varchar,
  target_url varchar
);

delete table check_answer_events;
create table check_answer_events (
  id serial primary key,
  user_id integer,
  event_time timestamp,
  type varchar(128),
  problem_id varchar,
  attempts integer,
  success boolean
);

delete table certificate_events;
create table certificate_events (
  id serial primary key,
  user_id integer,
  event_time timestamp,
  course_id varchar
);

delete table enrollment_evnts;
create table enrollment_evnts (
  id serial primary key,
  user_id integer,
  event_time timestamp,
  type varchar(128),
  course_id varchar
);
