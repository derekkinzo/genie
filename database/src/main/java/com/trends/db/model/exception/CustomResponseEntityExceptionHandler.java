package com.trends.db.model.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

import java.util.Date;

@ControllerAdvice
@RestController
public class CustomResponseEntityExceptionHandler extends ResponseEntityExceptionHandler {

  @ExceptionHandler({ Exception.class })
  public final ResponseEntity<Object> handleAllExceptions(final Exception exception, final WebRequest webRequest) {

    ExceptionResponse exceptionResponse = new ExceptionResponse(new Date(), exception.getMessage(),
        webRequest.getDescription(false));

    return new ResponseEntity<>(exceptionResponse, HttpStatus.INTERNAL_SERVER_ERROR);
  }

  @ExceptionHandler({ DiseaseException.class, TrendException.class, GeneException.class, PatentException.class,
                      PublicationException.class, TrialException.class
  })
  public final ResponseEntity<Object> handleNotFoundException(final Exception exception,
                                                              final WebRequest webRequest) {

    ExceptionResponse exceptionResponse = new ExceptionResponse(new Date(), exception.getMessage(),
        webRequest.getDescription(false));

    return new ResponseEntity<>(exceptionResponse, HttpStatus.NOT_FOUND);
  }

  @ExceptionHandler({ FileExportException.class })
  public final ResponseEntity<Object> handleFileExportException(final Exception exception, final WebRequest webRequest) {

    ExceptionResponse exceptionResponse = new ExceptionResponse(new Date(), exception.getMessage(),
        webRequest.getDescription(false));

    return new ResponseEntity<>(exceptionResponse, HttpStatus.INTERNAL_SERVER_ERROR);
  }

  @ExceptionHandler({ AuthenticationException.class })
  public final ResponseEntity<Object> handleAuthException(final Exception exception, final WebRequest webRequest) {

    ExceptionResponse exceptionResponse = new ExceptionResponse(new Date(), exception.getMessage(),
        webRequest.getDescription(false));

    return new ResponseEntity<>(exceptionResponse, HttpStatus.UNAUTHORIZED);
  }
}
