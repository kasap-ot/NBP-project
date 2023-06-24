--SCHEMA
create schema NBP_PROJECT;
alter schema NBP_PROJECT owner to nbp_user;

-------------------------------------------- F U N C T I O N S --------------------------------------------
--Function for calculating the total number of applicants for a given internship
create or replace function number_applicants(p_offer_id INTEGER)
returns INTEGER as
$$ declare applicant_count INTEGER;
    begin
    select distinct count(*) into applicant_count
    from applies_for
    where offer_id = p_offer_id;

    return applicant_count;
END;
$$;
--the call for this function is: SELECT number_applicants(@offer_id)



------------------------------------------ P R O C E D U R E S ------------------------------------------
--Procedure for inserting a row in the table end_user and student
create or replace procedure insert_end_user_student (
    p_username varchar,
    p_password varchar,
    p_name varchar,
    p_surname varchar,
    p_date_of_birth date,
    p_address varchar,
    p_phone_number varchar,
    p_email_address varchar,
    p_country_name varchar,
    p_study_level varchar,
    p_gpa float,
    p_start_year date,
    p_ects_credits integer,
    p_educational_institute_name varchar,
    p_major_name varchar
)
AS $$
DECLARE
    v_country_id INTEGER;
    v_educational_institute_id INTEGER;
    v_major_id INTEGER;
BEGIN
    SELECT id INTO v_country_id
    FROM country
    WHERE name = p_country_name;

    SELECT id INTO v_educational_institute_id
    from educational_institute
    WHERE name = p_educational_institute_name;

    SELECT id INTO v_major_id
    from major
    where major.major = p_major_name;

    IF EXISTS (
        SELECT 1
        FROM end_user
        where username = p_username
    )   THEN
        UPDATE end_user
        SET password = p_password,
            name = p_name,
            surname = p_surname,
            date_of_birth = p_date_of_birth,
            address = p_address,
            phone_number = p_phone_number,
            country_id = v_country_id
        WHERE username = p_username;

        UPDATE student
        SET study_level = p_study_level,
            gpa = p_gpa,
            start_year = p_start_year,
            ects_credits = p_ects_credits,
            major_id = v_major_id,
            educational_institute_id = v_educational_institute_id
        WHERE EXISTS (
            SELECT 1
            FROM end_user
            WHERE username = p_username
                AND end_user.id = student.id
        );

    ELSE

    INSERT INTO end_user(username, password, name, surname, date_of_birth, address, phone_number, country_id)
    VALUES (p_username, p_password, p_name, p_surname, p_date_of_birth, p_address, p_phone_number, p_email_address, v_country_id);

    INSERT INTO student(study_level, gpa, start_year, ects_credits, major_id, educational_institute_id)
    VALUES (p_study_level, p_gpa, p_start_year, p_ects_credits, v_major_id, v_educational_institute_id);
END IF;
COMMIT;
END;
$$;

--Procedure for inserting a row in the table end_user and member
--kaj go stavame clenot? vo member of iame member_id i commitee id, so se desava tuka?
--vo member kako kje stavame?


--Procedure for inserting a row in the offer
create or replace procedure insert_offer (
    p_requirements varchar,
    p_responsibilities varchar,
    p_benefits varchar,
    p_salary integer,
    p_field varchar,
    p_start_date date,
    p_duration_in_weeks integer,
    p_member_id integer,
    p_company_name varchar
)
AS $$
DECLARE
    v_company_id INTEGER;
BEGIN
    SELECT id INTO v_company_id
    FROM company
    WHERE name = p_company_name;

    IF EXISTS (
        SELECT 1
        FROM offer
        WHERE member_id = p_member_id
    ) THEN
        -- Update existing offer
        UPDATE offer
        SET requirements = p_requirements,
            responsibilities = p_responsibilities,
            benefits = p_benefits,
            salary = p_salary,
            field = p_field,
            start_date = p_start_date,
            duration_in_weeks = p_duration_in_weeks,
            company_id = v_company_id
        WHERE member_id = p_member_id;
    ELSE
        -- Insert a new offer
        INSERT INTO offer (requirements, responsibilities, benefits,
                           salary, field, start_date, duration_in_weeks, member_id, company_id)
        VALUES (p_requirements, p_responsibilities, p_benefits,
                p_salary, p_field, p_start_date, p_duration_in_weeks, p_member_id, v_company_id);
    END IF;

COMMIT;
END;
$$;



--Procedure for inserting a row in the accomodation table
create or replace procedure insert_accommodation (
    p_phone_number varchar,
    p_email_address varchar,
    p_address varchar,
    p_country_name varchar,
    p_start_date date,
    p_end_date date,
    p_type varchar,
    p_description integer,
    p_offer_id integer
)
AS $$
DECLARE
    v_country_id INTEGER;
