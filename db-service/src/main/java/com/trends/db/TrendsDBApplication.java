package com.trends.db;

import com.trends.db.config.TrendsDBConfig;
import com.trends.db.dao.ClinicalTrialRepo;
import com.trends.db.dao.DiseaseRepo;
import com.trends.db.dao.GeneRepo;
import com.trends.db.dao.PatentRepo;
import com.trends.db.dao.PublicationRepo;
import com.trends.db.dao.TrendRepo;
import com.trends.db.model.ClinicalTrial;
import com.trends.db.model.Disease;
import com.trends.db.model.Gene;
import com.trends.db.model.Patent;
import com.trends.db.model.Publication;
import com.trends.db.model.Trend;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.data.mongodb.config.EnableMongoAuditing;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

import java.util.Calendar;
import java.util.Collections;

/**
 * The type Trends com.trends.db application.
 */
@SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })
@Slf4j
@EnableMongoAuditing
public class TrendsDBApplication implements CommandLineRunner {

  private static final Integer version = 1;

  @Autowired
  private TrendRepo trendRepo;

  @Autowired
  private DiseaseRepo diseaseRepo;

  @Autowired
  private GeneRepo geneRepo;

  @Autowired
  private PatentRepo patentRepo;

  @Autowired
  private PublicationRepo publicationRepo;

  @Autowired
  private ClinicalTrialRepo clinicalTrialRepo;

  @Autowired
  private TrendsDBConfig trendsDBConfig;

  /**
   * The entry point of application.
   *
   * @param args the input arguments.
   */
  public static void main(String[] args) {

    SpringApplication.run(TrendsDBApplication.class, args);
  }

  @Bean
  public Docket trendsApi() {

    return new Docket(DocumentationType.SWAGGER_2)
        .select()
        .apis(RequestHandlerSelectors.any())
        .paths(PathSelectors.any())
        .build();
  }

  @Override
  public void run(final String... args) throws Exception {

    // Empty the schema
//    trendRepo.deleteAll();
//    clinicalTrialRepo.deleteAll();
//    publicationRepo.deleteAll();
//    patentRepo.deleteAll();
//    geneRepo.deleteAll();
//    diseaseRepo.deleteAll();

    // Create Schema
    diseaseRepo.insert(new Disease("Covid-19",
        Collections.singleton("CoronaVirus"),
        Collections.singleton("Some Alias"),
        Collections.singleton("Some Drug"),
        true,
        Calendar.getInstance().getTime(),
        Calendar.getInstance().getTime(),
        version));

    geneRepo.save(new Gene());
    patentRepo.save(new Patent());
    publicationRepo.save(new Publication());
    clinicalTrialRepo.save(new ClinicalTrial());
    trendRepo.save(new Trend());
  }
}
