package com.trends.db.controller;

import com.trends.db.model.Patent;
import com.trends.db.service.PatentService;
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

    // Configure PatentService.findPatentsByKeyword(...).
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
    when(mockPatentService.findPatentsByKeyword("keyword")).thenReturn(patents);

    // Run the test
    final Set<Patent> result = patentControllerUnderTest.getPatents("keyword");

    // Verify the results
  }

  @Test
  void testGetPatent() {
    // Setup

    // Configure PatentService.findPatentsById(...).
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
    when(mockPatentService.findPatentsById("id")).thenReturn(patent);

    // Run the test
    final Optional<Patent> result = patentControllerUnderTest.getPatent("id");

    // Verify the results
  }


  @Test
  void testAddPatent() {
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

    // Run the test
    patentControllerUnderTest.addPatent(patent);

    // Verify the results
    verify(mockPatentService).savePatent(any(Patent.class));
  }

  @Test
  void testUpdatePatents() {
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

    // Run the test
    patentControllerUnderTest.updatePatents(0, patent);

    // Verify the results
    verify(mockPatentService).updatePatent(any(Patent.class));
  }
}
