package com.trends.db.controller;

import com.trends.db.model.Gene;
import com.trends.db.service.GeneService;
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
 * The type Gene controller.
 */
@RestController
@RequestMapping("/v1/api")
public class GeneController {

  private final Logger logger = LoggerFactory.getLogger(this.getClass());

  @Autowired
  private final GeneService geneService;

  public GeneController(final GeneService geneService) {

    this.geneService = geneService;
  }

  @ApiOperation(value = "Get All Genes", nickname = "Get All Genes", response = Gene.class)
  @GetMapping(path = "/genes")
  public List<Gene> getAllGenes() {

    return geneService.findAllGenes();
  }

  /**
   * Gets genes.
   *
   * @param keyword the keyword
   * @return the genes
   */
  @ApiOperation(value = "Get Genes by keyword", nickname = "Get Genes by keyword", response = Gene.class)
  @GetMapping(path = "/genes/keyword/{keyword}")
  public Set<Gene> getGenes(@PathVariable final String keyword) {

    return geneService.findGenesByKeyword(keyword);
  }

  /**
   * Gets gene.
   *
   * @param id the id
   * @return the gene
   */
  @ApiOperation(value = "Get Genes by Id", nickname = "Get Genes by id", response = Gene.class)
  @GetMapping(path = "/genes/id/{id}")
  public Optional<Gene> getGene(@PathVariable final String id) {

    return geneService.findGenesById(id);
  }

  /**
   * Add genes set.
   *
   * @param genes the genes
   * @return the set
   */
  @PostMapping(path = "/genes")
  public void addGenes(@RequestBody @Valid final Set<Gene> genes) {

    geneService.saveGenes(genes);
  }

  /**
   * Add gene
   *
   * @param gene the gene
   * @return the set
   */
  @PostMapping(path = "/gene/add")
  public void addGene(@RequestBody @Valid final Gene gene) {

    geneService.saveGene(gene);
  }

  /**
   * Update genes
   *
   * @param gene the gene
   * @return the set
   */
  @PutMapping(path = "/genes/update/{id}")
  public void updateGenes(@PathVariable final Integer id, @RequestBody @Valid final Gene gene) {

    geneService.updateGene(gene);
  }
}
