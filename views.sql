--this file is reserved for creating and altering views.
--All views defined previously are supposed to be defined here



create view ACTIVE_OFFER as
select *
from applies_for
where acceptance_status = 'ACTIVE';




create view COMPLETED_OFFER as
select A.acceptance_status,A.date_of_app_submission,O.salary,O.field,O.start_date,O.duration_in_weeks,E.name,E.surname
from applies_for as A
    join offer as O on A.offer_id = O.id
    join end_user as E on E.id = A.student_id
where A.acceptance_status = 'completed';


create view OFFER_ACCOMMODATION_COMPANY as
select  A.phone_number,A.email_address,A.address,A.start_date as acc_start_date,A.end_date,A.type,O.salary,O.field,O.start_date as offer_start_date,O.duration_in_weeks,C.name,C.number_of_employees
from accommodation as A
    join offer as O on A.offer_id = O.id
    join company as C on O.company_id = C.id
order by A.id;

create view offer_view as 
select cou.name as country_name, o.field, o.start_date,o.duration_in_weeks, com.name as company_name, count(*) as number_of_applications
from offer as o
join company as com on o.company_id= com.id
join country as cou on com.country_id = cou.id
join applies_for as app on app.offer_id = o.id
join acceptance_status as acc on acc.id = app.acceptance_status
group by country_name, o.field, o.start_date,o.duration_in_weeks, company_name



create view COMPLETED_INTERNSHIP as
select I.grade_work,I.grade_accommodation,I.grade_student,((grade_student+grade_accommodation+grade_work)/3) as average_grade,A.acceptance_status,A.date_of_app_submission,O.salary,O.field,O.start_date,O.duration_in_weeks,E.name,E.surname
from internship as I
    join applies_for as A on I.applies_for_student_id = A.student_id and I.applies_for_offer_id = A.offer_id
    join offer as O on  A.offer_id = O.id
    join end_user as E on E.id = A.student_id
where A.acceptance_status = 'completed';


----------------- Kasap's views -----------------

create view student_completed_offers as
select end_user.name, end_user.surname, count(applies_for.acceptance_status)
from end_user 
inner join student on end_user.id = student.id
left join applies_for on student.id = applies_for.student_id
where applies_for.acceptance_status = 'COMPLETED'
group by end_user.name;


create view full_user_info as
select u.name, u.surname, u.date_of_birth, u.address, u.phone_number, u.email_address, country.name
from end_user as u
inner join country on u.country_id = country.id;




----------------- Brane's views -----------------
--offers by company
create view offers_by_company as (select c.name as Company_Name,
                                  o.field as Field,
                                  o.requirements as Requirements,
                                  o.responsibilities as Responsibilities,
                                  o.benefits as Benefits,
                                  o.salary as Salary,
                                  o.start_date as Start,
                                  o.duration_in_weeks as Duration
                           from offer o
                                    join company c on o.company_id = c.id);
select * from offers_by_company;

-- - events by type
create view event_type as
select 'training' as event_type, e.name as event_name
from event e
join training t on e.id = t.id
union
select 'competition' as event_type, e.name as event_name
from event e
join competition c on e.committee_id = c.id;

select * from event_type;

-- companies with average grade on its internships
select c.name, avg(grade_work)
from company c
    join offer o on c.id = o.company_id
    join internship i on o.id = i.applies_for_offer_id
group by 1;


-- - companies with its number of offers
create view companies_with_number_of_offers as
(select c.name, count(o.id) as number_offers
from company c
         join offer o on c.id = o.company_id
group by c.id, c.name);

select * from companies_with_number_of_offers;



----------------- Evica's views -----------------
-- - committees with number of offers created
create view offers_from_comittees as (
select c.id as Comittee_Id, count(o.id) as Number_Offers
from offer o join member_of mo on o.member_id = mo.member_id join committee c on mo.committee_id = c.id
group by c.id
);
select * from Offers_From_Comittees;

-- - committees with average grade of all of its offers
--ne mora ne treba :D
--from offer o join member_of mo on o.member_id = mo.member_id join committee c on mo.committee_id = c.id

-- - committess with its country
create view committees_countries as
(
select committee.id as committee_id, country.name as country
from committee
         join country on committee.country_id = country.id
    );
select * from committees_countries;


-- - members by organization
create view members_organizations as
(
select e.name, e.surname, o.name
from end_user e
         join member_of mo on e.id = mo.member_id
         join committee c on mo.committee_id = c.id
         join organization o on c.org_id = o.id
    );
select * from members_organizations;

