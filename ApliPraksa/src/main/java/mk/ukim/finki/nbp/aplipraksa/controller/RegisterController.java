package mk.ukim.finki.nbp.aplipraksa.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class RegisterController {
    @GetMapping("/register-as-student")
    public String getHomePage(Model model){
        model.addAttribute("bodyContent", "register-as-student");
        return "master-template";
    }

    @GetMapping("/register-as-member")
    public String getRegisterAsMemberPage(Model model) {
        model.addAttribute("bodyContent", "register-as-member");
        return "master-template";
    }
}
