package mk.ukim.finki.nbp.aplipraksa.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
@RequestMapping
public class OffersController {

    @GetMapping("/offers")
    public String offersPage(Model model) {
        model.addAttribute("bodyContent", "offers");
        return "master-template";
    }

    //PostMapping DELETE, EDIT
}
