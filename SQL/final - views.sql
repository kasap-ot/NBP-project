create or replace view COMPLETED_OFFERS as
    select o.requirements, o.responsibilities, o.benefits,
           o.salary, o.field, o.start_date, o.duration_in_weeks,
           o.member_id, o.company_id, af.student_id, af.offer_id, af.acceptance_status
    from applies_for af join offer o on af.offer_id = o.id
    where acceptance_status=5;