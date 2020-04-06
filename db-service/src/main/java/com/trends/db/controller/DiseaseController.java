package com.trends.db.controller;

import com.trends.db.model.Disease;
import com.trends.db.service.DiseaseService;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
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

  private final Logger logger = LoggerFactory.getLogger(this.getClass());

  private final DiseaseService diseaseService;

  public DiseaseController(final DiseaseService diseaseService) {

    this.diseaseService = diseaseService;
  }

  @ApiOperation(value = "Get Diseases by Keyword", nickname = "Get Diseases by keyword", response = Disease.class)
  @GetMapping(path = "/diseases")
  public List<Disease> getAllDiseases() {

    return diseaseService.findAllDiseases();
  }

  /**
   * Gets diseases.
   *
   * @param keyword the keyword
   * @return the diseases
   */
  @ApiOperation(value = "Get Diseases by Keyword", nickname = "Get Diseases by keyword", response = Disease.class)
  @GetMapping(path = "/diseases/keyword/{keyword}")
  public Set<Disease> getDiseases(@PathVariable final String keyword) {

    return diseaseService.findDiseasesByKeyword(keyword);
  }

  /**
   * Gets disease.
   *
   * @param id the keyword
   * @return the diseases
   */
  @ApiOperation(value = "Get Disease by Id", nickname = "Get Diseases by id", response = Disease.class)
  @GetMapping(path = "/diseases/id/{id}")
  public ResponseEntity getDiseaseById(@PathVariable final String id) {

    Optional<Disease> disease = diseaseService.findDiseasesById(id);
    if (disease.isPresent()) {
      return ResponseEntity.ok().body(disease.get());
    }
    else {
      return ResponseEntity.notFound().build();
    }
  }

  /**
   * Add diseases set.
   *
   * @param diseases the diseases
   */
  @PostMapping(path = "/diseases")
  public void addDiseases(@RequestBody final Set<Disease> diseases) {

    diseaseService.saveDiseases(diseases);
  }

  /**
   * Add disease
   *
   * @param disease the disease
   */
  @PostMapping(path = "/disease/add", consumes = "application/json")
  public void addDisease(@RequestBody @Valid final Disease disease) {

    diseaseService.saveDisease(disease);
  }

  /**
   * Update disease set.
   *
   * @param disease the disease to be updated
   */
  @PutMapping(path = "/diseases/update/{id}")
  public void updateDisease(@PathVariable final Integer id, @RequestBody final Disease disease) {

    diseaseService.updateDisease(disease);
  }

}
