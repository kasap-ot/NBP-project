package mk.ukim.finki.nbp.aplipraksa.controller;

import mk.ukim.finki.nbp.aplipraksa.model.Company;
import mk.ukim.finki.nbp.aplipraksa.model.Offer;
import mk.ukim.finki.nbp.aplipraksa.model.OfferEditView;
import mk.ukim.finki.nbp.aplipraksa.model.OfferShortView;
import mk.ukim.finki.nbp.aplipraksa.repository.GlobalRepository;
import mk.ukim.finki.nbp.aplipraksa.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;


@Controller
@RequestMapping("/offers")
public class OffersController {
    private final GlobalRepository globalRepository;
    private final MemberRepository memberRepository;
    @Autowired
    public OffersController(GlobalRepository globalRepository, MemberRepository memberRepository) {
        this.globalRepository = globalRepository;
        this.memberRepository = memberRepository;
    }

    @GetMapping(value={"","/{pageNumber}"})
    public String offersPage(@PathVariable(required = false) Integer pageNumber, Model model) {
        model.addAttribute("bodyContent", "offers");
        Iterable<OfferShortView> offerViews = this.globalRepository.findAllActiveOffers((pageNumber == null)?Integer.valueOf(1):pageNumber);
        model.addAttribute("offerViews",offerViews);
        model.addAttribute("pageNumber",(pageNumber == null)?Integer.valueOf(1):pageNumber);
        model.addAttribute("memberId",6976); // treba od sesija da se vidi dali e member ili student.
        return "master-template";
    }

//    @GetMapping("/add-offer")
////    @PreAuthorize("hasRole('ROLE_MEMBER')") - So security delot ke bide ovozmozeno
//    public String addOfferPage(Model model) {
////        List<Manufacturer> manufacturers = this.manufacturerService.findAll();
////        List<Category> categories = this.categoryService.listCategories();
////        model.addAttribute("manufacturers", manufacturers);
////        model.addAttribute("categories", categories);
//        //model.addAttribute - za firma, za contry
//        model.addAttribute("bodyContent", "add-offer");
//        return "master-template";
//    }

    @GetMapping("/{id}/edit-offer")
    public String editOfferPage(@PathVariable Integer id, Model model) {
//        if(this.productService.findById(id).isPresent()){
//            Product product = this.productService.findById(id).get();
//            List<Manufacturer> manufacturers = this.manufacturerService.findAll();
//            List<Category> categories = this.categoryService.listCategories();
//            model.addAttribute("manufacturers", manufacturers);
//            model.addAttribute("categories", categories);
//            model.addAttribute("product", product);

        model.addAttribute("bodyContent", "edit-offer");
        OfferEditView offerEditView = this.memberRepository.findOfferEditView(id);
        model.addAttribute("memberId",7205); //memberId mora od sesija da se zeme
        model.addAttribute("offerEditView",offerEditView);
        return "master-template";
    }
    @PostMapping("/{id}/edit-offer")
    public String editOffer(@PathVariable Integer id,
                            @RequestParam String field,
                            @RequestParam String requirements,
                            @RequestParam String responsibilities,
                            @RequestParam String benefits,
                            @RequestParam Integer salary,
                            @RequestParam(name = "start-date") LocalDate startDate,
                            @RequestParam Integer duration,
                            @RequestParam(name="acc-phone") String accPhone,
                            @RequestParam(name="acc-email") String accEmail,
                            @RequestParam(name="acc-address") String accAddress,
                            @RequestParam(name="acc-description") String accDescription,
                            Model model){
        this.memberRepository.updateOfferAndAccommodation(id,requirements,responsibilities,benefits,salary,
                field,startDate,duration,accPhone,accEmail,accAddress,accDescription);
        return "redirect:/offers";
    }
    @GetMapping("/add-offer")
    public String addOfferPage(Model model) {
//        if(this.productService.findById(id).isPresent()){
//            Product product = this.productService.findById(id).get();
//            List<Manufacturer> manufacturers = this.manufacturerService.findAll();
//            List<Category> categories = this.categoryService.listCategories();
//            model.addAttribute("manufacturers", manufacturers);
//            model.addAttribute("categories", categories);
//            model.addAttribute("product", product);
        model.addAttribute("memberId",7205); //memberId mora od sesija da se zeme
        Iterable<Company> companies = this.globalRepository.findAllCompanies();
        model.addAttribute("companies",companies);
        model.addAttribute("bodyContent", "add-offer");
        return "master-template";
    }
    @PostMapping("/add-offer")
    public String addOffer(@RequestParam(name = "company-id") Integer companyId,
                           @RequestParam String field,
                           @RequestParam String requirements,
                           @RequestParam String responsibilities,
                           @RequestParam Integer salary,
                           @RequestParam String benefits,
                           @RequestParam(name = "start-date") LocalDate startDate,
                           @RequestParam Integer duration,
                           Model model) {
        Integer memberId = 7205;
        this.memberRepository.createOffer(requirements,responsibilities,benefits,salary,field,startDate,duration,memberId,companyId);
        return "redirect:/offers";
    }

//        return "redirect:/offers?error=ProductNotFound"; }

    @GetMapping("/{id}/applications")
    public String numberOfApplicationsPage(@PathVariable Long id, Model model) {
        model.addAttribute("bodyContent", "numOfApp");
        return "master-template";
    }


    //PostMapping DELETE, EDIT, NUMBER OF APPLICATIONS

}
