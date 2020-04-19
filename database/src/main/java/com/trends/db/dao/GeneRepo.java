package com.trends.db.dao;

import com.trends.db.model.Gene;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
public interface GeneRepo extends MongoRepository<Gene, String> {

  Set<Gene> findGenesByKeywords(final String keyword);

}
