package com.trends.db.controller;

import com.trends.db.model.Trend;
import com.trends.db.service.TrendsService;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;
import java.util.Optional;
import java.util.Set;

/**
 * The type Trends controller.
 */
@RestController
@RequestMapping("/v1/api")
public class TrendsController {

  private static final Logger _logger = LoggerFactory.getLogger(TrendsController.class);

  @Autowired
  private final TrendsService trendsService;

  public TrendsController(final TrendsService trendsService) {

    this.trendsService = trendsService;
  }

  /**
   * Gets trends.
   *
   * @param keyword the keyword
   * @return the trends
   */
  @ApiOperation(value = "Get Trends by keyword", nickname = "Get Trends by keyword", response = Trend.class)
  @GetMapping(path = "/trends/keyword/{keyword}")
  public Set<Trend> getTrends(@PathVariable final String keyword) {

    return trendsService.findTrendsByKeyword(keyword);
  }

  /**
   * Gets trend.
   *
   * @param id the id
   * @return the trend
   */
  @ApiOperation(value = "Get Trends by Id", nickname = "Get Trends by id", response = Trend.class)
  @GetMapping(path = "/trends/id/{id}")
  public Optional<Trend> getTrend(@PathVariable final String id) {

    return trendsService.findTrendsById(id);
  }

  /**
   * Add trends set.
   *
   * @param trends the trends
   * @return the set
   */
  @PostMapping(path = "/trends")
  public void addTrends(@RequestBody @Valid final Set<Trend> trends) {

    trendsService.saveTrends(trends);
  }

  /**
   * Add trend set.
   *
   * @param trend the trend
   * @return the set
   */
  @PostMapping(path = "/trend/add")
  public void addTrend(@RequestBody @Valid final Trend trend) {

    trendsService.saveTrend(trend);
  }

  /**
   * Update trends set.
   *
   * @param trend the trend
   * @return the set
   */
  @PutMapping(path = "/trends/update/{id}")
  public void updateTrends(@PathVariable final Integer id, @RequestBody @Valid final Trend trend) {

    trendsService.updateTrend(trend);
  }
}
