package com.trends.db.controller;

import com.trends.db.model.Publication;
import com.trends.db.service.PublicationService;
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
 * The type Publication controller.
 */
@RestController
@RequestMapping("/v1/api")
public class PublicationController {

  private final Logger logger = LoggerFactory.getLogger(this.getClass());

  @Autowired
  private final PublicationService publicationService;

  public PublicationController(final PublicationService publicationService) {

    this.publicationService = publicationService;
  }

  /**
   * Gets publications.
   *
   * @param keyword the keyword
   * @return the publications
   */
  @ApiOperation(value = "Get Publications by keyword", nickname = "Get Publications by keyword", response =
      Publication.class)
  @GetMapping(path = "/publications/keyword/{keyword}")
  public Set<Publication> getPublications(@PathVariable final String keyword) {

    return publicationService.findPublicationsByKeyword(keyword);
  }

  /**
   * Gets publication.
   *
   * @param id the id
   * @return the publication
   */
  @ApiOperation(value = "Get Publications by Id", nickname = "Get Publications by id", response = Publication.class)
  @GetMapping(path = "/publications/id/{id}")
  public Optional<Publication> getPublication(@PathVariable final String id) {

    return publicationService.findPublicationsById(id);
  }

  /**
   * Add publications set.
   *
   * @param publications the publications
   * @return the set
   */
  @PostMapping(path = "/publications")
  public void addPublications(@RequestBody @Valid final Set<Publication> publications) {

    publicationService.savePublications(publications);
  }

  /**
   * Add publication set.
   *
   * @param publication the publication
   * @return the set
   */
  @PostMapping(path = "/publication/add")
  public void addPublication(@RequestBody @Valid final Publication publication) {

    publicationService.savePublication(publication);
  }

  /**
   * Update publications set.
   *
   * @param publication the publication
   * @return the set
   */
  @PutMapping(path = "/publications/update/{id}")
  public void updatePublications(@PathVariable final Integer id, @RequestBody @Valid final Publication publication) {

    publicationService.updatePublication(publication);
  }
}
