package com.trends.db.dao;

import com.trends.db.model.Patent;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
public interface PatentRepo extends MongoRepository<Patent, String> {

  Set<Patent> findPatentsByKeywords(final String keyword);

}
