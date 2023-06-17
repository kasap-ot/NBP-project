package mk.ukim.finki.nbp.aplipraksa.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
@RequestMapping
public class OffersController {

    @GetMapping("/offers")
    public String offersPage(Model model) {
        model.addAttribute("bodyContent", "offers");
        return "master-template";
    }

    @GetMapping("/add-offer")
//    @PreAuthorize("hasRole('ROLE_MEMBER')") - So security delot ke bide ovozmozeno
    public String addOfferPage(Model model) {
//        List<Manufacturer> manufacturers = this.manufacturerService.findAll();
//        List<Category> categories = this.categoryService.listCategories();
//        model.addAttribute("manufacturers", manufacturers);
//        model.addAttribute("categories", categories);
        //model.addAttribute - za firma, za contry
        model.addAttribute("bodyContent", "add-offer");
        return "master-template";
    }

    @GetMapping("/{id}/edit-offer")
    public String editProductPage(@PathVariable Long id, Model model) {
//        if(this.productService.findById(id).isPresent()){
//            Product product = this.productService.findById(id).get();
//            List<Manufacturer> manufacturers = this.manufacturerService.findAll();
//            List<Category> categories = this.categoryService.listCategories();
//            model.addAttribute("manufacturers", manufacturers);
//            model.addAttribute("categories", categories);
//            model.addAttribute("product", product);
        model.addAttribute("bodyContent", "add-product");
        return "master-template";
    }
//        return "redirect:/offers?error=ProductNotFound"; }


    //PostMapping DELETE, EDIT
}
