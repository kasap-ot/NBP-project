package mk.ukim.finki.nbp.aplipraksa.filters;



import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import mk.ukim.finki.nbp.aplipraksa.model.UserCredentials;

import java.io.IOException;

@WebFilter()
public class LoginFilter implements Filter {
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

        }else if(!path.equals("/login") && userCredentials==null){
                response.sendRedirect("/login");
            }else{
                filterChain.doFilter(servletRequest,servletResponse);
            }
        }



    @Override
    public void destroy() {

    }
}


