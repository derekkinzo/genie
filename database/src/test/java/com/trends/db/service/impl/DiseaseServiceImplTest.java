package com.trends.db.service.impl;

import com.trends.db.dao.DiseaseRepo;
import com.trends.db.model.Disease;
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

class DiseaseServiceImplTest {

  @Mock private DiseaseRepo mockDao;

  @InjectMocks private DiseaseServiceImpl diseaseServiceImplUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
  }

  @Test
  void testFindDiseasesById() {
    // Setup

    // Configure DiseaseRepo.findById(...).
    final Optional<Disease> disease =
        Optional.of(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockDao.findById("id")).thenReturn(disease);

    // Run the test
    final Optional<Disease> result = diseaseServiceImplUnderTest.findDiseasesById("id");

    // Verify the results
  }

  @Test
  void testFindDiseasesByKeyword() {
    // Setup

    // Configure DiseaseRepo.findDiseasesByKeywords(...).
    final Set<Disease> diseases = new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)));
    when(mockDao.findDiseasesByKeywords("keyword")).thenReturn(diseases);

    // Run the test
    final Set<Disease> result = diseaseServiceImplUnderTest.findDiseasesByKeyword("keyword");

    // Verify the results
  }

  @Test
  void testFindAllDiseases() {
    // Setup

    // Configure DiseaseRepo.findAll(...).
    final List<Disease> diseases =
        Arrays.asList(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockDao.findAll()).thenReturn(diseases);

    // Run the test
    final List<Disease> result = diseaseServiceImplUnderTest.findAllDiseases();

    // Verify the results
  }

  @Test
  void testSaveDiseases() {
    // Setup
    final Set<Disease> diseases = new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)));

    // Configure DiseaseRepo.insert(...).
    final List<Disease> diseases1 =
        Arrays.asList(new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockDao.insert(Arrays.asList())).thenReturn(diseases1);

    // Run the test
    diseaseServiceImplUnderTest.saveDiseases(diseases);

    // Verify the results
  }

  @Test
  void testSaveDisease() {
    // Setup
    final Disease disease = new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);

    // Configure DiseaseRepo.insert(...).
    final Disease disease1 =
        new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    when(mockDao.insert(any(Disease.class))).thenReturn(disease1);

    // Run the test
    diseaseServiceImplUnderTest.saveDisease(disease);

    // Verify the results
  }

  @Test
  void testUpdateDisease() {
    // Setup
    final Disease disease = new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);

    // Configure DiseaseRepo.insert(...).
    final Disease disease1 =
        new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    when(mockDao.insert(any(Disease.class))).thenReturn(disease1);

    // Run the test
    diseaseServiceImplUnderTest.updateDisease(disease);

    // Verify the results
  }
}
