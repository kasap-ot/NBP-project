create or replace procedure nbp_project.delete_student(
    p_user_id integer
)
as
$$
begin
    IF EXISTS (
            SELECT 1
            FROM nbp_project.student
            where id = p_user_id
        )
    THEN
        delete from nbp_project.internship where applies_for_student_id = p_user_id;
        delete from nbp_project.applies_for where student_id = p_user_id;
        delete from nbp_project.student where id = p_user_id;

    END IF;
end;
$$ language plpgsql;