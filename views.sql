--this file is reserved for creating and altering views.
--All views defined previously are supposed to be defined here



create view ACTIVE_OFFER as
select *
from applies_for
where acceptance_status = 'ACTIVE';




create view COMPLETED_OFFER as
select *
from applies_for
where acceptance_status = 'COMPLETED';


create view OFFER_ACCOMMODATION_COMPANY as
select  *
from (ACCOMMODATION as AC(acc_id,acc_phone_number,acc_email_address,acc_address,acc_country_id,acc_start_date,acc_end_date,type,description,offer_id)
        natural join OFFER as OF(offer_id,requirements,responsibilities,benefits,salary,field,off_start_date,duration_in_weeks,member_id,company_id)
     )as OF_AC
        natural join company as CO(company_id,name,co_phone_number,co_email_address,co_address,co_country_id,number_of_employees)
order by acc_id;

create view COMPLETED_INTERNSHIP as
select id as internship_id, grade_work, grade_accommodation,grade_student,((grade_student+grade_accommodation+grade_work)/3) as average_grade, comment_student, comment_company,duration_in_weeks,salary,bonus_pay,student_id,offer_id,acceptance_status,date_of_app_submission
from INTERNSHIP join COMPLETED_OFFER on (offer_id = applies_for_offer_id and student_id = applies_for_student_id)
order by average_grade desc ;