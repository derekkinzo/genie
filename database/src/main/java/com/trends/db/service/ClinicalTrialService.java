package com.trends.db.service;

import com.trends.db.model.ClinicalTrial;

import java.util.List;
import java.util.Optional;
import java.util.Set;

public interface ClinicalTrialService {

  Optional<ClinicalTrial> findClinicalTrialsById(final String id);

  Set<ClinicalTrial> findClinicalTrialsByKeyword(final String keyword);

  List<ClinicalTrial> findAllClinicalTrials();

  void saveClinicalTrial(final ClinicalTrial clinicalTrial);

  ClinicalTrial updateClinicalTrial(ClinicalTrial clinicalTrial, final ClinicalTrial payload);

}
