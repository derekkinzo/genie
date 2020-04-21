package com.trends.db.controller;

import com.trends.db.model.Patent;
import com.trends.db.service.PatentService;
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

class PatentControllerTest {

  @Mock private PatentService mockPatentService;

  private PatentController patentControllerUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
    patentControllerUnderTest = new PatentController(mockPatentService);
  }

  @Test
  void testGetPatents() {
    // Setup
    final ResponseEntity<List<Patent>> expectedResult = new ResponseEntity<>(
        Arrays.asList(new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), "patent", "patentNumber", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)), HttpStatus.OK);

    // Configure PatentService.findAllPatents(...).
    final List<Patent> patents = Arrays.asList(new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), "patent", "patentNumber", false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockPatentService.findAllPatents()).thenReturn(patents);

    // Run the test
    final ResponseEntity<List<Patent>> result = patentControllerUnderTest.getPatents();

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetPatentsByKeyword() {
    // Setup
    final ResponseEntity<Set<Patent>> expectedResult = new ResponseEntity<>(new HashSet<>(
        Arrays.asList(new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), "patent", "patentNumber", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), HttpStatus.OK);

    // Configure PatentService.findPatentsByKeyword(...).
    final Set<Patent> patents = new HashSet<>(
        Arrays.asList(new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new HashSet<>(
                Arrays.asList("value")), "patent", "patentNumber", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)));
    when(mockPatentService.findPatentsByKeyword("keyword")).thenReturn(patents);

    // Run the test
    final ResponseEntity<Set<Patent>> result = patentControllerUnderTest.getPatentsByKeyword("keyword");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetPatentById() {
    // Setup
    final ResponseEntity<Patent> expectedResult = new ResponseEntity<>(new Patent("drugName", new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), "patent",
        "patentNumber", false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure PatentService.findPatentsById(...).
    final Optional<Patent> patent = Optional.of(new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), "patent", "patentNumber", false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockPatentService.findPatentsById("id")).thenReturn(patent);

    // Run the test
    final ResponseEntity<Patent> result = patentControllerUnderTest.getPatentById("id");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testAddPatent() {
    // Setup
    final Patent patent =
        new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), "patent", "patentNumber", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);

    // Run the test
    patentControllerUnderTest.addPatent(patent);

    // Verify the results
    verify(mockPatentService).savePatent(new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), "patent", "patentNumber", false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
  }

  @Test
  void testUpdatePatents() {
    // Setup
    final Patent patent =
        new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), "patent", "patentNumber", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    final ResponseEntity<Patent> expectedResult =
        new ResponseEntity<>(new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), "patent", "patentNumber", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure PatentService.findPatentsById(...).
    final Optional<Patent> patent1 = Optional.of(new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), "patent", "patentNumber", false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockPatentService.findPatentsById("id")).thenReturn(patent1);

    // Configure PatentService.updatePatent(...).
    final Patent patent2 =
        new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), "patent", "patentNumber", false,
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    when(mockPatentService.updatePatent(new Patent("drugName", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), "patent", "patentNumber", false,
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), new Patent("drugName", new HashSet<>(
        Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), new HashSet<>(Arrays.asList("value")), "patent",
        "patentNumber", false, new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))).thenReturn(patent2);

    // Run the test
    final ResponseEntity<Patent> result = patentControllerUnderTest.updatePatents("id", patent);

    // Verify the results
    assertEquals(expectedResult, result);
  }
}
