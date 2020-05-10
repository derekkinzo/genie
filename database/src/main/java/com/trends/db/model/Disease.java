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
 * The type Disease.
 */
@Document(collection = "disease")
@Data
@ToString(exclude = { "id" })
public class Disease implements Serializable {

  @Id
  private String id;

  @NotBlank
  private String diseaseName;

  @Indexed
  private Set<String> keywords;
  private Set<String> aliases;
  private Set<String> approvedDrugs;
  private boolean isActive;

  @CreatedDate
  private Date createdOn;

  @LastModifiedDate
  private Date updatedOn;

  @Version
  private Integer version;

  public Disease(@NotBlank final String diseaseName, final Set<String> keywords, final Set<String> aliases,
                 final Set<String> approvedDrugs, final boolean isActive, final Date createdOn, final Date updatedOn,
                 final Integer version) {

    this.diseaseName = diseaseName;
    this.keywords = keywords;
    this.aliases = aliases;
    this.approvedDrugs = approvedDrugs;
    this.isActive = isActive;
    this.createdOn = createdOn;
    this.updatedOn = updatedOn;
    this.version = version;
  }
}
