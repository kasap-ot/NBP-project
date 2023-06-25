package mk.ukim.finki.nbp.aplipraksa;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;

@SpringBootApplication
@ServletComponentScan
public class ApliPraksaApplication {

    public static void main(String[] args) {
        SpringApplication.run(ApliPraksaApplication.class, args);
    }

}
