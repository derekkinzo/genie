package com.trends.db.model;

import com.trends.db.model.enums.TrialOutcome;
import com.trends.db.model.enums.TrialStatus;
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
 * The type Clinical trial.
 */
@Document(collection = "trial")
@Getter
@Setter
@ToString(exclude = { "id" })
public class ClinicalTrial implements Serializable {

  @Id
  private String id;

  @NotBlank
  private String pubMedId;

  private String trialType;
  private TrialStatus status;

  @Indexed
  private Set<String> keywords;
  private Set<String> leadSponsors;
  private Set<String> citations;
  private Set<String> collaborators;
  private boolean isStopped;
  private String whyStopped;
  private boolean isFdaRegulated;
  private Date trialStartedOn;
  private TrialOutcome outcome;

  @CreatedDate
  private Date createdOn;

  @LastModifiedDate
  private Date updatedOn;

  @Version
  private Integer version;
}
