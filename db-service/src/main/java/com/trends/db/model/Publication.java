package com.trends.db.model;

import com.fasterxml.jackson.annotation.JsonProperty;
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
@Getter
@Setter
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
}
