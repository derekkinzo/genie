package com.trends.db.service.impl;

import com.trends.db.dao.GeneRepo;
import com.trends.db.model.Gene;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;

import java.util.Arrays;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;
import static org.mockito.MockitoAnnotations.initMocks;

class GeneServiceImplTest {

  @Mock private GeneRepo mockDao;

  @InjectMocks private GeneServiceImpl geneServiceImplUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
  }

  @Test
  void testFindGenesById() {
    // Setup

    // Configure GeneRepo.findById(...).
    final Gene gene1 = new Gene();
    gene1.setId("id");
    gene1.setApprovedGeneName("approvedGeneName");
    gene1.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene1.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene1.setAliases(new HashSet<>(Arrays.asList("value")));
    gene1.setSymbolStatus(false);
    gene1.setChromosomalLocation("chromosomalLocation");
    gene1.setGeneGroup("geneGroup");
    gene1.setGeneId("geneId");
    gene1.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Optional<Gene> gene = Optional.of(gene1);
    when(mockDao.findById("id")).thenReturn(gene);

    // Run the test
    final Optional<Gene> result = geneServiceImplUnderTest.findGenesById("id");

    // Verify the results
  }

  @Test
  void testFindGenesByKeyword() {
    // Setup

    // Configure GeneRepo.findGenesByKeywords(...).
    final Gene gene = new Gene();
    gene.setId("id");
    gene.setApprovedGeneName("approvedGeneName");
    gene.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene.setAliases(new HashSet<>(Arrays.asList("value")));
    gene.setSymbolStatus(false);
    gene.setChromosomalLocation("chromosomalLocation");
    gene.setGeneGroup("geneGroup");
    gene.setGeneId("geneId");
    gene.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Set<Gene> genes = new HashSet<>(Arrays.asList(gene));
    when(mockDao.findGenesByKeywords("keyword")).thenReturn(genes);

    // Run the test
    final Set<Gene> result = geneServiceImplUnderTest.findGenesByKeyword("keyword");

    // Verify the results
  }

  @Test
  void testFindAllGenes() {
    // Setup

    // Configure GeneRepo.findAll(...).
    final Gene gene = new Gene();
    gene.setId("id");
    gene.setApprovedGeneName("approvedGeneName");
    gene.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene.setAliases(new HashSet<>(Arrays.asList("value")));
    gene.setSymbolStatus(false);
    gene.setChromosomalLocation("chromosomalLocation");
    gene.setGeneGroup("geneGroup");
    gene.setGeneId("geneId");
    gene.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final List<Gene> genes = Arrays.asList(gene);
    when(mockDao.findAll()).thenReturn(genes);

    // Run the test
    final List<Gene> result = geneServiceImplUnderTest.findAllGenes();

    // Verify the results
  }

  @Test
  void testSaveGenes() {
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
    gene.setGeneId("geneId");
    gene.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Set<Gene> genes = new HashSet<>(Arrays.asList(gene));

    // Configure GeneRepo.insert(...).
    final Gene gene1 = new Gene();
    gene1.setId("id");
    gene1.setApprovedGeneName("approvedGeneName");
    gene1.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene1.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene1.setAliases(new HashSet<>(Arrays.asList("value")));
    gene1.setSymbolStatus(false);
    gene1.setChromosomalLocation("chromosomalLocation");
    gene1.setGeneGroup("geneGroup");
    gene1.setGeneId("geneId");
    gene1.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final List<Gene> genes1 = Arrays.asList(gene1);
    when(mockDao.insert(Arrays.asList())).thenReturn(genes1);

    // Run the test
    geneServiceImplUnderTest.saveGenes(genes);

    // Verify the results
  }

  @Test
  void testSaveGene() {
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
    gene.setGeneId("geneId");
    gene.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());

    // Configure GeneRepo.insert(...).
    final Gene gene1 = new Gene();
    gene1.setId("id");
    gene1.setApprovedGeneName("approvedGeneName");
    gene1.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene1.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene1.setAliases(new HashSet<>(Arrays.asList("value")));
    gene1.setSymbolStatus(false);
    gene1.setChromosomalLocation("chromosomalLocation");
    gene1.setGeneGroup("geneGroup");
    gene1.setGeneId("geneId");
    gene1.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    when(mockDao.insert(any(Gene.class))).thenReturn(gene1);

    // Run the test
    geneServiceImplUnderTest.saveGene(gene);

    // Verify the results
  }

  @Test
  void testUpdateGene() {
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
    gene.setGeneId("geneId");
    gene.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());

    // Configure GeneRepo.insert(...).
    final Gene gene1 = new Gene();
    gene1.setId("id");
    gene1.setApprovedGeneName("approvedGeneName");
    gene1.setApprovedSymbols(new HashSet<>(Arrays.asList("value")));
    gene1.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene1.setAliases(new HashSet<>(Arrays.asList("value")));
    gene1.setSymbolStatus(false);
    gene1.setChromosomalLocation("chromosomalLocation");
    gene1.setGeneGroup("geneGroup");
    gene1.setGeneId("geneId");
    gene1.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    when(mockDao.insert(any(Gene.class))).thenReturn(gene1);

    // Run the test
    geneServiceImplUnderTest.updateGene(gene);

    // Verify the results
  }
}
