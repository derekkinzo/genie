package com.trends.db.service;

import com.trends.db.model.Disease;

import java.util.List;
import java.util.Optional;
import java.util.Set;

public interface DiseaseService {

  Optional<Disease> findDiseasesById(final String id);

  Set<Disease> findDiseasesByKeyword(final String keyword);

  List<Disease> findAllDiseases();

  void saveDiseases(final Set<Disease> diseases);

  void saveDisease(final Disease disease);

  void updateDisease(final Disease disease);
}
