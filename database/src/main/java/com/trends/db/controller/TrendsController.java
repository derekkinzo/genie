package com.trends.db.controller;

import com.trends.db.model.Trend;
import com.trends.db.model.exception.TrendException;
import com.trends.db.model.exception.TrialException;
import com.trends.db.service.TrendsService;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;
import java.util.List;
import java.util.Optional;
import java.util.Set;

/**
 * The type Trends controller.
 */
@RestController
@RequestMapping("/v1/api")
public class TrendsController {

  private static final Logger _logger = LoggerFactory.getLogger(TrendsController.class);

  private final TrendsService trendsService;

  public TrendsController(final TrendsService trendsService) {

    this.trendsService = trendsService;
  }

  /**
   * Gets trends.
   *
   * @return the trends
   */
  @ApiOperation(value = "Get Trends", nickname = "Get all trends", response = Trend.class)
  @GetMapping(path = "/trends", produces = "application/json")
  public ResponseEntity<List<Trend>> getTrends() {

    _logger.info("Getting all Trends...");

    final List<Trend> trends;

    try {
      trends = trendsService.findAllTrends();
    } catch (TrendException e) {
      _logger.error("Trends fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!trends.isEmpty()) {
      return ResponseEntity.ok().body(trends);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets trends.
   *
   * @param keyword the keyword
   * @return the trends
   */
  @ApiOperation(value = "Get Trends by keyword", nickname = "Get Trends by keyword", response = Trend.class)
  @GetMapping(path = "/trends/keyword/{keyword}", produces = "application/json")
  public ResponseEntity<Set<Trend>> getTrendsByKeyword(@PathVariable final String keyword) {

    _logger.info("Getting trends for keyword: {}", keyword);
    final Set<Trend> trends;

    try {
      trends = trendsService.findTrendsByKeyword(keyword);
    } catch (TrendException e) {
      _logger.error("Trends fetch failed");
      return ResponseEntity.notFound().build();
    }

    if (!trends.isEmpty()) {
      return ResponseEntity.ok().body(trends);

    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

  /**
   * Gets trend.
   *
   * @param id the id
   * @return the trend
   */
  @ApiOperation(value = "Get Trend by Id", nickname = "Get Trend by id", response = Trend.class)
  @GetMapping(path = "/trends/id/{id}", produces = "application/json")
  public ResponseEntity<Trend> getTrendById(@PathVariable final String id) {

    _logger.info("Getting trend for id: {}", id);
    final Optional<Trend> trend;

    try {
      trend = trendsService.findTrendsById(id);
    } catch (TrendException e) {
      _logger.error("Trend fetch failed");
      return ResponseEntity.notFound().build();
    }

    return trend.map(value -> ResponseEntity.ok().body(value))
                .orElseGet(() -> ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build());
  }

  /**
   * Add trend set.
   *
   * @param trend the trend
   * @return the set
   */
  @PostMapping(path = "/trend/add", consumes = "application/json")
  public void addTrend(@RequestBody @Valid final Trend trend) {

    trendsService.saveTrend(trend);
  }

  /**
   * Update trends set.
   *
   * @param trend the trend
   * @return the set
   */
  @PutMapping(path = "/trends/update/{id}", consumes = "application/json")
  public ResponseEntity<Trend> updateTrends(@PathVariable final String id, @RequestBody @Valid final Trend trend) {

    Optional<Trend> foundTrend =
        Optional.ofNullable(trendsService.findTrendsById(id)
                                         .orElseThrow(
                                             () -> new TrialException(String.format("Trend id %s not found", id))));
    final Trend updatedTrend = trendsService.updateTrend(foundTrend.get(), trend);
    return ResponseEntity.ok(updatedTrend);
  }
}
