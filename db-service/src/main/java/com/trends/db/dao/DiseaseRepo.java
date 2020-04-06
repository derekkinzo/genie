package com.trends.db.dao;

import com.trends.db.model.Disease;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
public interface DiseaseRepo extends MongoRepository<Disease, String> {

  Set<Disease> findDiseasesByKeywords(final String keyword);

}
