package mk.ukim.finki.nbp.aplipraksa.controller;

import jakarta.servlet.http.HttpSession;
import mk.ukim.finki.nbp.aplipraksa.model.StudentApplication;
import mk.ukim.finki.nbp.aplipraksa.model.UserCredentials;
import mk.ukim.finki.nbp.aplipraksa.repository.StudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping
//Preavtentifikacija, SAMO ZA STUDENT
public class ApplicationController {

    private final StudentRepository studentRepository;

    @Autowired
    public ApplicationController(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    @GetMapping(value = {"/applications","/applications/{pageNumber}"})
    public String myAppliocationsPage(@PathVariable(required = false) Integer pageNumber,Model model, HttpSession session) {
        //Samo student mozhe da pristapuva
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/profile";;
        Integer pageNum = (pageNumber == null || pageNumber <= 0) ? Integer.valueOf(1) : pageNumber;
        Iterable<StudentApplication> studentApplications = this.studentRepository.findMyApplications(userCredentials.getId(),pageNum);
        model.addAttribute("studentApps", studentApplications);
        model.addAttribute("userCredentials",userCredentials);
        model.addAttribute("pageNumber",pageNum);
        model.addAttribute("bodyContent", "my-applications");
        return "master-template";
    }

    @GetMapping("/applications/cancel/{appId}")
    public String deleteMyApplication(@PathVariable Integer appId,HttpSession session){
        //Samo student mozhe da pristapuva
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/profile";
        this.studentRepository.deleteMyApplication(userCredentials.getId(),appId);
        return "redirect:/applications";
    }

    @GetMapping("/give-feedback")
    public String giveFeedbackForApplication(HttpSession session) {
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        return null;
    }


    //@PostMapping za CANCEL
}

