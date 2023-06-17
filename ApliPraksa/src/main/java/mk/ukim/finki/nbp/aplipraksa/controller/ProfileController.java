package mk.ukim.finki.nbp.aplipraksa.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/profile")
public class ProfileController {

    @GetMapping("/{id}")
    public String ProfilePage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "profile");
        return "master-template";
    }

    @GetMapping("/{id}/edit")
    public String editProfilePage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "edit-profile");
        return "master-template";
    }

    @GetMapping("/{id}/add-project")
    public String addProjectPage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "add-project");
        return "master-template";
    }

    @GetMapping("/{id}/add-certificate")
    public String addCertificatePage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "add-certificate");
        return "master-template";
    }

    @GetMapping("/{id}/add-experience")
    public String addExperiencePage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "add-experience");
        return "master-template";
    }

}
