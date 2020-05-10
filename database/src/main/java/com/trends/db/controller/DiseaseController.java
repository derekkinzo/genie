package com.trends.db.controller;

import com.trends.db.model.Disease;
import com.trends.db.model.exception.DiseaseException;
import com.trends.db.service.DiseaseService;
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
 * The type Disease controller.
 */
@RestController
@RequestMapping("/v1/api")
public class DiseaseController {

  private static final Logger _logger = LoggerFactory.getLogger(DiseaseController.class);

  private final DiseaseService diseaseService;

  public DiseaseController(final DiseaseService diseaseService) {

    this.diseaseService = diseaseService;
  }

  @ApiOperation(value = "Get Diseases by Keyword", nickname = "Get Diseases by keyword", response = Disease.class)
  @GetMapping(path = "/diseases", produces = "application/json")
  public ResponseEntity<List<Disease>> getAllDiseases() {

    _logger.info("Getting all disease...");

    final List<Disease> diseases;

    try {
      diseases = diseaseService.findAllDiseases();
    } catch (DiseaseException e) {
      _logger.error("Disease fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!diseases.isEmpty()) {
      return ResponseEntity.ok().body(diseases);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets diseases.
   *
   * @param keyword the keyword
   * @return the diseases
   */
  @ApiOperation(value = "Get Diseases by Keyword", nickname = "Get Diseases by keyword", response = Disease.class)
  @GetMapping(path = "/diseases/keyword/{keyword}", produces = "application/json")
  public ResponseEntity<Set<Disease>> getDiseases(@PathVariable final String keyword) {

    _logger.info("Getting diseases for keyword: {}", keyword);
    final Set<Disease> diseases;

    try {
      diseases = diseaseService.findDiseasesByKeyword(keyword);
    } catch (DiseaseException e) {
      _logger.error("Disease fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!diseases.isEmpty()) {
      return ResponseEntity.ok().body(diseases);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets disease.
   *
   * @param id the keyword
   * @return the diseases
   */
  @ApiOperation(value = "Get Disease by Id", nickname = "Get Diseases by id", response = Disease.class)
  @GetMapping(path = "/diseases/id/{id}", produces = "application/json")
  public ResponseEntity<Disease> getDiseaseById(@PathVariable final String id) {

    _logger.info("Getting disease by id: {}", id);

    final Optional<Disease> disease;

    try {
      disease = diseaseService.findDiseaseById(id);
    } catch (DiseaseException e) {
      _logger.error("Disease fetch failed");
      return ResponseEntity.notFound().build();
    }

    return disease.map(value -> ResponseEntity.ok().body(value))
                  .orElseGet(() -> ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build());

  }

  /**
   * Add disease
   *
   * @param disease the disease
   */
  @ApiOperation(value = "Add Disease", nickname = "Add a disease", response = Disease.class)
  @PostMapping(path = "/disease/add", consumes = "application/json")
  public void addDisease(@RequestBody @Valid final Disease disease) {

    diseaseService.saveDisease(disease);
  }

  /**
   * Update disease
   *
   * @param disease the disease to be updated
   */
  @ApiOperation(value = "Update a disease", nickname = "Update a disease by id", response = Disease.class)
  @PutMapping(path = "/diseases/update/{id}", consumes = "application/json")
  public ResponseEntity<Disease> updateDisease(@PathVariable final String id, @RequestBody final Disease disease) {

    Optional<Disease> foundDisease =
        Optional.ofNullable(diseaseService.findDiseaseById(id)
                                          .orElseThrow(
                                              () -> new DiseaseException(String.format("Disease id %s not found", id))));
    final Disease updateDisease = diseaseService.updateDisease(foundDisease.get(), disease);
    return ResponseEntity.ok(updateDisease);
  }

}
