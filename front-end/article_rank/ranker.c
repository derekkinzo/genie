// stores the articles in the array with its score and citations. It runs the page rank algorithm for NUM_ITERS iterations and writes the results in result_rankings.
// This program performs about 5 iterations of page rank per second on 32 million articles with 16 cores.

#define _DEFAULT_SOURCE

#include <math.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include "ranker.h"

int NUM_ARTICLES;
Article* ARTICLES;

void* update(void* seg) {
  int segment = *((int*)seg);
  for (int n = 0; n < NUM_ITERS; n++) {
    printf("segment: %d, iteration: %d\n", segment, n);

    for (int i = segment; i < NUM_ARTICLES; i+= NUM_CORES) {
      Article* article = &ARTICLES[i];
      if (article->score) {
        long double score = 0;
        for (int j = 0; j < article->num_citations; j++) {
          Article citer = ARTICLES[article->citations[j]];
          score += citer.score / citer.num_cited;
        }
        article->score = HYDRATION + DEHYDRATION * score;
      }
    }
  }
  return NULL;
}

int cmp_scores(const void* result1, const void* result2) {
  Result r1 = *((Result*)result1);
  Result r2 = *((Result*)result2);
  if (r1.score > r2.score) {
    return -1;
  } else if (r2.score > r1.score) {
    return 1;
  } else {
    return 0;
  }
}

void write_results() {
  Result* results = malloc(sizeof(Result) * NUM_ARTICLES);
  for (int i = 0; i < NUM_ARTICLES; i++) {
    results[i].index = i;
    results[i].score = ARTICLES[i].score;
  }

  qsort(results, NUM_ARTICLES, sizeof(Result), cmp_scores);

  FILE* file = fopen("data/rankings", "w");

  long double total_score = 0;
  for (int i = 0; i < NUM_ARTICLES; i++) {
    if (results[i].score) {
      int index = results[i].index;
      long double score = results[i].score;
      total_score += score;
      fprintf(file, "%d,%Lf,", index, score);
      Article article = ARTICLES[index];
      fprintf(file, "%d,", article.num_citations);
      long double citation_scores = HYDRATION;
      for (int j = 0; j < article.num_citations; j++) {
        int citer = article.citations[j];
        citation_scores += DEHYDRATION * ARTICLES[citer].score / ARTICLES[citer].num_cited;
      }
      fprintf(file, "%Lf\n", citation_scores);
    }
  }
  fprintf(file, "total score: %Lf\n", total_score);
  fclose(file);
}

int main(void) {
  FILE* file = fopen("data/links", "r");
  assert(file);
  fread(&NUM_ARTICLES, sizeof(int), 1, file);
  NUM_ARTICLES += 1;
  ARTICLES = calloc(NUM_ARTICLES, sizeof(Article));

  int count;
  fread(&count, sizeof(int), 1, file);

  int cited;
  while (fread(&cited, sizeof(int), 1, file)) {
    ARTICLES[cited].score = 1;

    int num_citations;
    fread(&num_citations, sizeof(int), 1, file);
    ARTICLES[cited].num_citations = num_citations;

    ARTICLES[cited].citations = malloc(sizeof(int) * num_citations);
    fread(ARTICLES[cited].citations, sizeof(int), num_citations, file);

    for (int i = 0; i < num_citations; i++) {
      ARTICLES[ARTICLES[cited].citations[i]].score = 1;
      ARTICLES[ARTICLES[cited].citations[i]].num_cited += 1;
    }
  }

  assert(feof(file));
  fclose (file);

  pthread_t threads[NUM_CORES];
  int segs[NUM_CORES];

  for (int i = 1; i < NUM_CORES; i++) {
    segs[i] = i;
    pthread_create(&threads[i], NULL, update, &segs[i]);
  }
  segs[0] = 0;
  update(&segs[0]);

  for (int i = 1; i < NUM_CORES; i++) {
    pthread_cancel(threads[i]);
  }

  write_results();
}
