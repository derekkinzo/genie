package com.trends.db.controller;

import com.trends.db.model.Disease;
import com.trends.db.service.DiseaseService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.springframework.http.ResponseEntity;

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

    // Configure DiseaseService.findAllDiseases(...).
    final List<Disease> diseases =
        Arrays.asList(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockDiseaseService.findAllDiseases()).thenReturn(diseases);

    // Run the test
    final List<Disease> result = diseaseControllerUnderTest.getAllDiseases();

    // Verify the results
  }

  @Test
  void testGetDiseases() {
    // Setup

    // Configure DiseaseService.findDiseasesByKeyword(...).
    final Set<Disease> diseases = new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)));
    when(mockDiseaseService.findDiseasesByKeyword("keyword")).thenReturn(diseases);

    // Run the test
    final Set<Disease> result = diseaseControllerUnderTest.getDiseases("keyword");

    // Verify the results
  }

  @Test
  void testGetDiseaseById() {
    // Setup

    // Configure DiseaseService.findDiseasesById(...).
    final Optional<Disease> disease =
        Optional.of(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockDiseaseService.findDiseasesById("id")).thenReturn(disease);

    // Run the test
    final ResponseEntity result = diseaseControllerUnderTest.getDiseaseById("id");

    // Verify the results
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
    verify(mockDiseaseService).saveDisease(any(Disease.class));
  }

  @Test
  void testUpdateDisease() {
    // Setup
    final Disease disease = new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);

    // Run the test
    diseaseControllerUnderTest.updateDisease(0, disease);

    // Verify the results
    verify(mockDiseaseService).updateDisease(any(Disease.class));
  }
}
