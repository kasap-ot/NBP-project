create or replace function nbp_project.internship_for_offer(
    p_offer_id integer,
    p_student_id integer
) returns table (
    grade_work nbp_project.grade,
    grade_accommodation nbp_project.grade,
    comment_student varchar,
    duration_in_weeks nbp_project.pos_int,
    salary nbp_project.pos_int,
    bonus_pay nbp_project.pos_int
)
as $$
begin
    return query
    select i.grade_work as grade_work,
           i.grade_accommodation as grade_accommodation,
           i.comment_student as comment_student,
           i.duration_in_weeks as duration_in_weeks,
           i.salary as salary,
           i.bonus_pay as bonus_pay
    from nbp_project.internship as i
    where i.applies_for_offer_id = p_offer_id and
          i.applies_for_student_id = p_student_id;
end
$$ language plpgsql;
