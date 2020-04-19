package com.trends.db.controller;

import com.trends.db.model.Gene;
import com.trends.db.service.GeneService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;

import java.util.Arrays;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import static org.mockito.MockitoAnnotations.initMocks;

class GeneControllerTest {

  @Mock private GeneService mockGeneService;

  private GeneController geneControllerUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
    geneControllerUnderTest = new GeneController(mockGeneService);
  }

  @Test
  void testGetAllGenes() {
    // Setup

    // Configure GeneService.findAllGenes(...).
    final Gene gene = new Gene();
    gene.setId("id");
    gene.setApprovedGeneName("approvedGeneName");
    gene.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene.setAliases(new HashSet<>(Arrays.asList("value")));
    gene.setSymbolStatus(false);
    gene.setChromosomalLocation("chromosomalLocation");
    gene.setGeneGroup("geneGroup");
    gene.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    gene.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final List<Gene> genes = Arrays.asList(gene);
    when(mockGeneService.findAllGenes()).thenReturn(genes);

    // Run the test
    final List<Gene> result = geneControllerUnderTest.getAllGenes();

    // Verify the results
  }

  @Test
  void testGetGenes() {
    // Setup

    // Configure GeneService.findGenesByKeyword(...).
    final Gene gene = new Gene();
    gene.setId("id");
    gene.setApprovedGeneName("approvedGeneName");
    gene.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene.setAliases(new HashSet<>(Arrays.asList("value")));
    gene.setSymbolStatus(false);
    gene.setChromosomalLocation("chromosomalLocation");
    gene.setGeneGroup("geneGroup");
    gene.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    gene.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Set<Gene> genes = new HashSet<>(Arrays.asList(gene));
    when(mockGeneService.findGenesByKeyword("keyword")).thenReturn(genes);

    // Run the test
    final Set<Gene> result = geneControllerUnderTest.getGenes("keyword");

    // Verify the results
  }

  @Test
  void testGetGene() {
    // Setup

    // Configure GeneService.findGenesById(...).
    final Gene gene1 = new Gene();
    gene1.setId("id");
    gene1.setApprovedGeneName("approvedGeneName");
    gene1.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene1.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene1.setAliases(new HashSet<>(Arrays.asList("value")));
    gene1.setSymbolStatus(false);
    gene1.setChromosomalLocation("chromosomalLocation");
    gene1.setGeneGroup("geneGroup");
    gene1.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    gene1.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Optional<Gene> gene = Optional.of(gene1);
    when(mockGeneService.findGenesById("id")).thenReturn(gene);

    // Run the test
    final Optional<Gene> result = geneControllerUnderTest.getGene("id");

    // Verify the results
  }


  @Test
  void testAddGene() {
    // Setup
    final Gene gene = new Gene();
    gene.setId("id");
    gene.setApprovedGeneName("approvedGeneName");
    gene.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene.setAliases(new HashSet<>(Arrays.asList("value")));
    gene.setSymbolStatus(false);
    gene.setChromosomalLocation("chromosomalLocation");
    gene.setGeneGroup("geneGroup");
    gene.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    gene.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());

    // Run the test
    geneControllerUnderTest.addGene(gene);

    // Verify the results
    verify(mockGeneService).saveGene(any(Gene.class));
  }

  @Test
  void testUpdateGenes() {
    // Setup
    final Gene gene = new Gene();
    gene.setId("id");
    gene.setApprovedGeneName("approvedGeneName");
    gene.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene.setAliases(new HashSet<>(Arrays.asList("value")));
    gene.setSymbolStatus(false);
    gene.setChromosomalLocation("chromosomalLocation");
    gene.setGeneGroup("geneGroup");
    gene.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    gene.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());

    // Run the test
    geneControllerUnderTest.updateGenes(0, gene);

    // Verify the results
    verify(mockGeneService).updateGene(any(Gene.class));
  }
}
