package com.trends.db.controller;

import com.trends.db.model.ClinicalTrial;
import com.trends.db.model.enums.TrialOutcome;
import com.trends.db.model.enums.TrialStatus;
import com.trends.db.service.ClinicalTrialService;
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
    final ResponseEntity<List<ClinicalTrial>> expectedResult = new ResponseEntity<>(
        Arrays.asList(
            new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                false, "whyStopped", false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)), HttpStatus.OK);

    // Configure ClinicalTrialService.findAllClinicalTrials(...).
    final List<ClinicalTrial> clinicalTrials =
        Arrays.asList(new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, "whyStopped", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockClinicalTrialService.findAllClinicalTrials()).thenReturn(clinicalTrials);

    // Run the test
    final ResponseEntity<List<ClinicalTrial>> result = clinicalTrialControllerUnderTest.getAllTrials();

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetTrialsByKeyword() {
    // Setup
    final ResponseEntity<Set<ClinicalTrial>> expectedResult = new ResponseEntity<>(new HashSet<>(
        Arrays.asList(
            new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                false, "whyStopped", false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), HttpStatus.OK);

    // Configure ClinicalTrialService.findClinicalTrialsByKeyword(...).
    final Set<ClinicalTrial> trials = new HashSet<>(
        Arrays.asList(
            new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                false, "whyStopped", false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)));
    when(mockClinicalTrialService.findClinicalTrialsByKeyword("keyword")).thenReturn(trials);

    // Run the test
    final ResponseEntity<Set<ClinicalTrial>> result = clinicalTrialControllerUnderTest.getTrialsByKeyword("keyword");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetTrialById() {
    // Setup
    final ResponseEntity<ClinicalTrial> expectedResult =
        new ResponseEntity<>(new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, "whyStopped", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure ClinicalTrialService.findClinicalTrialsById(...).
    final Optional<ClinicalTrial> clinicalTrial =
        Optional.of(new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, "whyStopped", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockClinicalTrialService.findClinicalTrialsById("id")).thenReturn(clinicalTrial);

    // Run the test
    final ResponseEntity<ClinicalTrial> result = clinicalTrialControllerUnderTest.getTrialById("id");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testAddTrial() {
    // Setup
    final ClinicalTrial trial = new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), false, "whyStopped", false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        TrialOutcome.FAILED, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);

    // Run the test
    clinicalTrialControllerUnderTest.addTrial(trial);

    // Verify the results
    verify(mockClinicalTrialService)
        .saveClinicalTrial(new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, "whyStopped", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
  }

  @Test
  void testUpdateTrial() {
    // Setup
    final ClinicalTrial trial = new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), false, "whyStopped", false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        TrialOutcome.FAILED, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    final ResponseEntity<ClinicalTrial> expectedResult =
        new ResponseEntity<>(new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, "whyStopped", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure ClinicalTrialService.findClinicalTrialsById(...).
    final Optional<ClinicalTrial> clinicalTrial =
        Optional.of(new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, "whyStopped", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockClinicalTrialService.findClinicalTrialsById("id")).thenReturn(clinicalTrial);

    // Configure ClinicalTrialService.updateClinicalTrial(...).
    final ClinicalTrial clinicalTrial1 = new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), false, "whyStopped", false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        TrialOutcome.FAILED, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    when(mockClinicalTrialService
        .updateClinicalTrial(new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, "whyStopped", false,
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0),
            new ClinicalTrial("pubMedId", "trialType", TrialStatus.IN_PROGRESS, new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, "whyStopped", false,
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), TrialOutcome.FAILED,
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))).thenReturn(clinicalTrial1);

    // Run the test
    final ResponseEntity<ClinicalTrial> result = clinicalTrialControllerUnderTest.updateTrial("id", trial);

    // Verify the results
    assertEquals(expectedResult, result);
  }
}
