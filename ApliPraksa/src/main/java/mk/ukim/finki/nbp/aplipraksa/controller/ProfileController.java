package mk.ukim.finki.nbp.aplipraksa.controller;

import jakarta.servlet.http.HttpSession;
import mk.ukim.finki.nbp.aplipraksa.model.*;
import mk.ukim.finki.nbp.aplipraksa.model.enumerations.JobType;
import mk.ukim.finki.nbp.aplipraksa.model.enumerations.LangLevel;
import mk.ukim.finki.nbp.aplipraksa.model.enumerations.StudyType;
import mk.ukim.finki.nbp.aplipraksa.repository.GlobalRepository;
import mk.ukim.finki.nbp.aplipraksa.repository.StudentRepository;
import org.apache.catalina.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;

@Controller
@RequestMapping("/profile")
public class ProfileController {

    private final StudentRepository studentRepository;
    private final GlobalRepository globalRepository;

    @Autowired
    public ProfileController(StudentRepository studentRepository, GlobalRepository globalRepository) {
        this.studentRepository = studentRepository;
        this.globalRepository = globalRepository;
    }

    @GetMapping()
    public String ProfilePage(Model model, HttpSession session) {
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");

        if(userCredentials.getType().equals("student")){
            //za student
            Integer studentId = userCredentials.getId();
            StudentProfileView studentProfileView = this.studentRepository.findProfileByStudentId(studentId);
            Iterable<Project> projects = this.studentRepository.findAllProjectsByStudentId(studentId);
            Iterable<Experience> experiences = this.studentRepository.findAllExperiencesByStudentId(studentId);
            Iterable<Certificate> certificates = this.studentRepository.findAllCertificatesByStudentId(studentId);
            Iterable<LanguageView> languages = this.studentRepository.findAllLanguagesByStudentId(studentId);
            model.addAttribute("profile",studentProfileView);
            model.addAttribute("projects",projects);
            model.addAttribute("experiences",experiences);
            model.addAttribute("certificates",certificates);
            model.addAttribute("languages",languages);
        }else{
            //za member
            //TODO: IMPLEMENTACIJZA ZA MEMBER
            return "redirect:/offers";
        }
        model.addAttribute("userCredentials",userCredentials);
        model.addAttribute("bodyContent", "profile");
        return "master-template";
    }

    @GetMapping("/edit")
    public String editProfilePage(Model model,HttpSession session) {
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(userCredentials.getType().equals("student")){
            //za student
            Integer studentId = userCredentials.getId();
            StudentProfileEditView studentProfileEditView = this.studentRepository.findProfileEditByStudentId(studentId);
            Iterable<Faculty> faculties = this.globalRepository.findAllFaculties();
            Iterable<Country> countries = this.globalRepository.findAllCountries();
            Iterable<Major> majors = this.globalRepository.findAllMajors();
            model.addAttribute("profile",studentProfileEditView);
            model.addAttribute("studyTypes", StudyType.values());
            model.addAttribute("countries",countries);
            model.addAttribute("faculties",faculties);
            model.addAttribute("majors",majors);
        }else{
            //za member
            //TODO: IMPLEMENTACIJZA ZA MEMBER
            return "redirect:/offers";
        }

        model.addAttribute("userCredentials",userCredentials);
        model.addAttribute("bodyContent", "edit-profile");
        return "master-template";
    }
    @PostMapping("/edit")
    public String editProfile(@PathVariable Integer id,
                              @RequestParam String name,
                              @RequestParam String surname,
                              @RequestParam(name = "date-of-birth") LocalDate dateOfBirth,
                              @RequestParam String password,
                              @RequestParam String address,
                              @RequestParam(name="phone-number") String phoneNumber,
                              @RequestParam String email,
                              @RequestParam(name="country-id") Integer countryId,
                              @RequestParam(name="type-of-study") String typeOfStudy,
                              @RequestParam (name="faculty-id") Integer facultyId,
                              @RequestParam(name="major-id") Integer majorId,
                              @RequestParam(name="start-of-studies") Integer startOfStudies,
                              @RequestParam Float gpa,
                              @RequestParam Integer credits, Model model,HttpSession session){
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(userCredentials.getType().equals("student")){
            this.studentRepository.updateStudent(id,password,name,surname,dateOfBirth,address,phoneNumber,email,countryId,typeOfStudy,gpa,credits,majorId,facultyId,startOfStudies);
        }else{
            //TODO: IMPLEMENTACIJA ZA MEMBER
        }

        return "redirect:/profile";
    }
//    @GetMapping("/{id}/delete")
//    public String deleteProfile(@PathVariable Integer id){
//        this.studentRepository.deleteStudent(id);
//        return "/home";
//    }

