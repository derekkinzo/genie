package com.trends.db.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true)
@EnableWebSecurity
public class TrendSecurityConfig extends WebSecurityConfigurerAdapter {

  @Autowired
  protected void configAuthentication(AuthenticationManagerBuilder auth) throws Exception {

    auth.inMemoryAuthentication()
        .withUser("user")
        .password("{noop}password")
        .roles("USER");
  }

  @Override
  protected void configure(HttpSecurity http) throws Exception {

    http.authorizeRequests()
        .antMatchers("/v2/api-docs", "/v1/api/", "/configuration/ui", "/swagger-resources/**", "/configuration/security",
            "/swagger-ui.html**", "/webjars/**").permitAll()
        .anyRequest().authenticated()
        .and()
        .logout()
        .permitAll()
        .and()
        .formLogin()
        .permitAll()
        .and().httpBasic();

    http.csrf().disable();
  }
}
