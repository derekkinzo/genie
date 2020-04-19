package com.trends.db.controller;

import com.trends.db.model.ClinicalTrial;
import com.trends.db.service.ClinicalTrialService;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
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

  @Autowired
  private final ClinicalTrialService clinicalTrialService;

  public ClinicalTrialController(
      final ClinicalTrialService clinicalTrialService) {

    this.clinicalTrialService = clinicalTrialService;
  }

  @ApiOperation(value = "Get Trials by Keyword", nickname = "Get Trials by keyword", response = ClinicalTrial.class)
  @GetMapping(path = "/trials")
  public List<ClinicalTrial> getAllTrials() {

    return clinicalTrialService.findAllClinicalTrials();
  }

  /**
   * Gets trials.
   *
   * @param keyword the keyword
   * @return the trials
   */
  @ApiOperation(value = "Get Trials by Keyword", nickname = "Get Trials by keyword", response = ClinicalTrial.class)
  @GetMapping(path = "/trials/keyword/{keyword}")
  public Set<ClinicalTrial> getTrials(@PathVariable final String keyword) {

    return clinicalTrialService.findClinicalTrialsByKeyword(keyword);
  }

  /**
   * Gets trial.
   *
   * @param id the id
   * @return the trial
   */
  @ApiOperation(value = "Get Trials by Id", nickname = "Get Trials by id", response = ClinicalTrial.class)
  @GetMapping(path = "/trial/id/{id}")
  public Optional<ClinicalTrial> getTrial(@PathVariable final String id) {

    return clinicalTrialService.findClinicalTrialsById(id);
  }

  /**
   * Add trials set.
   *
   * @param trials the trials
   * @return the set
   */
  @ApiOperation(value = "Add Trials", nickname = "Add Bulk Trials")
  @PostMapping(path = "/trials")
  public void addTrials(@RequestBody @Valid final Set<ClinicalTrial> trials) {

    clinicalTrialService.saveClinicalTrials(trials);
  }

  /**
   * Add trial set.
   *
   * @param trial the trial
   * @return the set
   */
  @ApiOperation(value = "Add Trial", nickname = "Add a single Trial")
  @PostMapping(path = "/trials/add")
  public void addTrial(@RequestBody @Valid final ClinicalTrial trial) {

    clinicalTrialService.saveClinicalTrial(trial);
  }

  /**
   * Update trials set.
   *
   * @param trial the trial
   * @return the set
   */
  @ApiOperation(value = "UpdateTrial", nickname = "Update a Trial")
  @PutMapping(path = "/trials/update/{id}")
  public void updateTrial(@PathVariable final Integer id, @RequestBody @Valid final ClinicalTrial trial) {

    clinicalTrialService.updateClinicalTrial(trial);
  }
}
