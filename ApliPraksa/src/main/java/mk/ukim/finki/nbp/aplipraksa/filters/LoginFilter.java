package mk.ukim.finki.nbp.aplipraksa.filters;



import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import mk.ukim.finki.nbp.aplipraksa.model.UserCredentials;

import java.io.IOException;
import java.util.Arrays;
import java.util.stream.Stream;

@WebFilter()
public class LoginFilter implements Filter {
    static private String[] sessionlessPaths = {
            "/register-as-student",
            "/register-as-member",
            "/login",
            "/home",
            "/about-us"
    };
    static private boolean isPathSessionless(String path){
        return Arrays.asList(sessionlessPaths).contains(path);
    }
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {

    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {

        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;



        String path = request.getServletPath();
        UserCredentials  userCredentials = (UserCredentials) request.getSession().getAttribute("userCredentials");

        if(path.contains(".css")){
            //continue
            filterChain.doFilter(servletRequest,servletResponse);

        }else if(!(isPathSessionless(path))&& userCredentials==null){
                response.sendRedirect("/home");
            }else{
                filterChain.doFilter(servletRequest,servletResponse);
            }
        }



    @Override
    public void destroy() {

    }
}


