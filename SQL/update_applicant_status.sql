-- update status of applicant - from accepted to ongoing, from ongoing to completed
CREATE OR REPLACE PROCEDURE nbp_project.update_applicant_status(
    p_offer_id integer,
    p_student_id integer
)
AS $$
DECLARE
    v_status integer;
BEGIN
    -- check if this application exists
    IF EXISTS(
        SELECT 1
        FROM nbp_project.applies_for
        WHERE offer_id = p_offer_id AND
              student_id = p_student_id
    )
    THEN
        -- read the acceptance status for later
        SELECT acceptance_status
        FROM nbp_project.applies_for
        WHERE student_id = p_student_id AND
              offer_id = p_offer_id
        INTO v_status;

        -- change status from accepted to ongoing
        IF v_status = 2 THEN
            UPDATE nbp_project.applies_for
            SET acceptance_status = 4
            WHERE offer_id = p_offer_id AND
                  student_id = p_student_id;
        
        -- change status from ongoing to completed
        ELSIF v_status = 4 THEN
            UPDATE nbp_project.applies_for
            SET acceptance_status = 5
            WHERE offer_id = p_offer_id AND
                  student_id = p_student_id;
        END IF;
    END IF;
    COMMIT;
END
$$ LANGUAGE plpgsql;