create or replace procedure nbp_project.insert_offer (
    p_requirements varchar,
    p_responsibilities varchar,
    p_benefits varchar,
    p_salary integer,
    p_field varchar,
    p_start_date date,
    p_duration_in_weeks integer,
    p_member_id integer,
    p_company_id integer
)
AS $$
BEGIN
        INSERT INTO nbp_project.offer (requirements, responsibilities, benefits,
                           salary, field, start_date, duration_in_weeks, member_id, company_id,is_active)
        VALUES (p_requirements, p_responsibilities, p_benefits,
                p_salary, p_field, p_start_date, p_duration_in_weeks, p_member_id, p_company_id,true);
    COMMIT;

END;
$$ language plpgsql;

--update existing offer with offer_id
create or replace procedure nbp_project.update_offer(
    p_member_id integer,
    p_offer_id integer,
    p_requirements varchar,
    p_responsibilities varchar,
    p_benefits varchar,
    p_salary integer,
    p_field varchar,
    p_start_date date,
    p_duration_in_weeks integer
)
as
$$
    begin
        -- Update existing offer
        UPDATE nbp_project.offer
        SET requirements = p_requirements,
            responsibilities = p_responsibilities,
            benefits = p_benefits,
            salary = p_salary,
            field = p_field,
            start_date = p_start_date,
            duration_in_weeks = p_duration_in_weeks
        WHERE id = p_offer_id and member_id = p_member_id;
    end;

$$ language plpgsql;

--update existing offer with accommodation with offer_id
create or replace procedure nbp_project.update_offer_accommodation(
    p_member_id integer,
    p_offer_id integer,
    p_requirements varchar,
    p_responsibilities varchar,
    p_benefits varchar,
    p_salary integer,
    p_field varchar,
    p_start_date date,
    p_duration_in_weeks integer,
    p_acc_phone varchar,
    p_acc_email varchar,
    p_acc_address varchar,
    p_acc_description varchar
)
as
$$
begin
    UPDATE nbp_project.offer
    SET requirements = p_requirements,
        responsibilities = p_responsibilities,
        benefits = p_benefits,
        salary = p_salary,
        field = p_field,
        start_date = p_start_date,
        duration_in_weeks = p_duration_in_weeks
    WHERE id = p_offer_id and member_id = p_member_id;

    IF EXISTS (
            SELECT 1
            FROM nbp_project.accommodation as a
            where a.offer_id = p_offer_id
        )
    THEN
        --if exists update
        UPDATE nbp_project.accommodation
        SET phone_number = p_acc_phone,
            email_address = p_acc_email,
            address = p_acc_address,
            description = p_acc_description
        WHERE offer_id = p_offer_id;
    ELSE
        --Accommodation doesn't exists for this offer, insert the accommodation
        INSERT INTO  nbp_project.accommodation(phone_number,email_address,address,description,offer_id)
        VALUES (p_acc_phone,p_acc_email,p_acc_address,p_acc_description,p_offer_id);
    end if;
commit;
end;

$$ language plpgsql;


--insert new Student
create or replace procedure nbp_project.insert_end_user_student (
    p_username varchar,
    p_password varchar,
    p_name varchar,
    p_surname varchar,
    p_date_of_birth date,
    p_address varchar,
    p_phone_number varchar,
    p_email_address varchar,
    p_country_id integer,
    p_study_level varchar,
    p_gpa float,
    p_ects_credits integer,
    p_major_id integer,
    p_educational_institute_id integer,
    p_start_year integer
)
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM nbp_project.end_user
        where username = p_username
    )
    THEN
    --student exists with this username, raise exception or ignore ?

    ELSE
        INSERT INTO nbp_project.end_user(username, password, name, surname, date_of_birth, address, phone_number, country_id)
        VALUES (p_username, p_password, p_name, p_surname, p_date_of_birth, p_address, p_phone_number, p_email_address, p_country_id);

        INSERT INTO nbp_project.student(study_level, gpa, start_year, ects_credits, major_id, educational_institute_id)
        VALUES (p_study_level, p_gpa, p_start_year, p_ects_credits, p_major_id, p_educational_institute_id);
    END IF;
    COMMIT;
END;
$$ language plpgsql;

--update existing Student
create or replace procedure nbp_project.update_end_user_student (
    p_student_id integer,
    p_password varchar,
    p_name varchar,
    p_surname varchar,
    p_date_of_birth date,
    p_address varchar,
    p_phone_number varchar,
    p_email_address varchar,
    p_country_id integer,
    p_study_level varchar,
    p_gpa float,
    p_ects_credits integer,
    p_major_id integer,
    p_educational_institute_id integer,
    p_start_year integer
)
AS $$
BEGIN
    UPDATE nbp_project.end_user
    SET password = p_password,
        name = p_name,
        surname = p_surname,
        date_of_birth = p_date_of_birth,
        address = p_address,
        phone_number = p_phone_number,
        email_address = p_email_address,
        country_id = p_country_id
    WHERE id = p_student_id;

    UPDATE nbp_project.student
    SET study_level = p_study_level,
        gpa = p_gpa,
        start_year = p_start_year,
        ects_credits = p_ects_credits,
        major_id = p_major_id,
        educational_institute_id = p_educational_institute_id
    WHERE id = p_student_id;
    COMMIT;
