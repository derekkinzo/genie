package com.trends.db.config;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.Mockito;

import static org.junit.jupiter.api.Assertions.assertThrows;

class TrendsDBConfigTest {

  private static final String db = "mongodb://localhost:27017/dev-trends-db";

  private TrendsDBConfig trendsDBConfigUnderTest;

  @BeforeEach
  void setUp() {

    trendsDBConfigUnderTest = new TrendsDBConfig();
  }


  @Test
  void testMongoClient_ThrowsException() {
    // Setup

    // Run the test
    assertThrows(Exception.class, () -> {
      trendsDBConfigUnderTest.mongoClient();
    });
  }
}
