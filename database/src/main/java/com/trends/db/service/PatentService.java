package com.trends.db.service;

import com.trends.db.model.Patent;

import java.util.List;
import java.util.Optional;
import java.util.Set;

public interface PatentService {

  Optional<Patent> findPatentsById(final String id);

  Set<Patent> findPatentsByKeyword(final String keyword);

  List<Patent> findAllPatents();

  void savePatent(final Patent patent);

  Patent updatePatent(Patent patent, final Patent payload);
}
