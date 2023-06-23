package mk.ukim.finki.nbp.aplipraksa.model;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;

import java.sql.Date;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;

@Data
public class OfferView {
    private Integer offerId;
    private String countryName;
    private String fieldOfStudy;
    private String startingDate;
    private String lengthsInWeeks;
    private String companyName;
    //private int numberOfApplications;

    public OfferView(Integer offerId,String countryName, String fieldOfStudy, String startingDate, String lengthsInWeeks, String companyName) {
        this.offerId = offerId;
        this.countryName = countryName;
        this.fieldOfStudy = fieldOfStudy;
        this.startingDate = startingDate;
        this.lengthsInWeeks = lengthsInWeeks;
        this.companyName = companyName;
//        this.numberOfApplications = numberOfApplications;
    }

    public static OfferView mapRowToOfferView(ResultSet resultSet, int rowNum) throws SQLException {
        return new OfferView(
            Integer.parseInt(resultSet.getString("offer_id")),
            resultSet.getString("country_name"),
            resultSet.getString("field"),
            resultSet.getString("start_date"),
            resultSet.getString("duration_in_weeks"),
            resultSet.getString("company_name")
//           ,resultSet.getString("number_of_applications")
        );
    }


}
