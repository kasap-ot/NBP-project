package mk.ukim.finki.nbp.aplipraksa.controller;

import jakarta.servlet.http.HttpSession;
import mk.ukim.finki.nbp.aplipraksa.model.Country;
import mk.ukim.finki.nbp.aplipraksa.model.Faculty;
import mk.ukim.finki.nbp.aplipraksa.model.Major;
import mk.ukim.finki.nbp.aplipraksa.model.enumerations.StudyType;
import mk.ukim.finki.nbp.aplipraksa.repository.GlobalRepository;
import mk.ukim.finki.nbp.aplipraksa.repository.StudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.time.LocalDate;

@Controller
@RequestMapping("/")
public class RegisterController {

    private final StudentRepository studentRepository;
    private final GlobalRepository globalRepository;

    @Autowired
    public RegisterController(StudentRepository studentRepository, GlobalRepository globalRepository) {
        this.studentRepository = studentRepository;
        this.globalRepository = globalRepository;
    }

    @GetMapping("/register-as-student")
    public String getRegisterAsStudentPage(Model model, HttpSession session){
        //check wheather the user is already logged in.
        if(session.getAttribute("userCredentials")!=null)
            return "redirect:/offers";

        Iterable<Country> countries = this.globalRepository.findAllCountries();
        Iterable<Faculty> faculties = this.globalRepository.findAllFaculties();
        Iterable<Major> majors =this.globalRepository.findAllMajors();

        model.addAttribute("countries",countries);
        model.addAttribute("faculties",faculties);
        model.addAttribute("majors",majors  );
        model.addAttribute("studyTypes",StudyType.values());
        model.addAttribute("bodyContent", "register-as-student");
        return "master-template";
    }

    @PostMapping("/register-as-student")
    public String registerAsStudent(@RequestParam String username,
                                    @RequestParam String email,
                                    @RequestParam String password,
                                    @RequestParam String name,
                                    @RequestParam String surname,
                                    @RequestParam(name = "date-of-birth") LocalDate dateOfBirth,
                                    @RequestParam String address,
                                    @RequestParam String phone,
                                    @RequestParam(name="country") Integer countryId,
                                    @RequestParam(name="faculty") Integer facultyId,
                                    @RequestParam(name="major") Integer majorId,
                                    @RequestParam(name="study-level") String studyLevel,
                                    @RequestParam Float gpa,
                                    @RequestParam(name="start-year") Integer startYear,
                                    @RequestParam Integer credits, Model model, HttpSession session){
        //check wheather the user is already logged in.
        if(session.getAttribute("userCredentials")!=null)
            return "redirect:/offers";
        this.studentRepository.createStudent(username,password,name,surname,dateOfBirth,address,phone,email
                                            ,countryId, StudyType.valueOf(studyLevel),gpa,credits,majorId
                                            ,facultyId,startYear);
        return "redirect:/login";
    }

    @GetMapping("/register-as-member")
    public String getRegisterAsMemberPage(Model model,HttpSession session) {
        //check wheather the user is already logged in.
        if(session.getAttribute("userCredentials")!=null)
            return "redirect:/offers";
        model.addAttribute("bodyContent", "register-as-member");
        return "master-template";
    }
}
