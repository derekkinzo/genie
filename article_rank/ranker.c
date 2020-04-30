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

int main(void) {
  FILE* file = fopen("data/links", "r");
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

  pthread_t threads[NUM_CORES];
  int segs[NUM_CORES];

  for (int i = 1; i < NUM_CORES; i++) {
    segs[i] = i;
    pthread_create(&threads[i], NULL, update, &segs[i]);
  }
  segs[0] = 0;
  update(&segs[0]);

  for (int i = 0; i < NUM_CORES; i++) {
    pthread_cancel(threads[i]);
  }

  assert(feof(file));
  fclose (file);
}
