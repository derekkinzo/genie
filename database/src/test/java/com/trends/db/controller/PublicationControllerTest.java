package com.trends.db.controller;

import com.trends.db.model.Publication;
import com.trends.db.service.PublicationService;
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

    // Configure PublicationService.findPublicationsByKeyword(...).
    final Publication publication = new Publication();
    publication.setId("id");
    publication.setAbstractTitle("abstractTitle");
    publication.setKeywords(new HashSet<>(Arrays.asList("value")));
    publication.setSourceUri("sourceUri");
    publication.setAbstractContent("abstractContent");
    publication.setChemicals(new HashSet<>(Arrays.asList("value")));
    publication.setAuthors(new HashSet<>(Arrays.asList("value")));
    publication.setDateAccepted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication.setDateCompleted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication.setDateEntered(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Set<Publication> publications = new HashSet<>(Arrays.asList(publication));
    when(mockPublicationService.findPublicationsByKeyword("keyword")).thenReturn(publications);

    // Run the test
    final Set<Publication> result = publicationControllerUnderTest.getPublications("keyword");

    // Verify the results
  }

  @Test
  void testGetPublication() {
    // Setup

    // Configure PublicationService.findPublicationsById(...).
    final Publication publication1 = new Publication();
    publication1.setId("id");
    publication1.setAbstractTitle("abstractTitle");
    publication1.setKeywords(new HashSet<>(Arrays.asList("value")));
    publication1.setSourceUri("sourceUri");
    publication1.setAbstractContent("abstractContent");
    publication1.setChemicals(new HashSet<>(Arrays.asList("value")));
    publication1.setAuthors(new HashSet<>(Arrays.asList("value")));
    publication1.setDateAccepted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication1.setDateCompleted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication1.setDateEntered(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Optional<Publication> publication = Optional.of(publication1);
    when(mockPublicationService.findPublicationsById("id")).thenReturn(publication);

    // Run the test
    final Optional<Publication> result = publicationControllerUnderTest.getPublication("id");

    // Verify the results
  }


  @Test
  void testAddPublication() {
    // Setup
    final Publication publication = new Publication();
    publication.setId("id");
    publication.setAbstractTitle("abstractTitle");
    publication.setKeywords(new HashSet<>(Arrays.asList("value")));
    publication.setSourceUri("sourceUri");
    publication.setAbstractContent("abstractContent");
    publication.setChemicals(new HashSet<>(Arrays.asList("value")));
    publication.setAuthors(new HashSet<>(Arrays.asList("value")));
    publication.setDateAccepted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication.setDateCompleted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication.setDateEntered(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());

    // Run the test
    publicationControllerUnderTest.addPublication(publication);

    // Verify the results
    verify(mockPublicationService).savePublication(any(Publication.class));
  }

  @Test
  void testUpdatePublications() {
    // Setup
    final Publication publication = new Publication();
    publication.setId("id");
    publication.setAbstractTitle("abstractTitle");
    publication.setKeywords(new HashSet<>(Arrays.asList("value")));
    publication.setSourceUri("sourceUri");
    publication.setAbstractContent("abstractContent");
    publication.setChemicals(new HashSet<>(Arrays.asList("value")));
    publication.setAuthors(new HashSet<>(Arrays.asList("value")));
    publication.setDateAccepted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication.setDateCompleted(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    publication.setDateEntered(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());

    // Run the test
    publicationControllerUnderTest.updatePublications(0, publication);

    // Verify the results
    verify(mockPublicationService).updatePublication(any(Publication.class));
  }
}
