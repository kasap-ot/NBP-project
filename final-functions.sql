--all languages known by student
create or replace function nbp_project.lang_known_by_student(
    p_student_id integer
) returns table(id integer,name varchar, level nbp_project.lang_level)
as
$$
begin
    return query
           select l.id, l.name,kw.level
           from nbp_project.knows_language as kw
                join nbp_project.language as l
                    on kw.lang_id = l.id
           where  kw.student_id = p_student_id;
end;
$$ language plpgsql;
--drop function nbp_project.lang_known_by_student(p_student_id integer);




--function that returns a view for a student's profile
create or replace function nbp_project.student_profile_view(
    p_student_id integer
)returns table(id integer, name varchar,surname varchar, age integer,country_name varchar
              ,study_level nbp_project.study, fac_name varchar, major varchar, start_year integer)
as
$$
    begin
        return query
            select  eu.id, eu.name, eu.surname,date_part('year',age(NOW(),eu.date_of_birth))::integer as age,cou.name as country_name,st.study_level,ed.name as fac_name,ma.major as major, st.start_year
            from nbp_project.end_user as eu
                    join nbp_project.country as cou on eu.country_id = cou.id
                    join nbp_project.student as st on eu.id = st.id
                    join nbp_project.educational_institute as ed on st.educational_institute_id = ed.id
                    join nbp_project.major as ma on ma.id = st.major_id
            where p_student_id = eu.id;
    end;
$$ language plpgsql;

-- drop function nbp_project.student_profile_view(p_student_id integer);


--view that will be called for populating the edit-profile.html
create or replace function nbp_project.student_profile_edit_view(
    p_student_id integer
)returns table(id integer, name varchar,surname varchar, date_of_birth date,username varchar,password varchar,
    address nbp_project.address,phone_number nbp_project.phone,email_address nbp_project.email,country_id integer,
    study_level nbp_project.study,major_id integer, fac_id integer, start_year integer, gpa nbp_project.gpa, ects_credits integer)
as
$$
begin
    return query
        select  eu.id, eu.name, eu.surname,eu.date_of_birth,eu.username,eu.password,eu.address,eu.phone_number,eu.email_address,eu.country_id
             ,st.study_level,st.major_id,st.educational_institute_id as fac_id, st.start_year,st.gpa,st.ects_credits
        from nbp_project.end_user as eu
                 join nbp_project.student as st on eu.id = st.id
        where p_student_id = eu.id;
end;
$$ language plpgsql;

--drop function nbp_project.student_profile_edit_view(p_student_id integer);

--active offers
create or replace function nbp_project.active_offers(
    p_page_number integer
) returns table(offer_id integer,country_name varchar,field varchar, start_date date
               , duration_in_weeks nbp_project.pos_int,company_name varchar)
as
$$
declare
    v_page_number integer = p_page_number;
begin
    if v_page_number < 1 then
        v_page_number = 1;
    end if;
    return query
        select o.id as offer_id, cou.name as country_name, o.field, o.start_date,o.duration_in_weeks, com.name as company_name
        from nbp_project.offer as o
                 join nbp_project.company as com on o.company_id= com.id
                 join nbp_project.country as cou on com.country_id = cou.id
        order by o.start_date desc
        limit 20 offset (p_page_number -1)*20;
end;
$$ language plpgsql;
--drop function nbp_project.active_offers(p_page_number integer);

--function that returns view for path: "/companies"
create or replace function nbp_project.companies_view_on_page(
    p_page_number integer
)returns table(id integer, name varchar, address nbp_project.address, country_name varchar
                , number_of_employees nbp_project.pos_int,offers_count bigint)
as
$$
declare
    v_page_number integer = p_page_number;
begin
    if v_page_number < 1 then
        v_page_number = 1;
    end if;
    return query
        select com.id, com.name, com.address,cou.name,com.number_of_employees,count(*) as offers_count
        from nbp_project.company as com
            join nbp_project.country as cou on com.country_id = cou.id
            join nbp_project.offer as of on of.company_id = com.id
        group by com.id, com.name, com.address,cou.name,com.number_of_employees
        order by count(*) desc
        limit 20 offset (p_page_number -1)*20;
end;
$$ language plpgsql;

create or replace function nbp_project.offer_edit_view(
    p_offer_id integer
) returns table(offer_id integer,country_name varchar,company_name varchar,company_address varchar,
    requirements varchar, responsibilities varchar, benefits varchar, salary nbp_project.pos_int,
     field varchar, start_date date, duration_in_weeks nbp_project.pos_int, acc_phone nbp_project.phone,
     acc_email nbp_project.email, acc_address nbp_project.address, acc_description varchar)
as
$$
    begin
        return query
            --implementacija: Treba da se vrativ infoрмации за држава, понуда и сместување
            --според имиња на колоне на табела што се враќа како резултат, може да се заклучи кои
            --точно иформации треба да се вратат.
    end;
$$ language plpgsql;

--drop function nbp_project.companies_view_on_page(p_page_number integer);

-- create  view nbp_project.active_offers_view as
-- select o.id as offer_id, cou.name as country_name, o.field, o.start_date,o.duration_in_weeks, com.name as company_name
-- from offer as o
--          join company as com on o.company_id= com.id
--          join country as cou on com.country_id = cou.id
--      --join applies_for as app on app.offer_id = o.id
--      --join acceptance_status as acc on acc.id = app.acceptance_status
-- order by o.start_date desc
