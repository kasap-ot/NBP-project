package mk.ukim.finki.nbp.aplipraksa.repository;

import mk.ukim.finki.nbp.aplipraksa.model.Country;
import mk.ukim.finki.nbp.aplipraksa.model.Faculty;
import mk.ukim.finki.nbp.aplipraksa.model.Major;
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
}
