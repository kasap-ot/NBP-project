package mk.ukim.finki.nbp.aplipraksa.repository;

import jakarta.annotation.PostConstruct;

import mk.ukim.finki.nbp.aplipraksa.model.OfferView;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.sql.Date;
import java.time.LocalDate;

@Repository
public class OfferRepository {
    private JdbcTemplate jdbc;

    @Autowired
    public OfferRepository(JdbcTemplate jdbc){
        this.jdbc=jdbc;
    }
//    @PostConstruct
//    public void testCreateOffer(){
//        this.createOffer("0","0","0",1,"0", Date.valueOf("2019-01-10").toLocalDate(),2, 3,1);
//    }
    public void createOffer(String requirements,
                        String responsibilities,
                        String benefits,
                        Integer salary,
                        String field,
                        LocalDate startDate,
                        Integer durationInWeeks,
                        Integer memberId,
                        Integer companyId){
        jdbc.update("call nbp_project.insert_offer(?, ?,?,?,?,?,?,?,?)", requirements,responsibilities,benefits,salary,field,startDate,durationInWeeks,memberId,companyId);
    }
    public void deleteOffer(Integer offerId){
        jdbc.update("delete from nbp_project.offer where id=?",offerId);
    }
    public void updateOffer(Integer offerId,
                            String requirements,
                            String responsibilities,
                            String benefits,
                            Integer salary,
                            String field,
                            LocalDate startDate,
                            Integer durationInWeeks,
                            Integer memberId,
                            Integer companyId){
        jdbc.update("call nbp_project.update_offer(?, ?,?,?,?,?,?,?,?,?)",offerId,requirements,responsibilities,benefits,salary,field,startDate,durationInWeeks,memberId,companyId);
    }
//    @PostConstruct
//    public void testReadOfferView(){
//        Iterable<OfferView> offerViews = readOfferView();
//        System.out.println(offerViews.iterator().next().toString());
//    }
    public Iterable<OfferView> readOfferView(){
        return jdbc.query("select * from nbp_project.offer_view",OfferView::mapRowToOfferView);
    }
}
