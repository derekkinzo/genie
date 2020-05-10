package com.trends.db.controller;

import com.trends.db.model.Disease;
import com.trends.db.service.DiseaseService;
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

class DiseaseControllerTest {

  @Mock private DiseaseService mockDiseaseService;

  private DiseaseController diseaseControllerUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
    diseaseControllerUnderTest = new DiseaseController(mockDiseaseService);
  }

  @Test
  void testGetAllDiseases() {
    // Setup
    final ResponseEntity<List<Disease>> expectedResult = new ResponseEntity<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)), HttpStatus.OK);

    // Configure DiseaseService.findAllDiseases(...).
    final List<Disease> diseases =
        Arrays.asList(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockDiseaseService.findAllDiseases()).thenReturn(diseases);

    // Run the test
    final ResponseEntity<List<Disease>> result = diseaseControllerUnderTest.getAllDiseases();

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetDiseases() {
    // Setup
    final ResponseEntity<Set<Disease>> expectedResult = new ResponseEntity<>(new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), HttpStatus.OK);

    // Configure DiseaseService.findDiseasesByKeyword(...).
    final Set<Disease> diseases = new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)));
    when(mockDiseaseService.findDiseasesByKeyword("keyword")).thenReturn(diseases);

    // Run the test
    final ResponseEntity<Set<Disease>> result = diseaseControllerUnderTest.getDiseases("keyword");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetDiseaseById() {
    // Setup
    final ResponseEntity<Disease> expectedResult = new ResponseEntity<>(new Disease("diseaseName", new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure DiseaseService.findDiseaseById(...).
    final Optional<Disease> disease =
        Optional.of(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockDiseaseService.findDiseaseById("id")).thenReturn(disease);

    // Run the test
    final ResponseEntity<Disease> result = diseaseControllerUnderTest.getDiseaseById("id");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testAddDisease() {
    // Setup
    final Disease disease = new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);

    // Run the test
    diseaseControllerUnderTest.addDisease(disease);

    // Verify the results
    verify(mockDiseaseService).saveDisease(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
  }

  @Test
  void testUpdateDisease() {
    // Setup
    final Disease disease = new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    final ResponseEntity<Disease> expectedResult =
        new ResponseEntity<>(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure DiseaseService.findDiseaseById(...).
    final Optional<Disease> disease1 =
        Optional.of(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockDiseaseService.findDiseaseById("id")).thenReturn(disease1);

    // Configure DiseaseService.updateDisease(...).
    final Disease disease2 =
        new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    when(mockDiseaseService.updateDisease(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), new Disease("diseaseName", new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))).thenReturn(disease2);

    // Run the test
    final ResponseEntity<Disease> result = diseaseControllerUnderTest.updateDisease("id", disease);

    // Verify the results
    assertEquals(expectedResult, result);
  }
}
