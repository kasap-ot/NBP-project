package mk.ukim.finki.nbp.aplipraksa.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/companies")
public class CompaniesController {

    @GetMapping
    public String companiesPage(Model model) {
        //NEZ DALI TREBA ID
        model.addAttribute("bodyContent", "companies");
        return "master-template";
    }

    @GetMapping("/{id}/add-offer")
//    @PreAuthorize("hasRole('ROLE_MEMBER')") - So security delot ke bide ovozmozeno
    public String addOfferPage(@PathVariable Long id, Model model) {
        //id na koja kompanija, dodavame offer
        model.addAttribute("bodyContent", "add-offer");
        return "master-template";
    }

}
