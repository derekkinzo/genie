package com.trends.db;

import com.trends.db.config.TrendsDBConfig;
import com.trends.db.dao.ClinicalTrialRepo;
import com.trends.db.dao.DiseaseRepo;
import com.trends.db.dao.GeneRepo;
import com.trends.db.dao.PatentRepo;
import com.trends.db.dao.PublicationRepo;
import com.trends.db.dao.TrendRepo;
import com.trends.db.model.ClinicalTrial;
import com.trends.db.model.Disease;
import com.trends.db.model.Gene;
import com.trends.db.model.Patent;
import com.trends.db.model.Publication;
import com.trends.db.model.Trend;
import com.trends.db.model.enums.TrialStatus;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import springfox.documentation.spring.web.plugins.Docket;

import java.util.Arrays;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.HashSet;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;
import static org.mockito.MockitoAnnotations.initMocks;

class TrendsDBApplicationTest {

  @Mock private TrendRepo mockTrendRepo;
  @Mock private DiseaseRepo mockDiseaseRepo;
  @Mock private GeneRepo mockGeneRepo;
  @Mock private PatentRepo mockPatentRepo;
  @Mock private PublicationRepo mockPublicationRepo;
  @Mock private ClinicalTrialRepo mockClinicalTrialRepo;
  @Mock private TrendsDBConfig mockTrendsDBConfig;

  @InjectMocks private TrendsDBApplication trendsDBApplicationUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
  }

  @Test
  void testTrendsApi() {
    // Setup

    // Run the test
    final Docket result = trendsDBApplicationUnderTest.trendsApi();

    // Verify the results
  }

  @Test
  void testRun() {
    // Setup

    // Configure DiseaseRepo.insert(...).
    final Disease disease =
        new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    when(mockDiseaseRepo.insert(any(Disease.class))).thenReturn(disease);

    // Configure GeneRepo.save(...).
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
    when(mockGeneRepo.save(any(Gene.class))).thenReturn(gene);

    // Configure PatentRepo.save(...).
    final Patent patent = new Patent();
    patent.setId("id");
    patent.setDrugName("drugName");
    patent.setKeywords(new HashSet<>(Arrays.asList("value")));
    patent.setAliases(new HashSet<>(Arrays.asList("value")));
    patent.setParticipants(new HashSet<>(Arrays.asList("value")));
    patent.setPatent("patent");
    patent.setPatentNumber("patentNumber");
    patent.setActive(false);
    patent.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    patent.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    when(mockPatentRepo.save(any(Patent.class))).thenReturn(patent);

    // Configure PublicationRepo.save(...).
    final Publication publication = new Publication();
    publication.setId("id");
    publication.setAbstractTitle("abstractTitle");
    publication.setKeywords(new HashSet<>(Arrays.asList("value")));
    publication.setSourceUri("sourceUri");
    publication.setAbstractContent("abstractContent");
    publication.setChemicals(new HashSet<>(Arrays.asList("value")));
    publication.setAuthors(new HashSet<>(Arrays.asList("value")));
    publication.setDateAccepted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication.setDateCompleted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication.setDateEntered(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    when(mockPublicationRepo.save(any(Publication.class))).thenReturn(publication);

    // Configure ClinicalTrialRepo.save(...).
    final ClinicalTrial clinicalTrial = new ClinicalTrial();
    clinicalTrial.setId("id");
    clinicalTrial.setPubMedId("pubMedId");
    clinicalTrial.setTrialType("trialType");
    clinicalTrial.setStatus(TrialStatus.IN_PROGRESS);
    clinicalTrial.setKeywords(new HashSet<>(Arrays.asList("value")));
    clinicalTrial.setLeadSponsors(new HashSet<>(Arrays.asList("value")));
    clinicalTrial.setCitations(new HashSet<>(Arrays.asList("value")));
    clinicalTrial.setCollaborators(new HashSet<>(Arrays.asList("value")));
    clinicalTrial.setStopped(false);
    clinicalTrial.setWhyStopped("whyStopped");
    when(mockClinicalTrialRepo.save(any(ClinicalTrial.class))).thenReturn(clinicalTrial);

    // Configure TrendRepo.save(...).
    final Trend trend = new Trend();
    trend.setId("id");
    trend.setKeywords(new HashSet<>(Arrays.asList("value")));
    trend.setGeneSymbols(new HashSet<>(Arrays.asList("value")));
    trend.setAssociatedDiseases(new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))));
    trend.setTotalAssociations(0L);
    trend.setChromosomalLocation("chromosomalLocation");
    trend.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend.setVersion(0);
    when(mockTrendRepo.save(any(Trend.class))).thenReturn(trend);

    // Run the test
    trendsDBApplicationUnderTest.run("args");

    // Verify the results
  }

  @Test
  void testMain() {
    // Setup

    // Run the test
    TrendsDBApplication.main(new String[] { "value" });

    // Verify the results
  }
}
