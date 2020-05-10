package com.trends.db.controller;

import com.trends.db.model.Gene;
import com.trends.db.model.exception.DiseaseException;
import com.trends.db.model.exception.GeneException;
import com.trends.db.model.exception.TrialException;
import com.trends.db.service.GeneService;
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
 * The type Gene controller.
 */
@RestController
@RequestMapping("/v1/api")
public class GeneController {

  private static final Logger _logger = LoggerFactory.getLogger(GeneController.class);

  private final GeneService geneService;

  public GeneController(final GeneService geneService) {

    this.geneService = geneService;
  }

  @ApiOperation(value = "Get All Genes", nickname = "Get All Genes", response = Gene.class)
  @GetMapping(path = "/genes", produces = "application/json")
  public ResponseEntity<List<Gene>> getAllGenes() {

    _logger.info("Getting all genes...");

    final List<Gene> genes;

    try {
      genes = geneService.findAllGenes();
    } catch (GeneException e) {
      _logger.error("Gene fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!genes.isEmpty()) {
      return ResponseEntity.ok().body(genes);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets genes.
   *
   * @param keyword the keyword
   * @return the genes
   */
  @ApiOperation(value = "Get Genes by keyword", nickname = "Get Genes by keyword", response = Gene.class)
  @GetMapping(path = "/genes/keyword/{keyword}", produces = "application/json")
  public ResponseEntity<Set<Gene>> getGenesByKeyword(@PathVariable final String keyword) {

    _logger.info("Getting genes for keyword: {}", keyword);
    final Set<Gene> genes;

    try {
      genes = geneService.findGenesByKeyword(keyword);
    } catch (DiseaseException e) {
      _logger.error("Gene fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!genes.isEmpty()) {
      return ResponseEntity.ok().body(genes);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets gene.
   *
   * @param id the id
   * @return the gene
   */
  @ApiOperation(value = "Get Genes by Id", nickname = "Get Genes by id", response = Gene.class)
  @GetMapping(path = "/genes/id/{id}", produces = "application/json")
  public ResponseEntity<Gene> getGeneById(@PathVariable final String id) {

    _logger.info("Getting gene for id: {}", id);
    final Optional<Gene> gene;

    try {
      gene = geneService.findGenesById(id);
    } catch (DiseaseException e) {
      _logger.error("Gene fetch failed");
      return ResponseEntity.notFound().build();
    }

    return gene.map(value -> ResponseEntity.ok().body(value))
               .orElseGet(() -> ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build());
  }

  /**
   * Add gene
   *
   * @param gene the gene
   * @return the set
   */
  @PostMapping(path = "/gene/add", consumes = "application/json")
  public void addGene(@RequestBody @Valid final Gene gene) {

    geneService.saveGene(gene);
  }

  /**
   * Update genes
   *
   * @param gene the gene
   * @return the set
   */
  @PutMapping(path = "/gene/update/{id}", consumes = "application/json")
  public ResponseEntity<Gene> updateGene(@PathVariable final String id, @RequestBody @Valid final Gene gene) {

    Optional<Gene> foundGene =
        Optional.ofNullable(geneService.findGenesById(id)
                                       .orElseThrow(
                                           () -> new TrialException(String.format("Gene id %s not found", id))));
    final Gene updatedGene = geneService.updateGene(foundGene.get(), gene);
    return ResponseEntity.ok(updatedGene);
  }
}
