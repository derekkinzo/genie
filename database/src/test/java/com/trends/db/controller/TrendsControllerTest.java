package com.trends.db.controller;

import com.trends.db.model.Disease;
import com.trends.db.model.Trend;
import com.trends.db.service.TrendsService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;

import java.util.Arrays;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.HashSet;
import java.util.Optional;
import java.util.Set;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import static org.mockito.MockitoAnnotations.initMocks;

class TrendsControllerTest {

  @Mock private TrendsService mockTrendsService;

  private TrendsController trendsControllerUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
    trendsControllerUnderTest = new TrendsController(mockTrendsService);
  }

  @Test
  void testGetTrends() {
    // Setup

    // Configure TrendsService.findTrendsByKeyword(...).
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
    when(mockTrendsService.findTrendsByKeyword("keyword")).thenReturn(trends);

    // Run the test
    final Set<Trend> result = trendsControllerUnderTest.getTrends("keyword");

    // Verify the results
  }

  @Test
  void testGetTrend() {
    // Setup

    // Configure TrendsService.findTrendsById(...).
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
    when(mockTrendsService.findTrendsById("id")).thenReturn(trend);

    // Run the test
    final Optional<Trend> result = trendsControllerUnderTest.getTrend("id");

    // Verify the results
  }


  @Test
  void testAddTrend() {
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

    // Run the test
    trendsControllerUnderTest.addTrend(trend);

    // Verify the results
    verify(mockTrendsService).saveTrend(any(Trend.class));
  }

  @Test
  void testUpdateTrends() {
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

    // Run the test
    trendsControllerUnderTest.updateTrends(0, trend);

    // Verify the results
    verify(mockTrendsService).updateTrend(any(Trend.class));
  }
}