    @GetMapping("/add-project")
    public String addProjectPage(Model model,HttpSession session) {
        //Samo student mozhe da pristapi
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/profile";
        model.addAttribute("userCredentials",userCredentials);
        model.addAttribute("bodyContent", "add-project");
        return "master-template";
    }
    @PostMapping("/add-project")
    public String addProject(@RequestParam String name,
                             @RequestParam String description,
                             @RequestParam String completeness,
                             Model model,HttpSession session){
        //Samo student mozhe da pristapi
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/profile";
        this.studentRepository.addProject(userCredentials.getId(),name,description,completeness);
        return "redirect:/profile";
    }
    @GetMapping("/delete-project/{prId}")
    public String deleteProject(@PathVariable Integer prId,HttpSession session) {
        //Samo student mozhe da pristapi
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/profile";
        this.studentRepository.deleteProject(prId);
        return "redirect:/profile";
    }

    @GetMapping("/add-certificate")
    public String addCertificatePage(Model model,HttpSession session) {
        //Samo student mozhe da pristapi
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/profile";
        model.addAttribute("userCredentials",userCredentials);
        model.addAttribute("bodyContent", "add-certificate");
        return "master-template";
    }
    @PostMapping("/add-certificate")
    public String addCertificate(@RequestParam String name,
                             @RequestParam String description,
                             @RequestParam(name = "date-of-issue",required = false) LocalDate dateOfIssue,
                             @RequestParam String publisher,
                             Model model,HttpSession session){
        //Samo student mozhe da pristapi
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/profile";
        this.studentRepository.addCertificate(userCredentials.getId(),name,description,dateOfIssue,publisher);
        return "redirect:/profile";
    }
    @GetMapping("/delete-certificate/{crId}")
    public String deleteCertificate( @PathVariable Integer crId, Model model,HttpSession session) {
        //samo student
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/profile";
        this.studentRepository.deleteCertificate(crId);
        return "redirect:/profile";
    }



    @GetMapping("/{id}/add-language")
    public String addLanguagePage(@PathVariable String id,Model model){
        model.addAttribute("bodyContent", "add-language");
        model.addAttribute("langLevels", LangLevel.values());
        model.addAttribute("languages",this.studentRepository.findAllLanguages());
        model.addAttribute("studentId",id);
        return "master-template";

    }
    @PostMapping("/{id}/add-language")
    public String addLanguage(@PathVariable Integer id,
                              @RequestParam(name = "lang-id") Integer langId,
                              @RequestParam String level,
                              Model model){
        this.studentRepository.addLanguage(id,langId,level);
        return "redirect:/profile/"+id.toString();
    }
    @GetMapping("/{stId}/delete-language/{laId}")
    public String deleteLanguage(@PathVariable Integer stId, @PathVariable Integer laId, Model model) {
        this.studentRepository.deleteLanguage(laId,stId);
        return "redirect:/profile/"+stId;
    }
    @GetMapping("/add-experience")
    public String addExperiencePage( Model model,HttpSession session) {
        UserCredentials userCredentials = (UserCredentials) session.getAttribute("userCredentials");
        if(!userCredentials.getType().equals("student"))
            return "redirect:/profile";
        model.addAttribute("bodyContent", "add-experience");
        model.addAttribute("jobTypes",JobType.values());

        return "master-template";
    }
    @PostMapping("/{id}/add-experience")
    public String addExperience(@PathVariable Integer id,
                                @RequestParam(name = "job-type") String jobType,
                                @RequestParam(required = false) String description,
                                @RequestParam(name="start-date",required = false) LocalDate startDate,
                                @RequestParam(name="duration",required = false) Integer durationInWeeks, Model model){
        this.studentRepository.addExperience(id, jobType,description,startDate,durationInWeeks);
        return "redirect:/profile/"+id.toString();
    }
    @GetMapping("/{stId}/delete-experience/{exId}")
    public String deleteExperience(@PathVariable Integer stId, @PathVariable Integer exId, Model model) {
        this.studentRepository.deleteExperience(exId);
        return "redirect:/profile/"+stId;
    }

}
