package com.trends.db.service.impl;

import com.trends.db.dao.ClinicalTrialRepo;
import com.trends.db.model.ClinicalTrial;
import com.trends.db.model.enums.TrialStatus;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;
import static org.mockito.MockitoAnnotations.initMocks;

class ClinicalTrialServiceImplTest {

  @Mock private ClinicalTrialRepo mockDao;

  @InjectMocks private ClinicalTrialServiceImpl clinicalTrialServiceImplUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
  }

  @Test
  void testFindClinicalTrialsById() {
    // Setup

    // Configure ClinicalTrialRepo.findById(...).
    final ClinicalTrial clinicalTrial1 = new ClinicalTrial();
    clinicalTrial1.setId("id");
    clinicalTrial1.setPubMedId("pubMedId");
    clinicalTrial1.setTrialType("trialType");
    clinicalTrial1.setStatus(TrialStatus.IN_PROGRESS);
    clinicalTrial1.setKeywords(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setLeadSponsors(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setCitations(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setCollaborators(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setStopped(false);
    clinicalTrial1.setWhyStopped("whyStopped");
    final Optional<ClinicalTrial> clinicalTrial = Optional.of(clinicalTrial1);
    when(mockDao.findById("id")).thenReturn(clinicalTrial);

    // Run the test
    final Optional<ClinicalTrial> result = clinicalTrialServiceImplUnderTest.findClinicalTrialsById("id");

    // Verify the results
  }

  @Test
  void testFindClinicalTrialsByKeyword() {
    // Setup

    // Configure ClinicalTrialRepo.findClinicalTrialsByKeywords(...).
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
    final Set<ClinicalTrial> clinicalTrials = new HashSet<>(Arrays.asList(clinicalTrial));
    when(mockDao.findClinicalTrialsByKeywords("keyword")).thenReturn(clinicalTrials);

    // Run the test
    final Set<ClinicalTrial> result = clinicalTrialServiceImplUnderTest.findClinicalTrialsByKeyword("keyword");

    // Verify the results
  }

  @Test
  void testFindAllClinicalTrials() {
    // Setup

    // Configure ClinicalTrialRepo.findAll(...).
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
    final List<ClinicalTrial> clinicalTrials = Arrays.asList(clinicalTrial);
    when(mockDao.findAll()).thenReturn(clinicalTrials);

    // Run the test
    final List<ClinicalTrial> result = clinicalTrialServiceImplUnderTest.findAllClinicalTrials();

    // Verify the results
  }

  @Test
  void testSaveClinicalTrials() {
    // Setup
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
    final Set<ClinicalTrial> clinicalTrials = new HashSet<>(Arrays.asList(clinicalTrial));

    // Configure ClinicalTrialRepo.insert(...).
    final ClinicalTrial clinicalTrial1 = new ClinicalTrial();
    clinicalTrial1.setId("id");
    clinicalTrial1.setPubMedId("pubMedId");
    clinicalTrial1.setTrialType("trialType");
    clinicalTrial1.setStatus(TrialStatus.IN_PROGRESS);
    clinicalTrial1.setKeywords(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setLeadSponsors(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setCitations(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setCollaborators(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setStopped(false);
    clinicalTrial1.setWhyStopped("whyStopped");
    final List<ClinicalTrial> clinicalTrials1 = Arrays.asList(clinicalTrial1);
    when(mockDao.insert(Arrays.asList())).thenReturn(clinicalTrials1);

    // Run the test
    clinicalTrialServiceImplUnderTest.saveClinicalTrials(clinicalTrials);

    // Verify the results
  }

  @Test
  void testSaveClinicalTrial() {
    // Setup
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

    // Configure ClinicalTrialRepo.insert(...).
    final ClinicalTrial clinicalTrial1 = new ClinicalTrial();
    clinicalTrial1.setId("id");
    clinicalTrial1.setPubMedId("pubMedId");
    clinicalTrial1.setTrialType("trialType");
    clinicalTrial1.setStatus(TrialStatus.IN_PROGRESS);
    clinicalTrial1.setKeywords(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setLeadSponsors(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setCitations(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setCollaborators(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setStopped(false);
    clinicalTrial1.setWhyStopped("whyStopped");
    when(mockDao.insert(any(ClinicalTrial.class))).thenReturn(clinicalTrial1);

    // Run the test
    clinicalTrialServiceImplUnderTest.saveClinicalTrial(clinicalTrial);

    // Verify the results
  }

  @Test
  void testUpdateClinicalTrial() {
    // Setup
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

    // Configure ClinicalTrialRepo.insert(...).
    final ClinicalTrial clinicalTrial1 = new ClinicalTrial();
    clinicalTrial1.setId("id");
    clinicalTrial1.setPubMedId("pubMedId");
    clinicalTrial1.setTrialType("trialType");
    clinicalTrial1.setStatus(TrialStatus.IN_PROGRESS);
    clinicalTrial1.setKeywords(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setLeadSponsors(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setCitations(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setCollaborators(new HashSet<>(Arrays.asList("value")));
    clinicalTrial1.setStopped(false);
    clinicalTrial1.setWhyStopped("whyStopped");
    when(mockDao.insert(any(ClinicalTrial.class))).thenReturn(clinicalTrial1);

    // Run the test
    clinicalTrialServiceImplUnderTest.updateClinicalTrial(clinicalTrial);

    // Verify the results
  }
}
