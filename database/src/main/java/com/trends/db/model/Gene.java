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

import javax.validation.constraints.NotBlank;
import java.io.Serializable;
import java.util.Date;
import java.util.Set;

/**
 * The type Gene.
 */
@Document(collection = "gene")
@Data
@ToString(exclude = { "id" })
public class Gene implements Serializable {

  @Id
  private String id;

  @NotBlank
  private String approvedGeneName;
  private Set<String> approvedSymbols;

  @Indexed
  private Set<String> keywords;
  private Set<String> aliases;
  private boolean symbolStatus;
  private String chromosomalLocation;
  private String geneGroup;
  private String geneId;

  @CreatedDate
  private Date createdOn;

  @LastModifiedDate
  private Date updatedOn;

  @Version
  private Integer version;

  public Gene(@NotBlank final String approvedGeneName, final Set<String> approvedSymbols, final Set<String> keywords,
              final Set<String> aliases, final boolean symbolStatus, final String chromosomalLocation,
              final String geneGroup, final String geneId,
              final Date createdOn, final Date updatedOn, final Integer version) {

    this.approvedGeneName = approvedGeneName;
    this.approvedSymbols = approvedSymbols;
    this.keywords = keywords;
    this.aliases = aliases;
    this.symbolStatus = symbolStatus;
    this.chromosomalLocation = chromosomalLocation;
    this.geneGroup = geneGroup;
    this.geneId = geneId;
    this.createdOn = createdOn;
    this.updatedOn = updatedOn;
    this.version = version;
  }
}
