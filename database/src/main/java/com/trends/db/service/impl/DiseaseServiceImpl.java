package com.trends.db.service.impl;

import com.trends.db.dao.DiseaseRepo;
import com.trends.db.model.Disease;
import com.trends.db.service.DiseaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.Set;

@Service
public class DiseaseServiceImpl implements DiseaseService {

  @Autowired
  private DiseaseRepo dao;

  @Override
  public Optional<Disease> findDiseaseById(final String id) {

    return dao.findById(id);
  }

  @Override
  public Set<Disease> findDiseasesByKeyword(final String keyword) {

    return dao.findDiseasesByKeywords(keyword);
  }

  @Override
  public List<Disease> findAllDiseases() {

    return dao.findAll();
  }

  @Override
  public void saveDisease(final Disease disease) {

    dao.insert(disease);
  }

  @Override
  public Disease updateDisease(final Disease disease, final Disease payload) {

     return dao.insert(disease);
  }

}
