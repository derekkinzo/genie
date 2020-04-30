#define _DEFAULT_SOURCE

#include <math.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

int NUM_ARTICLES;

int main(void) {
  FILE* file = fopen("data/links", "r");
  fread(&NUM_ARTICLES, sizeof(int), 1, file);
  printf ("num articles %d\n", NUM_ARTICLES);
  int cited;
  while (fread(&cited, sizeof(int), 1, file)) {
    printf ("cited %d, ", cited);
    int num_citations;
    fread(&num_citations, sizeof(int), 1, file);
    printf ("num citations %d \n", num_citations);
    int* citations = malloc(sizeof(int) * num_citations);
    fread(citations, sizeof(int), num_citations, file);
  }
  assert(feof(file));
  fclose (file);
}
