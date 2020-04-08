package com.trends.db.controller;

import com.trends.db.model.Patent;
import com.trends.db.service.PatentService;
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
import java.util.Optional;
import java.util.Set;

/**
 * The type Patent controller.
 */
@RestController
@RequestMapping("/v1/api")
public class PatentController {

  private final Logger logger = LoggerFactory.getLogger(this.getClass());

  @Autowired
  private final PatentService patentService;

  public PatentController(final PatentService patentService) {

    this.patentService = patentService;
  }

  /**
   * Gets patents.
   *
   * @param keyword the keyword
   * @return the patents
   */
  @ApiOperation(value = "Get Patents by keyword", nickname = "Get Patents by keyword", response = Patent.class)
  @GetMapping(path = "/patents/keyword/{keyword}")
  public Set<Patent> getPatents(@PathVariable final String keyword) {

    return patentService.findPatentsByKeyword(keyword);
  }

  /**
   * Gets patent.
   *
   * @param id the id
   * @return the patent
   */
  @ApiOperation(value = "Get Disease by Id", nickname = "Get Patents by id", response = Patent.class)
  @GetMapping(path = "/patents/id/{id}")
  public Optional<Patent> getPatent(@PathVariable final String id) {

    return patentService.findPatentsById(id);
  }

  /**
   * Add patents set.
   *
   * @param patents the patents
   * @return the set
   */
  @PostMapping(path = "/patents")
  public void addPatents(@RequestBody @Valid final Set<Patent> patents) {

    patentService.savePatents(patents);
  }

  /**
   * Add patent set.
   *
   * @param patent the patent
   * @return the set
   */
  @PostMapping(path = "/patent/add")
  public void addPatent(@RequestBody @Valid final Patent patent) {

    patentService.savePatent(patent);
  }

  /**
   * Update patents set.
   *
   * @param patent the patent
   * @return the set
   */
  @PutMapping(path = "/patents/update/{id}")
  public void updatePatents(@PathVariable final Integer id, @PathVariable final Patent patent) {

    patentService.updatePatent(patent);
  }
}
