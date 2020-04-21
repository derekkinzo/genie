package com.trends.db.model;

import com.fasterxml.jackson.annotation.JsonProperty;
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
 * The type Publication.
 */
@Document(collection = "publication")
@Data
@ToString(exclude = { "id" })
public class Publication implements Serializable {

  @Id
  @JsonProperty(value = "pubmed_id")
  private String id;

  @NotBlank
  @JsonProperty(value = "title")
  private String abstractTitle;

  @Indexed
  @JsonProperty(value = "mesh")
  private Set<String> keywords;
  private String sourceUri;

  @NotBlank
  @JsonProperty(value = "abstract")
  private String abstractContent;

  @JsonProperty(value = "chemicals")
  private Set<String> chemicals;

  @JsonProperty(value = "authors")
  private Set<String> authors;

  private Date dateAccepted;

  private Date dateCompleted;

  private Date dateEntered;

  private Date dateReceived;

  private Date dateRevised;

  private String doiId;

  private String language;

  private String piiId;

  private String pmcId;

  private String pmiId;

  private String publishStatus;

  @CreatedDate
  private Date createdOn;

  @LastModifiedDate
  private Date updatedOn;

  @Version
  private Integer version;

  public Publication(@NotBlank final String abstractTitle, final Set<String> keywords, final String sourceUri,
                     @NotBlank final String abstractContent, final Set<String> chemicals, final Set<String> authors,
                     final Date dateAccepted,
                     final Date dateCompleted, final Date dateEntered, final Date dateReceived, final Date dateRevised,
                     final String doiId,
                     final String language, final String piiId, final String pmcId, final String pmiId,
                     final String publishStatus, final Date createdOn,
                     final Date updatedOn, final Integer version) {

    this.abstractTitle = abstractTitle;
    this.keywords = keywords;
    this.sourceUri = sourceUri;
    this.abstractContent = abstractContent;
    this.chemicals = chemicals;
    this.authors = authors;
    this.dateAccepted = dateAccepted;
    this.dateCompleted = dateCompleted;
    this.dateEntered = dateEntered;
    this.dateReceived = dateReceived;
    this.dateRevised = dateRevised;
    this.doiId = doiId;
    this.language = language;
    this.piiId = piiId;
    this.pmcId = pmcId;
    this.pmiId = pmiId;
    this.publishStatus = publishStatus;
    this.createdOn = createdOn;
    this.updatedOn = updatedOn;
    this.version = version;
  }
}
