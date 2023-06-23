package mk.ukim.finki.nbp.aplipraksa.controller;

import mk.ukim.finki.nbp.aplipraksa.model.*;
import mk.ukim.finki.nbp.aplipraksa.model.enumerations.JobType;
import mk.ukim.finki.nbp.aplipraksa.model.enumerations.LangLevel;
import mk.ukim.finki.nbp.aplipraksa.model.enumerations.StudyType;
import mk.ukim.finki.nbp.aplipraksa.repository.GlobalRepository;
import mk.ukim.finki.nbp.aplipraksa.repository.StudentRepository;
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

    @GetMapping("/{id}")
    public String ProfilePage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "profile");
        Integer studentId = Integer.parseInt(id);
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
        return "master-template";
    }

    @GetMapping("/{id}/edit")
    public String editProfilePage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "edit-profile");
        Integer studentId = Integer.parseInt(id);
        StudentProfileEditView studentProfileEditView = this.studentRepository.findProfileEditByStudentId(studentId);
        Iterable<Faculty> faculties = this.globalRepository.findAllFaculties();
        Iterable<Country> countries = this.globalRepository.findAllCountries();
        Iterable<Major> majors = this.globalRepository.findAllMajors();
        model.addAttribute("profile",studentProfileEditView);
        model.addAttribute("studyTypes", StudyType.values());
        model.addAttribute("countries",countries);
        model.addAttribute("faculties",faculties);
        model.addAttribute("majors",majors);
        return "master-template";
    }
    @PostMapping("/{id}/edit")
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
                              @RequestParam Integer credits, Model model){
        this.studentRepository.updateStudent(id,password,name,surname,dateOfBirth,address,phoneNumber,email,countryId,typeOfStudy,gpa,credits,majorId,facultyId,startOfStudies);
        return "redirect:/profile/"+id.toString();
    }

    @GetMapping("/{id}/add-project")
    public String addProjectPage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "add-project");
        model.addAttribute("studentId",id);
        return "master-template";
    }
    @PostMapping("/{id}/add-project")
    public String addProject(@PathVariable Integer id,
                             @RequestParam String name,
                             @RequestParam String description,
                             @RequestParam String completeness,
                             Model model){

        this.studentRepository.addProject(id,name,description,completeness);
        return "redirect:/profile/"+id.toString();
    }
    @GetMapping("/{stId}/delete-project/{prId}")
    public String deleteProject(@PathVariable Integer stId, @PathVariable Integer prId, Model model) {
        this.studentRepository.deleteProject(prId);
        return "redirect:/profile/"+stId;
    }

    @GetMapping("/{id}/add-certificate")
    public String addCertificatePage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "add-certificate");
        model.addAttribute("studentId",id);
        return "master-template";
    }
    @PostMapping("/{id}/add-certificate")
    public String addCertificate(@PathVariable Integer id,
                             @RequestParam String name,
                             @RequestParam String description,
                             @RequestParam(name = "date-of-issue",required = false) LocalDate dateOfIssue,
                             @RequestParam String publisher,
                             Model model){

        this.studentRepository.addCertificate(id,name,description,dateOfIssue,publisher);
        return "redirect:/profile/"+id.toString();
    }
    @GetMapping("/{stId}/delete-certificate/{crId}")
    public String deleteCertificate(@PathVariable Integer stId, @PathVariable Integer crId, Model model) {
        this.studentRepository.deleteCertificate(crId);
        return "redirect:/profile/"+stId;
    }


    @GetMapping("/{id}/add-experience")
    public String addExperiencePage(@PathVariable String id, Model model) {
        model.addAttribute("bodyContent", "add-experience");
        model.addAttribute("jobTypes",JobType.values());
        model.addAttribute("studentId",id);
        return "master-template";
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
