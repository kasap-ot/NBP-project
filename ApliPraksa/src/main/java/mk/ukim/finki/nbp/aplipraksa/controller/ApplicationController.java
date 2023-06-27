package mk.ukim.finki.nbp.aplipraksa.controller;

import jakarta.servlet.http.HttpSession;
import mk.ukim.finki.nbp.aplipraksa.model.StudentApplication;
import mk.ukim.finki.nbp.aplipraksa.model.UserCredentials;
import mk.ukim.finki.nbp.aplipraksa.repository.StudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

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
    public String myApplicationsPage(@PathVariable(required = false) Integer pageNumber,Model model, HttpSession session) {
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

    @GetMapping("/{id}/give-feedback")
    public String giveFeedbackForm(
            @PathVariable Integer id,
            HttpSession session,
            Model model
    ) {
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        model.addAttribute("bodyContent", "give-feedback");
        model.addAttribute("userCredentials", userCredentials);
        model.addAttribute("offerId", id);
        return "master-template";
    }

    @PostMapping("/{id}/give-feedback")
    public String giveFeedbackForApplication(
            @PathVariable Integer id,
            @RequestParam Integer gradeWork,
            @RequestParam Integer gradeAccommodation,
            @RequestParam String commentByStudent,
            HttpSession session) {
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/offers";
        this.studentRepository.saveFeedback(userCredentials.getId(),id,gradeWork, gradeAccommodation, commentByStudent);
        return "redirect:/applications";
    }


    //@PostMapping za CANCEL
}

