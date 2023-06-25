package mk.ukim.finki.nbp.aplipraksa.controller;

import mk.ukim.finki.nbp.aplipraksa.model.StudentApplication;
import mk.ukim.finki.nbp.aplipraksa.repository.StudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
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

    @GetMapping("/{id}/applications")
    public String myAppliocationsPage(@PathVariable Integer id, Model model) {
        //id-to na student
        model.addAttribute("bodyContent", "my-applications");
        Iterable<StudentApplication> studentApplications = this.studentRepository.findMyApplications(id);
        model.addAttribute("studentApps", studentApplications);
        return "master-template";
    }

    //@PostMapping za CANCEL
}
