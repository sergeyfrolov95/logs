create table sequence_events (
  id serial primary key,
  user_id integer,
  event_time date,
  type varchar(128),
  new integer,
  old integer
);

create table video_events (
  id serial primary key,
  user_id integer,
  event_time date,
  type varchar(128),
  timecode varchar(128)
);

create table document_events (
  id serial primary key,
  user_id integer,
  event_time date,
  type varchar(128),
  new integer,
  old integer
);

create table link_events (
  id serial primary key,
  user_id integer,
  event_time date,
  current_url varchar,
  target_url varchar
);

create table check_answer_events (
  id serial primary key,
  user_id integer,
  event_time date,
  type varchar(128),
  problem_id varchar,
  attempts integer,
  success boolean
);

create table certificate_events (
  id serial primary key,
  user_id integer,
  event_time date,
  course_id varchar
);

create table enrollment_evnts (
  id serial primary key,
  user_id integer,
  event_time date,
  type varchar(128),
  course_id varchar
);
