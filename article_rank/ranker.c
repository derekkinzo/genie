#define _DEFAULT_SOURCE

#include <math.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "ranker.h"

int NUM_ARTICLES;
int MAX_ID;
Article* ARTICLES;

int main(void) {
  FILE* file = fopen("data/links", "r");
  fread(&MAX_ID, sizeof(int), 1, file);
  fread(&NUM_ARTICLES, sizeof(int), 1, file);
  ARTICLES = calloc(MAX_ID, sizeof(Article));

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
    }
  }

  assert(feof(file));
  fclose (file);
}
