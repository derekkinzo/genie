package com.trends.db.controller;

import com.trends.db.model.ClinicalTrial;
import com.trends.db.model.exception.DiseaseException;
import com.trends.db.model.exception.TrialException;
import com.trends.db.service.ClinicalTrialService;
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
 * The type Clinical trial controller.
 */
@RestController
@RequestMapping("/v1/api")
public class ClinicalTrialController {

  private static final Logger _logger = LoggerFactory.getLogger(ClinicalTrialController.class);

  private final ClinicalTrialService clinicalTrialService;

  public ClinicalTrialController(final ClinicalTrialService clinicalTrialService) {

    this.clinicalTrialService = clinicalTrialService;
  }

  @ApiOperation(value = "Get Trials by Keyword", nickname = "Get Trials by keyword", response = ClinicalTrial.class)
  @GetMapping(path = "/trials", produces = "application/json")
  public ResponseEntity<List<ClinicalTrial>> getAllTrials() {

    _logger.info("Getting all Trials...");

    final List<ClinicalTrial> trials;

    try {
      trials = clinicalTrialService.findAllClinicalTrials();
    } catch (TrialException e) {
      _logger.error("Trials fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!trials.isEmpty()) {
      return ResponseEntity.ok().body(trials);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets trials.
   *
   * @param keyword the keyword
   * @return the trials
   */
  @ApiOperation(value = "Get Trials by Keyword", nickname = "Get Trials by keyword", response = ClinicalTrial.class)
  @GetMapping(path = "/trials/keyword/{keyword}", produces = "application/json")
  public ResponseEntity<Set<ClinicalTrial>> getTrialsByKeyword(@PathVariable final String keyword) {

    _logger.info("Getting trials for keyword: {}", keyword);
    final Set<ClinicalTrial> trials;

    try {
      trials = clinicalTrialService.findClinicalTrialsByKeyword(keyword);
    } catch (TrialException e) {
      _logger.error("Trial fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!trials.isEmpty()) {
      return ResponseEntity.ok().body(trials);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets trial.
   *
   * @param id the id
   * @return the trial
   */
  @ApiOperation(value = "Get Trial by Id", nickname = "Get Trial by id", response = ClinicalTrial.class)
  @GetMapping(path = "/trial/id/{id}", produces = "application/json")
  public ResponseEntity<ClinicalTrial> getTrialById(@PathVariable final String id) {

    _logger.info("Getting trial by id: {}", id);

    final Optional<ClinicalTrial> trial;

    try {
      trial = clinicalTrialService.findClinicalTrialsById(id);
    } catch (DiseaseException e) {
      _logger.error("Trial fetch failed");
      return ResponseEntity.notFound().build();
    }

    return trial.map(value -> ResponseEntity.ok().body(value))
                .orElseGet(() -> ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build());
  }

  /**
   * Add trial set.
   *
   * @param trial the trial
   * @return the set
   */
  @ApiOperation(value = "Add Trial", nickname = "Add a single Trial")
  @PostMapping(path = "/trial/add", consumes = "application/json")
  public void addTrial(@RequestBody @Valid final ClinicalTrial trial) {

    clinicalTrialService.saveClinicalTrial(trial);
  }

  /**
   * Update a trial
   *
   * @param trial the trial
   * @return the set
   */
  @ApiOperation(value = "UpdateTrial", nickname = "Update a Trial")
  @PutMapping(path = "/trial/update/{id}", consumes = "application/json")
  public ResponseEntity<ClinicalTrial> updateTrial(@PathVariable final String id,
                                                   @RequestBody @Valid final ClinicalTrial trial) {

    Optional<ClinicalTrial> foundTrial =
        Optional.ofNullable(clinicalTrialService.findClinicalTrialsById(id)
                                                .orElseThrow(
                                                    () -> new TrialException(String.format("Trial id %s not found", id))));
    final ClinicalTrial updatedTrial = clinicalTrialService.updateClinicalTrial(foundTrial.get(), trial);
    return ResponseEntity.ok(updatedTrial);

  }
}
