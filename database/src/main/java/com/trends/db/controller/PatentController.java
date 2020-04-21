package com.trends.db.controller;

import com.trends.db.model.Patent;
import com.trends.db.model.exception.DiseaseException;
import com.trends.db.model.exception.PatentException;
import com.trends.db.model.exception.TrialException;
import com.trends.db.service.PatentService;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;
import java.util.List;
import java.util.Optional;
import java.util.Set;

/**
 * The type Patent controller.
 */
@RestController
@RequestMapping("/v1/api")
public class PatentController {

  private static final Logger _logger = LoggerFactory.getLogger(PatentController.class);

  private final PatentService patentService;

  public PatentController(final PatentService patentService) {

    this.patentService = patentService;
  }

  /**
   * Gets all patents.
   *
   * @return the patents
   */
  @ApiOperation(value = "Get Patents by keyword", nickname = "Get All Patents", response = Patent.class)
  @GetMapping(path = "/patents", produces = "application/json")
  public ResponseEntity<List<Patent>> getPatents() {

    _logger.info("Getting all patents...");

    final List<Patent> patents;

    try {
      patents = patentService.findAllPatents();
    } catch (PatentException e) {
      _logger.error("Patent fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!patents.isEmpty()) {
      return ResponseEntity.ok().body(patents);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets patents.
   *
   * @param keyword the keyword
   * @return the patents
   */
  @ApiOperation(value = "Get Patents by keyword", nickname = "Get Patents by keyword", response = Patent.class)
  @GetMapping(path = "/patents/keyword/{keyword}", produces = "application/json")
  public ResponseEntity<Set<Patent>> getPatentsByKeyword(@PathVariable final String keyword) {

    _logger.info("Getting patents for keyword: {}", keyword);
    final Set<Patent> patents;

    try {
      patents = patentService.findPatentsByKeyword(keyword);
    } catch (DiseaseException e) {
      _logger.error("Patent fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!patents.isEmpty()) {
      return ResponseEntity.ok().body(patents);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();

  }

  /**
   * Gets patent.
   *
   * @param id the id
   * @return the patent
   */
  @ApiOperation(value = "Get Patents by Id", nickname = "Get Patents by id", response = Patent.class)
  @GetMapping(path = "/patents/id/{id}", produces = "application/json")
  public ResponseEntity<Patent> getPatentById(@PathVariable final String id) {

    _logger.info("Getting patent for id: {}", id);
    final Optional<Patent> patent;

    try {
      patent = patentService.findPatentsById(id);
    } catch (DiseaseException e) {
      _logger.error("Patent fetch failed");
      return ResponseEntity.notFound().build();
    }

    return patent.map(value -> ResponseEntity.ok().body(value))
                 .orElseGet(() -> ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build());
  }

  @PostMapping(path = "/patent/add", consumes = "application/json")
  public void addPatent(@RequestBody @Valid final Patent patent) {

    patentService.savePatent(patent);
  }

  @PutMapping(path = "/patents/update/{id}", consumes = "application/json")
  public ResponseEntity<Patent> updatePatents(@PathVariable final String id, @PathVariable final Patent patent) {

    Optional<Patent> foundPatent =
        Optional.ofNullable(patentService.findPatentsById(id)
                                         .orElseThrow(
                                             () -> new TrialException(String.format("Patent id %s not found", id))));
    final Patent updatedPatent = patentService.updatePatent(foundPatent.get(), patent);
    return ResponseEntity.ok(updatedPatent);
  }
}
