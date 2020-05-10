package com.trends.db.controller;

import com.trends.db.model.Disease;
import com.trends.db.model.Trend;
import com.trends.db.service.TrendsService;
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
    final ResponseEntity<List<Trend>> expectedResult = new ResponseEntity<>(
        Arrays.asList(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)), HttpStatus.OK);

    // Configure TrendsService.findAllTrends(...).
    final List<Trend> trends =
        Arrays.asList(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockTrendsService.findAllTrends()).thenReturn(trends);

    // Run the test
    final ResponseEntity<List<Trend>> result = trendsControllerUnderTest.getTrends();

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetTrendsByKeyword() {
    // Setup
    final ResponseEntity<Set<Trend>> expectedResult = new ResponseEntity<>(new HashSet<>(
        Arrays.asList(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), HttpStatus.OK);

    // Configure TrendsService.findTrendsByKeyword(...).
    final Set<Trend> trends = new HashSet<>(
        Arrays.asList(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)));
    when(mockTrendsService.findTrendsByKeyword("keyword")).thenReturn(trends);

    // Run the test
    final ResponseEntity<Set<Trend>> result = trendsControllerUnderTest.getTrendsByKeyword("keyword");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetTrendById() {
    // Setup
    final ResponseEntity<Trend> expectedResult =
        new ResponseEntity<>(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure TrendsService.findTrendsById(...).
    final Optional<Trend> trend =
        Optional.of(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockTrendsService.findTrendsById("id")).thenReturn(trend);

    // Run the test
    final ResponseEntity<Trend> result = trendsControllerUnderTest.getTrendById("id");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testAddTrend() {
    // Setup
    final Trend trend =
        new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);

    // Run the test
    trendsControllerUnderTest.addTrend(trend);

    // Verify the results
    verify(mockTrendsService)
        .saveTrend(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
  }

  @Test
  void testUpdateTrends() {
    // Setup
    final Trend trend =
        new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    final ResponseEntity<Trend> expectedResult =
        new ResponseEntity<>(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure TrendsService.findTrendsById(...).
    final Optional<Trend> trend1 =
        Optional.of(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockTrendsService.findTrendsById("id")).thenReturn(trend1);

    // Configure TrendsService.updateTrend(...).
    final Trend trend2 =
        new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    when(mockTrendsService
        .updateTrend(new Trend(new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), new Trend(new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList(
                new Disease("diseaseName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
                    new HashSet<>(
                        Arrays.asList("value")), false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
                    new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), 0L, "chromosomalLocation",
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))).thenReturn(trend2);

    // Run the test
    final ResponseEntity<Trend> result = trendsControllerUnderTest.updateTrends("id", trend);

    // Verify the results
    assertEquals(expectedResult, result);
  }
}