BEGIN
    SELECT id INTO v_country_id
    FROM country
    WHERE name = p_country_name;

    IF EXISTS (
        SELECT 1
        FROM accommodation
        WHERE offer_id = p_offer_id
    ) THEN
        -- Update existing accommodation
        UPDATE accommodation
        SET phone_number = p_phone_number,
            email_address = p_email_address,
            address = p_address,
            country_id = v_country_id,
            start_date = p_start_date,
            end_date = p_end_date,
            type = p_type,
            description = p_description
        WHERE offer_id = p_offer_id;
    ELSE
        -- Insert a new accommodation
        INSERT INTO accommodation (phone_number, email_address, address,
                                   country_id, start_date, end_date, type, description, offer_id)
        VALUES (p_phone_number, p_email_address, p_address,
                v_country_id, p_start_date, p_end_date, p_type, p_description, p_offer_id);
    END IF;
COMMIT;
END;
$$;

--Procedure for inserting a row in the applies_for table
CREATE OR REPLACE PROCEDURE insert_or_update_applies_for(
    p_student_id INTEGER,
    p_offer_id INTEGER,
    p_date_of_app_submission DATE,
    p_acceptance_status INTEGER
)
AS $$
BEGIN
    -- Check if the application exists based on the provided student_id and offer_id
    IF EXISTS (
        SELECT 1
        FROM applies_for
        WHERE student_id = p_student_id
            AND offer_id = p_offer_id
    ) THEN
        -- Update existing application
        UPDATE applies_for
        SET date_of_app_submission = p_date_of_app_submission,
            acceptance_status = p_acceptance_status
        WHERE student_id = p_student_id
            AND offer_id = p_offer_id;
    ELSE
        -- Insert a new application
        INSERT INTO applies_for (student_id, offer_id, date_of_app_submission, acceptance_status)
        VALUES (p_student_id, p_offer_id, p_date_of_app_submission, p_acceptance_status);
    END IF;

    COMMIT;
END;
$$;


--Procedure for inserting a row in the certificate table
CREATE OR REPLACE PROCEDURE insert_or_update_certificate(
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
        FROM certificate
        WHERE name = p_name
            AND student_id = p_student_id
    ) THEN
        -- Update existing certificate
        UPDATE certificate
        SET description = p_description,
            date_of_issue = p_date_of_issue,
            publisher = p_publisher
        WHERE name = p_name
            AND student_id = p_student_id;
    ELSE
        -- Insert a new certificate
        INSERT INTO certificate (name, description, date_of_issue, publisher, student_id)
        VALUES (p_name, p_description, p_date_of_issue, p_publisher, p_student_id);
    END IF;

    COMMIT;
END;
$$;


--Procedure for inserting a row in the committee table
CREATE OR REPLACE PROCEDURE insert_or_update_committee(
    p_phone_number VARCHAR,
    p_email_address VARCHAR,
    p_address VARCHAR,
    p_country_id INTEGER,
    p_org_id INTEGER
)
AS $$
BEGIN
    -- Check if the committee exists based on the provided org_id
    IF EXISTS (
        SELECT 1
        FROM committee
        WHERE org_id = p_org_id
    ) THEN
        -- Update existing committee
        UPDATE committee
        SET phone_number = p_phone_number,
            email_address = p_email_address,
            address = p_address,
            country_id = p_country_id
        WHERE org_id = p_org_id;
    ELSE
        -- Insert a new committee
        INSERT INTO committee (phone_number, email_address, address, country_id, org_id)
        VALUES (p_phone_number, p_email_address, p_address, p_country_id, p_org_id);
    END IF;

    COMMIT;
END;
$$;


--Procedure for inserting a row into the company table
CREATE OR REPLACE PROCEDURE insert_or_update_company(
    p_name VARCHAR,
    p_phone_number VARCHAR,
    p_email_address VARCHAR,
    p_address VARCHAR,
    p_country_id INTEGER,
    p_number_of_employees INTEGER
)
AS $$
BEGIN
    -- Check if the company exists based on the provided name
    IF EXISTS (
        SELECT 1
        FROM company
        WHERE name = p_name
    ) THEN
        -- Update existing company
        UPDATE company
        SET phone_number = p_phone_number,
            email_address = p_email_address,
            address = p_address,
            country_id = p_country_id,
            number_of_employees = p_number_of_employees
        WHERE name = p_name;
    ELSE
        -- Insert a new company
        INSERT INTO company (name, phone_number, email_address, address, country_id, number_of_employees)
        VALUES (p_name, p_phone_number, p_email_address, p_address, p_country_id, p_number_of_employees);
    END IF;

    COMMIT;
END;
$$;


