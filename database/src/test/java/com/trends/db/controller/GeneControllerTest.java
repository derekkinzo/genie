package com.trends.db.controller;

import com.trends.db.model.Gene;
import com.trends.db.service.GeneService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.util.Arrays;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;
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
    final ResponseEntity<List<Gene>> expectedResult = new ResponseEntity<>(
        Arrays.asList(
            new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, "chromosomalLocation", "geneGroup", "geneId",
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)), HttpStatus.OK);

    // Configure GeneService.findAllGenes(...).
    final List<Gene> genes = Arrays.asList(new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false, "chromosomalLocation", "geneGroup", "geneId",
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockGeneService.findAllGenes()).thenReturn(genes);

    // Run the test
    final ResponseEntity<List<Gene>> result = geneControllerUnderTest.getAllGenes();

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetGenesByKeyword() {
    // Setup
    final ResponseEntity<Set<Gene>> expectedResult = new ResponseEntity<>(new HashSet<>(
        Arrays.asList(
            new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, "chromosomalLocation", "geneGroup", "geneId",
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), HttpStatus.OK);

    // Configure GeneService.findGenesByKeyword(...).
    final Set<Gene> genes = new HashSet<>(
        Arrays.asList(
            new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, "chromosomalLocation", "geneGroup", "geneId",
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)));
    when(mockGeneService.findGenesByKeyword("keyword")).thenReturn(genes);

    // Run the test
    final ResponseEntity<Set<Gene>> result = geneControllerUnderTest.getGenesByKeyword("keyword");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetGeneById() {
    // Setup
    final ResponseEntity<Gene> expectedResult = new ResponseEntity<>(new Gene("approvedGeneName", new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        "chromosomalLocation", "geneGroup", "geneId", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure GeneService.findGenesById(...).
    final Optional<Gene> gene =
        Optional.of(new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false, "chromosomalLocation", "geneGroup",
            "geneId", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockGeneService.findGenesById("id")).thenReturn(gene);

    // Run the test
    final ResponseEntity<Gene> result = geneControllerUnderTest.getGeneById("id");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testAddGene() {
    // Setup
    final Gene gene =
        new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, "chromosomalLocation", "geneGroup", "geneId",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);

    // Run the test
    geneControllerUnderTest.addGene(gene);

    // Verify the results
    verify(mockGeneService).saveGene(new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false, "chromosomalLocation", "geneGroup", "geneId",
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
  }

  @Test
  void testUpdateGene() {
    // Setup
    final Gene gene =
        new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, "chromosomalLocation", "geneGroup", "geneId",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    final ResponseEntity<Gene> expectedResult =
        new ResponseEntity<>(new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false, "chromosomalLocation", "geneGroup",
            "geneId", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure GeneService.findGenesById(...).
    final Optional<Gene> gene1 =
        Optional.of(new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false, "chromosomalLocation", "geneGroup",
            "geneId", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockGeneService.findGenesById("id")).thenReturn(gene1);

    // Configure GeneService.updateGene(...).
    final Gene gene2 =
        new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, "chromosomalLocation", "geneGroup", "geneId",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    when(mockGeneService.updateGene(new Gene("approvedGeneName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false, "chromosomalLocation", "geneGroup", "geneId",
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), new Gene("approvedGeneName", new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        "chromosomalLocation", "geneGroup", "geneId", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))).thenReturn(gene2);

    // Run the test
    final ResponseEntity<Gene> result = geneControllerUnderTest.updateGene("id", gene);

    // Verify the results
    assertEquals(expectedResult, result);
  }
}
