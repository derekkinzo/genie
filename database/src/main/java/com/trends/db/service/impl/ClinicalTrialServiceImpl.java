package com.trends.db.service.impl;

import com.trends.db.dao.ClinicalTrialRepo;
import com.trends.db.model.ClinicalTrial;
import com.trends.db.service.ClinicalTrialService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.List;
import java.util.Optional;
import java.util.Set;

@Service
public class ClinicalTrialServiceImpl implements ClinicalTrialService {

  @Autowired
  private ClinicalTrialRepo dao;

  @Override
  public Optional<ClinicalTrial> findClinicalTrialsById(final String id) {

    return dao.findById(id);
  }

  @Override
  public Set<ClinicalTrial> findClinicalTrialsByKeyword(final String keyword) {

    return dao.findClinicalTrialsByKeywords(keyword);
  }

  @Override
  public List<ClinicalTrial> findAllClinicalTrials() {

    return dao.findAll();
  }

  @Override
  public void saveClinicalTrial(final ClinicalTrial clinicalTrial) {

    dao.insert(clinicalTrial);
  }

  @Override
  public ClinicalTrial updateClinicalTrial(ClinicalTrial clinicalTrial, final ClinicalTrial payload) {

    clinicalTrial.setCitations(payload.getCitations());
    clinicalTrial.setCollaborators(payload.getCollaborators());
    clinicalTrial.setKeywords(payload.getKeywords());
    clinicalTrial.setFdaRegulated(payload.isFdaRegulated());
    clinicalTrial.setCreatedOn(payload.getCreatedOn());
    clinicalTrial.setLeadSponsors(payload.getLeadSponsors());
    clinicalTrial.setOutcome(payload.getOutcome());
    clinicalTrial.setPubMedId(payload.getPubMedId());
    clinicalTrial.setStatus(payload.getStatus());
    clinicalTrial.setStopped(payload.isStopped());
    clinicalTrial.setTrialStartedOn(payload.getTrialStartedOn());
    clinicalTrial.setTrialType(payload.getTrialType());
    clinicalTrial.setWhyStopped(payload.getWhyStopped());
    clinicalTrial.setUpdatedOn(new Date());

    return dao.insert(clinicalTrial);
  }
}
