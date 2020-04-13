package com.trends.db.service.impl;

import com.trends.db.dao.PatentRepo;
import com.trends.db.model.Patent;
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

class PatentServiceImplTest {

  @Mock private PatentRepo mockDao;

  @InjectMocks private PatentServiceImpl patentServiceImplUnderTest;

  @BeforeEach
  void setUp() {

    initMocks(this);
  }

  @Test
  void testFindPatentsById() {
    // Setup

    // Configure PatentRepo.findById(...).
    final Patent patent1 = new Patent();
    patent1.setId("id");
    patent1.setDrugName("drugName");
    patent1.setKeywords(new HashSet<>(Arrays.asList("value")));
    patent1.setAliases(new HashSet<>(Arrays.asList("value")));
    patent1.setParticipants(new HashSet<>(Arrays.asList("value")));
    patent1.setPatent("patent");
    patent1.setPatentNumber("patentNumber");
    patent1.setActive(false);
    patent1.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    patent1.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Optional<Patent> patent = Optional.of(patent1);
    when(mockDao.findById("id")).thenReturn(patent);

    // Run the test
    final Optional<Patent> result = patentServiceImplUnderTest.findPatentsById("id");

    // Verify the results
  }

  @Test
  void testFindPatentsByKeyword() {
    // Setup

    // Configure PatentRepo.findPatentsByKeywords(...).
    final Patent patent = new Patent();
    patent.setId("id");
    patent.setDrugName("drugName");
    patent.setKeywords(new HashSet<>(Arrays.asList("value")));
    patent.setAliases(new HashSet<>(Arrays.asList("value")));
    patent.setParticipants(new HashSet<>(Arrays.asList("value")));
    patent.setPatent("patent");
    patent.setPatentNumber("patentNumber");
    patent.setActive(false);
    patent.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    patent.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Set<Patent> patents = new HashSet<>(Arrays.asList(patent));
    when(mockDao.findPatentsByKeywords("keyword")).thenReturn(patents);

    // Run the test
    final Set<Patent> result = patentServiceImplUnderTest.findPatentsByKeyword("keyword");

    // Verify the results
  }

  @Test
  void testFindAllPatents() {
    // Setup

    // Configure PatentRepo.findAll(...).
    final Patent patent = new Patent();
    patent.setId("id");
    patent.setDrugName("drugName");
    patent.setKeywords(new HashSet<>(Arrays.asList("value")));
    patent.setAliases(new HashSet<>(Arrays.asList("value")));
    patent.setParticipants(new HashSet<>(Arrays.asList("value")));
    patent.setPatent("patent");
    patent.setPatentNumber("patentNumber");
    patent.setActive(false);
    patent.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    patent.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final List<Patent> patents = Arrays.asList(patent);
    when(mockDao.findAll()).thenReturn(patents);

    // Run the test
    final List<Patent> result = patentServiceImplUnderTest.findAllPatents();

    // Verify the results
  }

  @Test
  void testSavePatents() {
    // Setup
    final Patent patent = new Patent();
    patent.setId("id");
    patent.setDrugName("drugName");
    patent.setKeywords(new HashSet<>(Arrays.asList("value")));
    patent.setAliases(new HashSet<>(Arrays.asList("value")));
    patent.setParticipants(new HashSet<>(Arrays.asList("value")));
    patent.setPatent("patent");
    patent.setPatentNumber("patentNumber");
    patent.setActive(false);
    patent.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    patent.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final Set<Patent> genes = new HashSet<>(Arrays.asList(patent));

    // Configure PatentRepo.insert(...).
    final Patent patent1 = new Patent();
    patent1.setId("id");
    patent1.setDrugName("drugName");
    patent1.setKeywords(new HashSet<>(Arrays.asList("value")));
    patent1.setAliases(new HashSet<>(Arrays.asList("value")));
    patent1.setParticipants(new HashSet<>(Arrays.asList("value")));
    patent1.setPatent("patent");
    patent1.setPatentNumber("patentNumber");
    patent1.setActive(false);
    patent1.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    patent1.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    final List<Patent> patents = Arrays.asList(patent1);
    when(mockDao.insert(Arrays.asList())).thenReturn(patents);

    // Run the test
    patentServiceImplUnderTest.savePatents(genes);

    // Verify the results
  }

  @Test
  void testSavePatent() {
    // Setup
    final Patent gene = new Patent();
    gene.setId("id");
    gene.setDrugName("drugName");
    gene.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene.setAliases(new HashSet<>(Arrays.asList("value")));
    gene.setParticipants(new HashSet<>(Arrays.asList("value")));
    gene.setPatent("patent");
    gene.setPatentNumber("patentNumber");
    gene.setActive(false);
    gene.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    gene.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());

    // Configure PatentRepo.insert(...).
    final Patent patent = new Patent();
    patent.setId("id");
    patent.setDrugName("drugName");
    patent.setKeywords(new HashSet<>(Arrays.asList("value")));
    patent.setAliases(new HashSet<>(Arrays.asList("value")));
    patent.setParticipants(new HashSet<>(Arrays.asList("value")));
    patent.setPatent("patent");
    patent.setPatentNumber("patentNumber");
    patent.setActive(false);
    patent.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    patent.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    when(mockDao.insert(any(Patent.class))).thenReturn(patent);

    // Run the test
    patentServiceImplUnderTest.savePatent(gene);

    // Verify the results
  }

  @Test
  void testUpdatePatent() {
    // Setup
    final Patent gene = new Patent();
    gene.setId("id");
    gene.setDrugName("drugName");
    gene.setKeywords(new HashSet<>(Arrays.asList("value")));
    gene.setAliases(new HashSet<>(Arrays.asList("value")));
    gene.setParticipants(new HashSet<>(Arrays.asList("value")));
    gene.setPatent("patent");
    gene.setPatentNumber("patentNumber");
    gene.setActive(false);
    gene.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    gene.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());

    // Configure PatentRepo.insert(...).
    final Patent patent = new Patent();
    patent.setId("id");
    patent.setDrugName("drugName");
    patent.setKeywords(new HashSet<>(Arrays.asList("value")));
    patent.setAliases(new HashSet<>(Arrays.asList("value")));
    patent.setParticipants(new HashSet<>(Arrays.asList("value")));
    patent.setPatent("patent");
    patent.setPatentNumber("patentNumber");
    patent.setActive(false);
    patent.setAcquiredOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    patent.setExpiresOn(new GregorianCalendar(2019, Calendar.JANUARY, 1).getTime());
    when(mockDao.insert(any(Patent.class))).thenReturn(patent);

    // Run the test
    patentServiceImplUnderTest.updatePatent(gene);

    // Verify the results
  }
}