--Procedure for inserting a row into the educational_institute table
CREATE OR REPLACE PROCEDURE insert_or_update_educational_institute(
    p_name VARCHAR,
    p_superior_id INTEGER
)
AS $$
BEGIN
    -- Check if the educational institute exists based on the provided name
    IF EXISTS (
        SELECT 1
        FROM educational_institute
        WHERE name = p_name
    ) THEN
        -- Update existing educational institute
        UPDATE educational_institute
        SET superior_id = p_superior_id
        WHERE name = p_name;
    ELSE
        -- Insert a new educational institute
        INSERT INTO educational_institute (name, superior_id)
        VALUES (p_name, p_superior_id);
    END IF;

    COMMIT;
END;
$$;


--Procedure for inserting a row into the experience table
CREATE OR REPLACE PROCEDURE insert_or_update_experience(
    p_type_of_job VARCHAR,
    p_description VARCHAR,
    p_start_year DATE,
    p_duration_in_weeks INTEGER,
    p_student_id INTEGER
)
AS $$
BEGIN
    -- Check if the experience exists based on the provided type_of_job and student_id
    IF EXISTS (
        SELECT 1
        FROM experience
        WHERE type_of_job = p_type_of_job
            AND student_id = p_student_id
    ) THEN
        -- Update existing experience
        UPDATE experience
        SET description = p_description,
            start_year = p_start_year,
            duration_in_weeks = p_duration_in_weeks
        WHERE type_of_job = p_type_of_job
            AND student_id = p_student_id;
    ELSE
        -- Insert a new experience
        INSERT INTO experience (type_of_job, description, start_year, duration_in_weeks, student_id)
        VALUES (p_type_of_job, p_description, p_start_year, p_duration_in_weeks, p_student_id);
    END IF;

    COMMIT;
END;
$$;


--Procedure for inserting a row into the internship table
CREATE OR REPLACE PROCEDURE insert_or_update_internship(
    p_grade_work INTEGER,
    p_grade_accommodation INTEGER,
    p_grade_student INTEGER,
    p_comment_student VARCHAR,
    p_comment_company VARCHAR,
    p_duration_in_weeks INTEGER,
    p_salary INTEGER,
    p_bonus_pay INTEGER,
    p_applies_for_student_id INTEGER,
    p_applies_for_offer_id INTEGER
)
AS $$
BEGIN
    -- Check if the internship exists based on the provided applies_for_student_id and applies_for_offer_id
    IF EXISTS (
        SELECT 1
        FROM internship
        WHERE applies_for_student_id = p_applies_for_student_id
            AND applies_for_offer_id = p_applies_for_offer_id
    ) THEN
        -- Update existing internship
        UPDATE internship
        SET grade_work = p_grade_work,
            grade_accommodation = p_grade_accommodation,
            grade_student = p_grade_student,
            comment_student = p_comment_student,
            comment_company = p_comment_company,
            duration_in_weeks = p_duration_in_weeks,
            salary = p_salary,
            bonus_pay = p_bonus_pay
        WHERE applies_for_student_id = p_applies_for_student_id
            AND applies_for_offer_id = p_applies_for_offer_id;
    ELSE
        -- Insert a new internship
        INSERT INTO internship (grade_work, grade_accommodation, grade_student,
                                comment_student, comment_company, duration_in_weeks,
                                salary, bonus_pay, applies_for_student_id, applies_for_offer_id)
        VALUES (p_grade_work, p_grade_accommodation, p_grade_student, p_comment_student, p_comment_company,
                p_duration_in_weeks, p_salary, p_bonus_pay, p_applies_for_student_id, p_applies_for_offer_id);
    END IF;

    COMMIT;
END;
$$;







CREATE OR REPLACE PROCEDURE insert_or_update_organization(
    p_name VARCHAR,
    p_phone_number VARCHAR,
    p_email_address VARCHAR,
    p_address VARCHAR,
    p_country_id INTEGER
)
AS $$
BEGIN
    -- Check if the organization exists based on the provided name
    IF EXISTS (
        SELECT 1
        FROM organization
        WHERE name = p_name
    ) THEN
        -- Update existing organization
        UPDATE organization
        SET phone_number = p_phone_number,
            email_address = p_email_address,
            address = p_address,
            country_id = p_country_id
        WHERE name = p_name;
    ELSE
        -- Insert a new organization
        INSERT INTO organization (name, phone_number, email_address, address, country_id)
        VALUES (p_name, p_phone_number, p_email_address, p_address, p_country_id);
    END IF;

    COMMIT;
END;
$$;


--Procedure for inserting a row into the project table
CREATE OR REPLACE PROCEDURE insert_or_update_project(
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
        FROM project
        WHERE name = p_name
    ) THEN
        -- Update existing project
        UPDATE project
        SET description = p_description,
            completeness = p_completeness,
            student_id = p_student_id
        WHERE name = p_name;
    ELSE
        -- Insert a new project
        INSERT INTO project (name, description, completeness, student_id)
        VALUES (p_name, p_description, p_completeness, p_student_id);
    END IF;

    COMMIT;
END;
$$;
