package com.trends.db.config;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class TrendsDBConfig {

  private Logger logger = LoggerFactory.getLogger(TrendsDBConfig.class);

  @Value("${spring.data.mongodb.uri}")
  private String mongoUri;

  @Bean
  public MongoClient mongoClient() throws Exception {

    logger.info("Mongo URI: " + mongoUri);
    return MongoClients.create(mongoUri);
  }
}
