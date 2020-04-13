package com.trends.db.controller;

import com.trends.db.model.ClinicalTrial;
import com.trends.db.model.enums.TrialStatus;
import com.trends.db.service.ClinicalTrialService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import static org.mockito.MockitoAnnotations.initMocks;

class ClinicalTrialControllerTest {

  @Mock private ClinicalTrialService mockClinicalTrialService;

  private ClinicalTrialController clinicalTrialControllerUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
    clinicalTrialControllerUnderTest = new ClinicalTrialController(mockClinicalTrialService);
  }

  @Test
  void testGetAllTrials() {
    // Setup

    // Configure ClinicalTrialService.findAllClinicalTrials(...).
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
    when(mockClinicalTrialService.findAllClinicalTrials()).thenReturn(clinicalTrials);

    // Run the test
    final List<ClinicalTrial> result = clinicalTrialControllerUnderTest.getAllTrials();

    // Verify the results
  }

  @Test
  void testGetTrials() {
    // Setup

    // Configure ClinicalTrialService.findClinicalTrialsByKeyword(...).
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
    when(mockClinicalTrialService.findClinicalTrialsByKeyword("keyword")).thenReturn(clinicalTrials);

    // Run the test
    final Set<ClinicalTrial> result = clinicalTrialControllerUnderTest.getTrials("keyword");

    // Verify the results
  }

  @Test
  void testGetTrial() {
    // Setup

    // Configure ClinicalTrialService.findClinicalTrialsById(...).
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
    when(mockClinicalTrialService.findClinicalTrialsById("id")).thenReturn(clinicalTrial);

    // Run the test
    final Optional<ClinicalTrial> result = clinicalTrialControllerUnderTest.getTrial("id");

    // Verify the results
  }


  @Test
  void testAddTrial() {
    // Setup
    final ClinicalTrial trial = new ClinicalTrial();
    trial.setId("id");
    trial.setPubMedId("pubMedId");
    trial.setTrialType("trialType");
    trial.setStatus(TrialStatus.IN_PROGRESS);
    trial.setKeywords(new HashSet<>(Arrays.asList("value")));
    trial.setLeadSponsors(new HashSet<>(Arrays.asList("value")));
    trial.setCitations(new HashSet<>(Arrays.asList("value")));
    trial.setCollaborators(new HashSet<>(Arrays.asList("value")));
    trial.setStopped(false);
    trial.setWhyStopped("whyStopped");

    // Run the test
    clinicalTrialControllerUnderTest.addTrial(trial);

    // Verify the results
    verify(mockClinicalTrialService).saveClinicalTrial(any(ClinicalTrial.class));
  }

  @Test
  void testUpdateTrial() {
    // Setup
    final ClinicalTrial trial = new ClinicalTrial();
    trial.setId("id");
    trial.setPubMedId("pubMedId");
    trial.setTrialType("trialType");
    trial.setStatus(TrialStatus.IN_PROGRESS);
    trial.setKeywords(new HashSet<>(Arrays.asList("value")));
    trial.setLeadSponsors(new HashSet<>(Arrays.asList("value")));
    trial.setCitations(new HashSet<>(Arrays.asList("value")));
    trial.setCollaborators(new HashSet<>(Arrays.asList("value")));
    trial.setStopped(false);
    trial.setWhyStopped("whyStopped");

    // Run the test
    clinicalTrialControllerUnderTest.updateTrial(0, trial);

    // Verify the results
    verify(mockClinicalTrialService).updateClinicalTrial(any(ClinicalTrial.class));
  }
}
