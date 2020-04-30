#define _DEFAULT_SOURCE

#include <math.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "ranker.h"

int NUM_ARTICLES;
Article* ARTICLES;

void update() {
  for (int i = 0; i < NUM_ARTICLES; i++) {
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

int main(void) {
  FILE* file = fopen("data/links", "r");
  fread(&NUM_ARTICLES, sizeof(int), 1, file);
  NUM_ARTICLES += 1;
  ARTICLES = calloc(NUM_ARTICLES, sizeof(Article));

  int count;
  fread(&count, sizeof(int), 1, file);
  printf("Number of articles: %d\n", count);

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

  for (int i = 0; i < 1000; i++) {
    update();
    printf("Iteration: %d\n", i);
  }

  assert(feof(file));
  fclose (file);
}
