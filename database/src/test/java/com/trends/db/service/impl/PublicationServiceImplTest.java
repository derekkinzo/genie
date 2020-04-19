package com.trends.db.service.impl;

import com.trends.db.dao.PublicationRepo;
import com.trends.db.model.Publication;
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

class PublicationServiceImplTest {

  @Mock private PublicationRepo mockDao;

  @InjectMocks private PublicationServiceImpl publicationServiceImplUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
  }

  @Test
  void testFindPublicationsById() {
    // Setup

    // Configure PublicationRepo.findById(...).
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
    when(mockDao.findById("id")).thenReturn(publication);

    // Run the test
    final Optional<Publication> result = publicationServiceImplUnderTest.findPublicationsById("id");

    // Verify the results
  }

  @Test
  void testFindPublicationsByKeyword() {
    // Setup

    // Configure PublicationRepo.findPublicationsByKeywords(...).
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
    when(mockDao.findPublicationsByKeywords("keyword")).thenReturn(publications);

    // Run the test
    final Set<Publication> result = publicationServiceImplUnderTest.findPublicationsByKeyword("keyword");

    // Verify the results
  }

  @Test
  void testFindAllPublications() {
    // Setup

    // Run the test
    final List<Publication> result = publicationServiceImplUnderTest.findAllPublications();

    // Verify the results
  }

  @Test
  void testSavePublications() {
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
    final Set<Publication> publications = new HashSet<>(Arrays.asList(publication));

    // Configure PublicationRepo.insert(...).
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
    final List<Publication> publications1 = Arrays.asList(publication1);
    when(mockDao.insert(Arrays.asList())).thenReturn(publications1);

    // Run the test
    publicationServiceImplUnderTest.savePublications(publications);

    // Verify the results
  }

  @Test
  void testSavePublication() {
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

    // Configure PublicationRepo.insert(...).
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
    when(mockDao.insert(any(Publication.class))).thenReturn(publication1);

    // Run the test
    publicationServiceImplUnderTest.savePublication(publication);

    // Verify the results
  }

  @Test
  void testUpdatePublication() {
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

    // Configure PublicationRepo.insert(...).
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
    when(mockDao.insert(any(Publication.class))).thenReturn(publication1);

    // Run the test
    publicationServiceImplUnderTest.updatePublication(publication);

    // Verify the results
  }
}
