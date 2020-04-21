package com.trends.db.service.impl;

import com.trends.db.dao.PatentRepo;
import com.trends.db.model.Patent;
import com.trends.db.service.PatentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.Set;

@Service
public class PatentServiceImpl implements PatentService {

  @Autowired
  private PatentRepo dao;

  @Override
  public Optional<Patent> findPatentsById(final String id) {

    return dao.findById(id);
  }

  @Override
  public Set<Patent> findPatentsByKeyword(final String keyword) {

    return dao.findPatentsByKeywords(keyword);
  }

  @Override
  public List<Patent> findAllPatents() {

    return dao.findAll();
  }

  @Override
  public void savePatent(final Patent patent) {

    dao.insert(patent);
  }

  @Override
  public Patent updatePatent(final Patent patent, final Patent payload) {

     return dao.insert(patent);
  }

}