END;
$$ language plpgsql;

--Procedure for inserting a row into the experience table
CREATE OR REPLACE PROCEDURE nbp_project.insert_experience(
    p_type_of_job VARCHAR,
    p_description VARCHAR,
    p_start_year DATE,
    p_duration_in_weeks INTEGER,
    p_student_id INTEGER
)
AS $$
BEGIN
    -- Check if the experience exists based on the provided type_of_job and student_id
        -- Insert a new experience
    INSERT INTO nbp_project.experience (type_of_job, description, start_year, duration_in_weeks, student_id)
    VALUES (p_type_of_job, p_description, p_start_year, p_duration_in_weeks, p_student_id);


    COMMIT;
END;
$$language plpgsql;

--Procedure for inserting a row into the knows_language table
CREATE OR REPLACE PROCEDURE nbp_project.insert_or_update_knows_language(
    p_student_id INTEGER,
    p_lang_id INTEGER,
    p_level VARCHAR
)
AS $$
BEGIN
    -- Check if the language knowledge exists based on the provided student_id and lang_id
    IF EXISTS (
            SELECT 1
            FROM nbp_project.knows_language
            WHERE student_id = p_student_id
              AND lang_id = p_lang_id
        ) THEN
        -- Update existing language knowledge
        UPDATE nbp_project.knows_language
        SET level = p_level
        WHERE student_id = p_student_id
          AND lang_id = p_lang_id;
    ELSE
        -- Insert a new language knowledge
        INSERT INTO nbp_project.knows_language (student_id, lang_id, level)
        VALUES (p_student_id, p_lang_id, p_level);
    END IF;

    COMMIT;
END;
$$ language plpgsql;

--Procedure for inserting a row into the project table
CREATE OR REPLACE PROCEDURE nbp_project.insert_or_update_project(
    p_name VARCHAR,
    p_description VARCHAR,
    p_completeness VARCHAR,
    p_student_id INTEGER
)
AS $$
BEGIN
    -- Check if the project exists based on the provided name
    IF EXISTS (
            SELECT 1
            FROM nbp_project.project
            WHERE name = p_name
        ) THEN
        -- Update existing project
        UPDATE nbp_project.project
        SET description = p_description,
            completeness = p_completeness,
            student_id = p_student_id
        WHERE name = p_name;
    ELSE
        -- Insert a new project
        INSERT INTO nbp_project.project (name, description, completeness, student_id)
        VALUES (p_name, p_description, p_completeness, p_student_id);
    END IF;

    COMMIT;
END;
$$ language plpgsql;

--Procedure for inserting a row in the certificate table
CREATE OR REPLACE PROCEDURE nbp_project.insert_or_update_certificate(
    p_name VARCHAR,
    p_description VARCHAR,
    p_date_of_issue DATE,
    p_publisher VARCHAR,
    p_student_id INTEGER
)
AS $$
BEGIN
    -- Check if the certificate exists based on the provided name and student_id
    IF EXISTS (
            SELECT 1
            FROM nbp_project.certificate
            WHERE name = p_name
              AND student_id = p_student_id
        ) THEN
        -- Update existing certificate
        UPDATE nbp_project.certificate
        SET description = p_description,
            date_of_issue = p_date_of_issue,
            publisher = p_publisher
        WHERE name = p_name
          AND student_id = p_student_id;
    ELSE
        -- Insert a new certificate
        INSERT INTO nbp_project.certificate (name, description, date_of_issue, publisher, student_id)
        VALUES (p_name, p_description, p_date_of_issue, p_publisher, p_student_id);
    END IF;

    COMMIT;
END;
$$ language plpgsql;


create or replace procedure nbp_project.student_apply_for_offer(
    p_student_id integer,
    p_offer_id integer
)
AS $$
BEGIN
    INSERT INTO nbp_project.applies_for (student_id, offer_id, date_of_app_submission, acceptance_status)
    VALUES (p_student_id, p_offer_id, now(), 1);
    COMMIT;

END;
$$ language plpgsql;


create or replace procedure nbp_project.accept_applicant(
    p_student_id integer,
    p_offer_id integer
)
as $$
begin
    -- check if this application exists and if it has status: waiting
    -- change status in applies_for to 'accepted' for applicant
    -- change offer.is_active to false
    -- change status in applies_for to 'rejected' for all other applicants

    if exists(
        select 1
        from nbp_project.applies_for
        where offer_id = p_offer_id and
              student_id = p_student_id and
              applies_for.acceptance_status = 1 -- 1 means 'waiting'
    )
    then

    -- change status of the selected applicant to 'accepted'
    update nbp_project.applies_for
    set acceptance_status = 2       -- 2 means 'accepted'
    where offer_id = p_offer_id and
          student_id = p_student_id;

    -- set the offer as not active anymore
    update nbp_project.offer as offer
    set is_active = false
    where offer.id = p_offer_id;

    -- reject all other applicants for the offer
    update nbp_project.applies_for
    set acceptance_status = 3       -- 3 means 'rejected'
    where offer_id = p_offer_id and
          student_id != p_student_id;

    end if;
end;
$$ language plpgsql;