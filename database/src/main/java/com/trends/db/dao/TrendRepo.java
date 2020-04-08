package com.trends.db.dao;

import com.trends.db.model.Trend;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
public interface TrendRepo extends MongoRepository<Trend, String> {

  Set<Trend> findTrendsByKeywords(final String keyword);

}
