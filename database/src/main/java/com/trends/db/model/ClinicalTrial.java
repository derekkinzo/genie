package com.trends.db.model;

import com.trends.db.model.enums.TrialOutcome;
import com.trends.db.model.enums.TrialStatus;
import lombok.Data;
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
@Data
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

  public ClinicalTrial(@NotBlank final String pubMedId, final String trialType, final TrialStatus status,
                       final Set<String> keywords, final Set<String> leadSponsors, final Set<String> citations,
                       final Set<String> collaborators, final boolean isStopped, final String whyStopped,
                       final boolean isFdaRegulated,
                       final Date trialStartedOn, final TrialOutcome outcome, final Date createdOn, final Date updatedOn,
                       final Integer version) {

    this.pubMedId = pubMedId;
    this.trialType = trialType;
    this.status = status;
    this.keywords = keywords;
    this.leadSponsors = leadSponsors;
    this.citations = citations;
    this.collaborators = collaborators;
    this.isStopped = isStopped;
    this.whyStopped = whyStopped;
    this.isFdaRegulated = isFdaRegulated;
    this.trialStartedOn = trialStartedOn;
    this.outcome = outcome;
    this.createdOn = createdOn;
    this.updatedOn = updatedOn;
    this.version = version;
  }
}


