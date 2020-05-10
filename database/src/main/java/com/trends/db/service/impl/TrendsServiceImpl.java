package com.trends.db.service.impl;

import com.trends.db.dao.TrendRepo;
import com.trends.db.model.Trend;
import com.trends.db.service.TrendsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.Set;

@Service
public class TrendsServiceImpl implements TrendsService {

  @Autowired
  private TrendRepo dao;

  @Override
  public Optional<Trend> findTrendsById(final String id) {

    return dao.findById(id);
  }

  @Override
  public Set<Trend> findTrendsByKeyword(final String keyword) {

    return dao.findTrendsByKeywords(keyword);
  }

  @Override
  public List<Trend> findAllTrends() {

    return dao.findAll();
  }

  @Override
  public void saveTrend(final Trend trend) {

    dao.insert(trend);
  }

  @Override
  public Trend updateTrend(final Trend trend, final Trend payload) {

    return dao.insert(trend);
  }

}
