package com.trends.db.service.impl;

import com.trends.db.dao.TrendRepo;
import com.trends.db.model.Disease;
import com.trends.db.model.Trend;
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

class TrendsServiceImplTest {

  @Mock private TrendRepo mockDao;

  @InjectMocks private TrendsServiceImpl trendsServiceImplUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
  }

  @Test
  void testFindTrendsById() {
    // Setup

    // Configure TrendRepo.findById(...).
    final Trend trend1 = new Trend();
    trend1.setId("id");
    trend1.setKeywords(new HashSet<>(Arrays.asList("value")));
    trend1.setGeneSymbols(new HashSet<>(Arrays.asList("value")));
    trend1.setAssociatedDiseases(new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))));
    trend1.setTotalAssociations(0L);
    trend1.setChromosomalLocation("chromosomalLocation");
    trend1.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend1.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend1.setVersion(0);
    final Optional<Trend> trend = Optional.of(trend1);
    when(mockDao.findById("id")).thenReturn(trend);

    // Run the test
    final Optional<Trend> result = trendsServiceImplUnderTest.findTrendsById("id");

    // Verify the results
  }

  @Test
  void testFindTrendsByKeyword() {
    // Setup

    // Configure TrendRepo.findTrendsByKeywords(...).
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
    final Set<Trend> trends = new HashSet<>(Arrays.asList(trend));
    when(mockDao.findTrendsByKeywords("keyword")).thenReturn(trends);

    // Run the test
    final Set<Trend> result = trendsServiceImplUnderTest.findTrendsByKeyword("keyword");

    // Verify the results
  }

  @Test
  void testFindAllTrends() {
    // Setup

    // Configure TrendRepo.findAll(...).
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
    final List<Trend> trends = Arrays.asList(trend);
    when(mockDao.findAll()).thenReturn(trends);

    // Run the test
    final List<Trend> result = trendsServiceImplUnderTest.findAllTrends();

    // Verify the results
  }

  @Test
  void testSaveTrends() {
    // Setup
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
    final Set<Trend> trends = new HashSet<>(Arrays.asList(trend));

    // Configure TrendRepo.insert(...).
    final Trend trend1 = new Trend();
    trend1.setId("id");
    trend1.setKeywords(new HashSet<>(Arrays.asList("value")));
    trend1.setGeneSymbols(new HashSet<>(Arrays.asList("value")));
    trend1.setAssociatedDiseases(new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))));
    trend1.setTotalAssociations(0L);
    trend1.setChromosomalLocation("chromosomalLocation");
    trend1.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend1.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend1.setVersion(0);
    final List<Trend> trends1 = Arrays.asList(trend1);
    when(mockDao.insert(Arrays.asList())).thenReturn(trends1);

    // Run the test
    trendsServiceImplUnderTest.saveTrends(trends);

    // Verify the results
  }

  @Test
  void testSaveTrend() {
    // Setup
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

    // Configure TrendRepo.insert(...).
    final Trend trend1 = new Trend();
    trend1.setId("id");
    trend1.setKeywords(new HashSet<>(Arrays.asList("value")));
    trend1.setGeneSymbols(new HashSet<>(Arrays.asList("value")));
    trend1.setAssociatedDiseases(new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))));
    trend1.setTotalAssociations(0L);
    trend1.setChromosomalLocation("chromosomalLocation");
    trend1.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend1.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend1.setVersion(0);
    when(mockDao.insert(any(Trend.class))).thenReturn(trend1);

    // Run the test
    trendsServiceImplUnderTest.saveTrend(trend);

    // Verify the results
  }

  @Test
  void testUpdateTrend() {
    // Setup
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

    // Configure TrendRepo.insert(...).
    final Trend trend1 = new Trend();
    trend1.setId("id");
    trend1.setKeywords(new HashSet<>(Arrays.asList("value")));
    trend1.setGeneSymbols(new HashSet<>(Arrays.asList("value")));
    trend1.setAssociatedDiseases(new HashSet<>(
        Arrays.asList(
            new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                new HashSet<>(
                    Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))));
    trend1.setTotalAssociations(0L);
    trend1.setChromosomalLocation("chromosomalLocation");
    trend1.setCreatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend1.setUpdatedOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    trend1.setVersion(0);
    when(mockDao.insert(any(Trend.class))).thenReturn(trend1);

    // Run the test
    trendsServiceImplUnderTest.updateTrend(trend);

    // Verify the results
  }
}
