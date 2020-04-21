package com.trends.db.controller;

import com.trends.db.model.Publication;
import com.trends.db.model.exception.PublicationException;
import com.trends.db.model.exception.TrialException;
import com.trends.db.service.PublicationService;
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
 * The type Publication controller.
 */
@RestController
@RequestMapping("/v1/api")
public class PublicationController {

  private static final Logger _logger = LoggerFactory.getLogger(PublicationController.class);

  private final PublicationService publicationService;

  public PublicationController(final PublicationService publicationService) {

    this.publicationService = publicationService;
  }

  /**
   * Gets all publications.
   *
   * @return the publications
   */
  @ApiOperation(value = "Get All Publications", nickname = "Get All Publications", response =
      Publication.class)
  @GetMapping(path = "/publications", produces = "application/json")
  public ResponseEntity<List<Publication>> getPublications() {

    _logger.info("Getting all publications...");

    final List<Publication> publications;

    try {
      publications = publicationService.findAllPublications();
    } catch (PublicationException e) {
      _logger.error("Publication fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!publications.isEmpty()) {
      return ResponseEntity.ok().body(publications);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets publications.
   *
   * @param keyword the keyword
   * @return the publications
   */
  @ApiOperation(value = "Get Publications by keyword", nickname = "Get Publications by keyword", response =
      Publication.class)
  @GetMapping(path = "/publications/keyword/{keyword}", produces = "application/json")
  public ResponseEntity<Set<Publication>> getPublicationsByKeyword(@PathVariable final String keyword) {

    _logger.info("Getting publications for keyword: {}", keyword);
    final Set<Publication> publications;

    try {
      publications = publicationService.findPublicationsByKeyword(keyword);
    } catch (PublicationException e) {
      _logger.error("Publication fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!publications.isEmpty()) {
      return ResponseEntity.ok().body(publications);
    }

    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets publication.
   *
   * @param id the id
   * @return the publication
   */
  @ApiOperation(value = "Get Publications by Id", nickname = "Get Publications by id", response = Publication.class)
  @GetMapping(path = "/publications/id/{id}", produces = "application/json")
  public ResponseEntity<Publication> getPublicationById(@PathVariable final String id) {

    _logger.info("Getting publication for id: {}", id);
    final Optional<Publication> publication;

    try {
      publication = publicationService.findPublicationsById(id);
    } catch (PublicationException e) {
      _logger.error("Publication fetch failed");
      return ResponseEntity.notFound().build();
    }

    return publication.map(value -> ResponseEntity.ok().body(value))
                      .orElseGet(() -> ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build());

  }

  @PostMapping(path = "/publication/add", consumes = "application/json")
  public void addPublication(@RequestBody @Valid final Publication publication) {

    publicationService.savePublication(publication);
  }

  @PutMapping(path = "/publications/update/{id}", consumes = "application/json")
  public ResponseEntity<Publication> updatePublications(@PathVariable final String id,
                                                        @RequestBody @Valid final Publication publication) {

    Optional<Publication> foundPatent =
        Optional.ofNullable(publicationService.findPublicationsById(id)
                                              .orElseThrow(
                                                  () -> new TrialException(String.format("Publication id %s not found",
                                                      id))));
    final Publication updatedPublication = publicationService.updatePublication(foundPatent.get(), publication);
    return ResponseEntity.ok(updatedPublication);
  }
}
