package mk.ukim.finki.nbp.aplipraksa.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping
//Preavtentifikacija, SAMO ZA STUDENT
public class ApplicationController {

    @GetMapping("/{id}/applications")
    public String myAppliocationsPage(@PathVariable Long id, Model model) {
        //id-to na student
        model.addAttribute("bodyContent", "my-applications");
        return "master-template";
    }

    //@PostMapping za CANCEL
}
