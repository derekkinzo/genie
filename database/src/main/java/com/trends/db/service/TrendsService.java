package com.trends.db.service;

import com.trends.db.model.Trend;

import java.util.List;
import java.util.Optional;
import java.util.Set;

public interface TrendsService {

  Optional<Trend> findTrendsById(final String id);

  Set<Trend> findTrendsByKeyword(final String keyword);

  List<Trend> findAllTrends();

  void saveTrend(final Trend trend);

  Trend updateTrend(Trend trend, final Trend payload);
}
