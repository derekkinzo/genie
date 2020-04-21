package com.trends.db.model;

import lombok.Data;
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
@Data
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

  public Trend(final Set<String> keywords, final Set<String> geneSymbols, final Set<Disease> associatedDiseases,
               final long totalAssociations,
               final String chromosomalLocation, final Date createdOn, final Date updatedOn, final Integer version) {

    this.keywords = keywords;
    this.geneSymbols = geneSymbols;
    this.associatedDiseases = associatedDiseases;
    this.totalAssociations = totalAssociations;
    this.chromosomalLocation = chromosomalLocation;
    this.createdOn = createdOn;
    this.updatedOn = updatedOn;
    this.version = version;
  }
}
