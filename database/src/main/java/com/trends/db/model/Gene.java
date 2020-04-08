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
 * The type Gene.
 */
@Document(collection = "gene")
@Getter
@Setter
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
}
