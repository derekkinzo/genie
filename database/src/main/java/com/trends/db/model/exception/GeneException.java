package com.trends.db.model.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.NOT_FOUND)
public class GeneException extends RuntimeException {

  public GeneException(final String message) {

    super(message);
  }
}
