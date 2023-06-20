
--SCHEMA
create schema NBP_PROJECT;
alter schema NBP_PROJECT owner to nbp_user;


-- DOMAINS
create domain email as varchar(255) check ( VALUE ~ '^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$' ); -- one matching format is: yyyyyy@xxxx.xxx
create domain phone as varchar(9) check ( VALUE ~ '[0-9]{9}'); -- Exactly 9 digits.
create domain address as varchar(255);
create domain job as varchar(20) check ( VALUE ~ '^(EMPLOYMENT|INTERNSHIP)$'); --EMPLOYEMENT or INTERNSHIP
create domain pos_int as integer check ( VALUE > 0);
create domain percent as varchar(10) check ( VALUE ~ '^([0-9]|[1-9][0-9]|100)$'); -- 0-100
create domain lang_level    as varchar(10) check (VALUE ~ '^([ABC][12])$');  -- A1,A2,B1,B2,C1,C2
create domain study as varchar(10) check ( VALUE ~ '^(BACHELOR|MASTER|DOCTORAL)$'); -- BACHELOR or MASTER or DOCTORAL
create domain gpa   as float check ( VALUE >= 6 and VALUE <=10); -- [6,10]
create domain app_status as varchar(20) check ( VALUE ~ '^(ACCEPTED|REJECTED)$' ); --ACCEPTED or REJECTED
create domain grade as integer check ( VALUE >=0 and VALUE <=10);

--Alter domains
alter domain nbp_project.app_status drop constraint app_status_check;
alter domain nbp_project.app_status add constraint app_status_check
    check ((VALUE)::text ~'^(applied|accepted|rejected|ongoing|completed)$'::text);
--WARNING: uncomment following line only when you must to delete and drop the schema.
-- drop schema nbp_project cascade ;

--Alter tables
alter table applies_for drop column acceptance_status;
alter table applies_for add column acceptance_status integer;
alter table applies_for add constraint foreign_key1
    foreign key (acceptance_status) references acceptance_status(id)
            on delete set null on update cascade;
alter table educational_institute drop column phone_number;
alter table educational_institute drop column email_address;
alter table educational_institute drop column address;
alter table educational_institute drop column country_id;
alter table student add column study_level nbp_project.study;
alter table student add column gpa nbp_project.gpa;
alter table student add column start_year date;
alter table student add column ects_credits integer;
alter table student add column major_id integer;
alter table student add constraint major_fk
    foreign key (major_id)  references major(id)
        on delete set null on update cascade;
alter table student add column educational_institute_id integer;
alter table student add constraint edu_institute_fk
    foreign key (educational_institute_id) references educational_institute(id)
        on delete set null on update cascade;
alter table organization drop column country_id;
alter table member add column committee_id integer;
alter table member add constraint committee_fk
    foreign key (committee_id) references committee
        on delete set null on update cascade;
alter table student drop column start_year;
alter table student add column start_year integer;


--TABLES


--delete
drop table PARTICIPATES_IN;
drop table WON_PRIZE;
drop table TRAINING ;
drop table COMPETITION;
drop table EVENT;
drop table acceptance_status;
drop table studies;
drop table member_of;


create table major(
    id  int     primary key ,
    major varchar(50)
);

create table acceptance_status (
    id      int         primary key,
    status  varchar(20)
);

