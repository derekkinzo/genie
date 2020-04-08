package com.trends.db.dao;

import com.trends.db.model.Publication;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
public interface PublicationRepo extends MongoRepository<Publication, String> {

  Set<Publication> findPublicationsByKeywords(final String keyword);

}
