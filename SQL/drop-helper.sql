-- DROP PROCEDURES

drop procedure nbp_project.insert_offer;
drop procedure nbp_project.update_offer;
drop procedure nbp_project.update_offer_accommodation;
drop procedure nbp_project.insert_end_user_student;
drop procedure nbp_project.update_end_user_student;
drop procedure nbp_project.insert_experience;
drop procedure nbp_project.insert_or_update_knows_language;
drop procedure nbp_project.insert_or_update_project;
drop procedure nbp_project.insert_or_update_certificate;
drop procedure nbp_project.student_apply_for_offer;


-- DROP FUNCTIONS

drop function nbp_project.lang_known_by_student;
drop function nbp_project.offer_detail_view;
drop function nbp_project.student_profile_view;
drop function nbp_project.student_profile_edit_view;
drop function nbp_project.active_offers;
drop function nbp_project.companies_view_on_page;
drop function nbp_project.offer_edit_view;
drop function nbp_project.student_application;
drop function nbp_project.offers_created_by_member;
drop function nbp_project.find_user_credentials_with_username_and_password;
drop function nbp_project.is_student;
drop function nbp_project.is_member;