create table COUNTRY(
    id      serial      PRIMARY KEY,
    name    varchar(50) UNIQUE    NOT NULL
);
create table END_USER(
    id              serial         PRIMARY KEY,
    username        varchar(20)     UNIQUE,
    password        varchar(20),
    name            varchar(20),
    surname         varchar(20),
    date_of_birth   date,
    address         address,
    phone_number    phone,
    email_address   email,
    country_id      integer,
    FOREIGN KEY (country_id) REFERENCES COUNTRY (id)
                     ON DELETE SET NULL ON UPDATE CASCADE
);
create table STUDENT(
    id      integer     PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES END_USER(id)
                    ON  DELETE CASCADE ON UPDATE CASCADE
);
create table MEMBER(
    id      integer     PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES END_USER(id)
                    ON  DELETE CASCADE ON UPDATE CASCADE
);
create table EXPERIENCE(
    id                  serial         PRIMARY KEY,
    type_of_job         job,
    description         varchar(1024),
    start_year          date,
    duration_in_weeks   pos_int,
    student_id          integer     NOT NULL,
    FOREIGN KEY (student_id) REFERENCES STUDENT(id)
                    ON DELETE CASCADE ON UPDATE CASCADE
);
create table CERTIFICATE(
    id                  serial     PRIMARY KEY,
    name                varchar(30),
    description         varchar(1024),
    date_of_issue       date,
    publisher           varchar(30),
    student_id          integer     NOT NULL,
    FOREIGN KEY (student_id) REFERENCES STUDENT(id)
                    ON DELETE CASCADE ON UPDATE CASCADE
);
create table PROJECT(
    id                  serial         PRIMARY KEY,
    name                varchar(50),
    description         varchar(1024),
    completeness        percent         DEFAULT '0',
    student_id          integer         NOT NULL,
    FOREIGN KEY (student_id) REFERENCES STUDENT(id)
                    ON DELETE CASCADE ON UPDATE CASCADE
);
create table LANGUAGE(
    id      serial     PRIMARY KEY,
    name    varchar(30) NOT NULL,
    code    varchar(10) NOT NULL
);
create table KNOWS_LANGUAGE(
    student_id  integer,
    lang_id     integer,
    level       lang_level      NOT NULL,
    PRIMARY KEY (student_id,lang_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(id)
                    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (lang_id) REFERENCES LANGUAGE(id)
                    ON DELETE CASCADE ON UPDATE CASCADE

);
create table EDUCATIONAL_INSTITUTE(
    id              serial     PRIMARY KEY,
    name            varchar(50),
    phone_number    phone,
    email_address   email,
    address         address,
    superior_id     integer,
    country_id      integer,
    FOREIGN KEY (superior_id) REFERENCES EDUCATIONAL_INSTITUTE (id)
                                  ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (country_id) REFERENCES COUNTRY(id)
                                  ON DELETE SET NULL ON UPDATE CASCADE
);
create table STUDIES(
    faculty_id          integer,
    student_id          integer,
    study_level         study,
    gpa                 gpa,
    start_year          date,
    ects_credits        integer,
    PRIMARY KEY (student_id, faculty_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(id)
                ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (faculty_id) REFERENCES EDUCATIONAL_INSTITUTE(id)
                ON DELETE CASCADE ON UPDATE CASCADE


);
create table COMPANY(
    id                      serial     PRIMARY KEY,
    name                    varchar(30),
    phone_number            phone,
    email_address           email,
    address                 address,
    country_id              integer,
    number_of_employees     pos_int,
    FOREIGN KEY (country_id) REFERENCES COUNTRY(id)
                          ON DELETE SET NULL ON UPDATE CASCADE

);
create table OFFER(
    id                  serial     PRIMARY KEY,
    requirements        varchar(500),
    responsibilities    varchar(500),
    benefits            varchar(500),
    salary              pos_int,
    field               varchar(50),
    start_date          date,
    duration_in_weeks   pos_int,
    member_id           integer     NOT NULL,
    company_id          integer,
    FOREIGN KEY (member_id) REFERENCES MEMBER(id)
                ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (company_id) REFERENCES COMPANY(id)
                ON DELETE SET NULL ON UPDATE CASCADE
);
create table ACCOMMODATION(
    id          serial     PRIMARY KEY ,
    phone_number            phone,
    email_address           email,
    address                 address,
    country_id              integer,
    start_date              date,
    end_date                date,
    type                    varchar(30),
    description             varchar(500),
    offer_id                integer     NOT NULL,
    FOREIGN KEY (country_id) REFERENCES COUNTRY(id)
                          ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (offer_id) REFERENCES OFFER(id)
                          ON DELETE SET NULL ON UPDATE CASCADE,
    CHECK (start_date < end_date)
);
create table APPLIES_FOR(
    student_id                      integer,
    offer_id                        integer,
    acceptance_status               app_status,
    date_of_app_submission          date,
    PRIMARY KEY (student_id,offer_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(id)
                        ON DELETE SET NULL  ON UPDATE CASCADE,
    FOREIGN KEY (offer_id) REFERENCES OFFER(id)
                        ON DELETE SET NULL  ON UPDATE CASCADE

);

create table INTERNSHIP(
    id      serial     PRIMARY KEY ,
    grade_work  grade,
    grade_accommodation     grade,
    grade_student           grade,
    comment_student         varchar(500),
    comment_company         varchar(500),
    duration_in_weeks       pos_int,
    salary                  pos_int,
    bonus_pay               pos_int,
    applies_for_student_id  integer,
    applies_for_offer_id    integer,
    FOREIGN KEY (applies_for_student_id,applies_for_offer_id) REFERENCES APPLIES_FOR (student_id,offer_id)
                                ON DELETE SET NULL ON UPDATE CASCADE
);
create table ORGANIZATION (
    id              serial     PRIMARY KEY,
    name            varchar(50),
    phone_number    phone,
    email_address   email,
    address         address,
    country_id      integer,
    FOREIGN KEY (country_id) REFERENCES COUNTRY(id)
                          ON DELETE SET NULL ON UPDATE CASCADE
);
create table COMMITTEE(
    id              serial     PRIMARY KEY,
    phone_number    phone,
    email_address   email,
    address         address,
    country_id      integer,
    org_id          integer     NOT NULL,
    FOREIGN KEY (country_id) REFERENCES COUNTRY(id)
                        ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (org_id) REFERENCES ORGANIZATION(id)

);
create table MEMBER_OF(
   member_id        integer,
   committee_id     integer,
   PRIMARY KEY (member_id,committee_id),
   FOREIGN KEY (member_id) REFERENCES MEMBER(id)
                      ON DELETE CASCADE ON UPDATE CASCADE,
   FOREIGN KEY (committee_id) REFERENCES COMMITTEE(id)
                      ON DELETE CASCADE ON UPDATE CASCADE


);
create table EVENT(
    id              serial     PRIMARY KEY,
    name            varchar(50),
    phone_number    phone,
    email_address   email,
    address         address,
    start_date      date,
    end_date        date,
    topic           varchar(50),
    country_id      integer,
    committee_id    integer,
    FOREIGN KEY (country_id) REFERENCES COUNTRY(id)
                          ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (committee_id) REFERENCES COMMITTEE(id)
                          ON DELETE SET NULL ON UPDATE CASCADE,
    CHECK (start_date < end_date)
);
create table TRAINING(
    id                  integer         PRIMARY KEY,
    curriculum          varchar(500),
    mentor              varchar(30),
    FOREIGN KEY (id)    REFERENCES EVENT(id)
                            ON DELETE CASCADE ON UPDATE CASCADE
);
create table COMPETITION(
    id                  integer         PRIMARY KEY,
    rules               varchar(500),
    FOREIGN KEY (id) REFERENCES  EVENT(id)
                        ON DELETE CASCADE ON UPDATE CASCADE
);
create table PARTICIPATES_IN(
    student_id  integer,
    training_id integer,
    PRIMARY KEY (student_id,training_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(id)
                            ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (training_id) REFERENCES TRAINING(id)
                            ON DELETE CASCADE ON UPDATE CASCADE
);
create table WON_PRIZE(
    student_id      integer,
    competition_id  integer,
    place           integer,
    PRIMARY KEY (student_id,competition_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(id)
                      ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (competition_id) REFERENCES  COMPETITION(id)
                      ON DELETE CASCADE ON UPDATE CASCADE
);












