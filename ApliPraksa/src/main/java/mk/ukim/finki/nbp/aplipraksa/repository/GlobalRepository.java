package mk.ukim.finki.nbp.aplipraksa.repository;

import mk.ukim.finki.nbp.aplipraksa.model.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class GlobalRepository {
    public JdbcTemplate jdbc;
    
    @Autowired
    public GlobalRepository(JdbcTemplate jdbcTemplate){
        this.jdbc=jdbcTemplate;
    }

    public Iterable<Faculty> findAllFaculties() {
        return jdbc.query("select * from nbp_project.educational_institute as ed where ed.superior_id is not null",Faculty::mapRowToFaculty);
    }

    public Iterable<Country> findAllCountries() {
        return jdbc.query("select * from nbp_project.country",Country::mapRowToCountry);
    }

    public Iterable<Major> findAllMajors() {
        return jdbc.query("select * from nbp_project.major",Major::mapRowToMajor);
    }
    public Iterable<OfferShortView> findAllActiveOffers(Integer pageNumber){
        return jdbc.query("select * from nbp_project.active_offers(?)", OfferShortView::mapRowToOfferView,pageNumber);
    }
    public Iterable<CompanyView> findAllCompaniesViewOnPage(Integer pageNumber){
        return jdbc.query("select * from nbp_project.companies_view_on_page(?)",CompanyView::mapRowToCompanyView,pageNumber);
    }

    public Offer findOfferById(Integer id) {
        return jdbc.queryForObject("select * from nbp_project.offer",Offer::mapRowToOffer);
    }

    public Iterable<Company> findAllCompanies() {
        return jdbc.query("select * from nbp_project.company",Company::mapRowToCompany);
    }
}