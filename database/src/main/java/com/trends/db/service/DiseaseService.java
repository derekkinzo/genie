package com.trends.db.service;

import com.trends.db.model.Disease;

import java.util.List;
import java.util.Optional;
import java.util.Set;

public interface DiseaseService {

  Optional<Disease> findDiseaseById(final String id);

  Set<Disease> findDiseasesByKeyword(final String keyword);

  List<Disease> findAllDiseases();

  void saveDisease(final Disease disease);

  Disease updateDisease(Disease disease, final Disease payload);
}
