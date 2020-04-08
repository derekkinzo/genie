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

import javax.validation.constraints.NotBlank;
import java.io.Serializable;
import java.util.Date;
import java.util.Set;

/**
 * The type Patent.
 */
@Document(collection = "patent")
@Getter
@Setter
@ToString(exclude = { "id" })
public class Patent implements Serializable {

  @Id
  private String id;

  @NotBlank
  private String drugName;

  @Indexed
  private Set<String> keywords;
  private Set<String> aliases;
  private Set<String> participants;
  private String patent;
  private String patentNumber;
  private boolean isActive;
  private Date acquiredOn;
  private Date expiresOn;

  @CreatedDate
  private Date createdOn;

  @LastModifiedDate
  private Date updatedOn;

  @Version
  private Integer version;
}
