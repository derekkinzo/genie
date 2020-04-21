package com.trends.db.controller;

import com.trends.db.model.Publication;
import com.trends.db.service.PublicationService;
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

class PublicationControllerTest {

  @Mock private PublicationService mockPublicationService;

  private PublicationController publicationControllerUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
    publicationControllerUnderTest = new PublicationController(mockPublicationService);
  }

  @Test
  void testGetPublications() {
    // Setup
    final ResponseEntity<List<Publication>> expectedResult = new ResponseEntity<>(
        Arrays.asList(new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)), HttpStatus.OK);

    // Configure PublicationService.findAllPublications(...).
    final List<Publication> publications = Arrays.asList(
        new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockPublicationService.findAllPublications()).thenReturn(publications);

    // Run the test
    final ResponseEntity<List<Publication>> result = publicationControllerUnderTest.getPublications();

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetPublicationsByKeyword() {
    // Setup
    final ResponseEntity<Set<Publication>> expectedResult = new ResponseEntity<>(new HashSet<>(
        Arrays.asList(new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))), HttpStatus.OK);

    // Configure PublicationService.findPublicationsByKeyword(...).
    final Set<Publication> publications = new HashSet<>(
        Arrays.asList(new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0)));
    when(mockPublicationService.findPublicationsByKeyword("keyword")).thenReturn(publications);

    // Run the test
    final ResponseEntity<Set<Publication>> result = publicationControllerUnderTest.getPublicationsByKeyword("keyword");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testGetPublicationById() {
    // Setup
    final ResponseEntity<Publication> expectedResult = new ResponseEntity<>(new Publication("abstractTitle", new HashSet<>(
        Arrays.asList("value")), "sourceUri", "abstractContent", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
        "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure PublicationService.findPublicationsById(...).
    final Optional<Publication> publication = Optional
        .of(new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockPublicationService.findPublicationsById("id")).thenReturn(publication);

    // Run the test
    final ResponseEntity<Publication> result = publicationControllerUnderTest.getPublicationById("id");

    // Verify the results
    assertEquals(expectedResult, result);
  }

  @Test
  void testAddPublication() {
    // Setup
    final Publication publication =
        new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);

    // Run the test
    publicationControllerUnderTest.addPublication(publication);

    // Verify the results
    verify(mockPublicationService).savePublication(
        new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
  }

  @Test
  void testUpdatePublications() {
    // Setup
    final Publication publication =
        new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    final ResponseEntity<Publication> expectedResult = new ResponseEntity<>(new Publication("abstractTitle", new HashSet<>(
        Arrays.asList("value")), "sourceUri", "abstractContent", new HashSet<>(Arrays.asList("value")), new HashSet<>(
        Arrays.asList("value")), new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
        "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
        new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), HttpStatus.OK);

    // Configure PublicationService.findPublicationsById(...).
    final Optional<Publication> publication1 = Optional
        .of(new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0));
    when(mockPublicationService.findPublicationsById("id")).thenReturn(publication1);

    // Configure PublicationService.updatePublication(...).
    final Publication publication2 =
        new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0);
    when(mockPublicationService.updatePublication(
        new Publication("abstractTitle", new HashSet<>(Arrays.asList("value")), "sourceUri", "abstractContent",
            new HashSet<>(
                Arrays.asList("value")), new HashSet<>(Arrays.asList("value")),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0), new Publication("abstractTitle", new HashSet<>(
            Arrays.asList("value")), "sourceUri", "abstractContent", new HashSet<>(Arrays.asList("value")), new HashSet<>(
            Arrays.asList("value")), new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), "doiId", "language", "piiId", "pmcId", "pmiId",
            "publishStatus", new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(),
            new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime(), 0))).thenReturn(publication2);

    // Run the test
    final ResponseEntity<Publication> result = publicationControllerUnderTest.updatePublications("id", publication);

    // Verify the results
    assertEquals(expectedResult, result);
  }
}
