package com.trends.db.service.impl;

import com.trends.db.dao.PublicationRepo;
import com.trends.db.model.Publication;
import com.trends.db.service.PublicationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.Set;

@Service
public class PublicationServiceImpl implements PublicationService {

  @Autowired
  private PublicationRepo dao;

  @Override
  public Optional<Publication> findPublicationsById(final String id) {

    return dao.findById(id);
  }

  @Override
  public Set<Publication> findPublicationsByKeyword(final String keyword) {

    return dao.findPublicationsByKeywords(keyword);
  }

  @Override
  public List<Publication> findAllPublications() {

    return dao.findAll();
  }

  @Override
  public void savePublication(final Publication publication) {

    dao.insert(publication);
  }

  @Override
  public Publication updatePublication(final Publication publication, final Publication payload) {

    return dao.insert(publication);
  }

}
