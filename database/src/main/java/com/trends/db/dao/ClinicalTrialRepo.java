package com.trends.db.dao;

import com.trends.db.model.ClinicalTrial;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
public interface ClinicalTrialRepo extends MongoRepository<ClinicalTrial, String> {

  Set<ClinicalTrial> findClinicalTrialsByKeywords(final String keyword);



}
