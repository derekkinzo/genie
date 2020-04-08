package com.trends.db.model;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.annotation.Version;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

import java.io.Serializable;
import java.util.Date;
import java.util.Set;

/**
 * The type Trend.
 */
@Document(collection = "trend")
@Getter
@Setter
@ToString(exclude = { "id" })
public class Trend implements Serializable {

  @Id
  private String id;

  @Indexed
  private Set<String> keywords;
  private Set<String> geneSymbols;
  private Set<Disease> associatedDiseases;
  private long totalAssociations;
  private String chromosomalLocation;

  @CreatedDate
  private Date createdOn;

  @LastModifiedDate
  private Date updatedOn;

  @Version
  private Integer version;

}
