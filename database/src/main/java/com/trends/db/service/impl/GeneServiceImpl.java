package com.trends.db.service.impl;

import com.trends.db.dao.GeneRepo;
import com.trends.db.model.Gene;
import com.trends.db.service.GeneService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.Set;

@Service
public class GeneServiceImpl implements GeneService {

  @Autowired
  private GeneRepo dao;

  @Override
  public Optional<Gene> findGenesById(final String id) {

    return dao.findById(id);
  }

  @Override
  public Set<Gene> findGenesByKeyword(final String keyword) {

    return dao.findGenesByKeywords(keyword);
  }

  @Override
  public List<Gene> findAllGenes() {

    return dao.findAll();
  }

  @Override
  public void saveGene(final Gene gene) {

    dao.insert(gene);
  }

  @Override
  public Gene updateGene(final Gene gene, final Gene payload) {

    return dao.insert(gene);
  }

}
