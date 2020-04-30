#define _DEFAULT_SOURCE

#include <math.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

int main(void) {
  FILE* file = fopen("data/links", "r");
  int i = 0;
  fread(&i, sizeof(int), 1, file);
  getc(file);
  assert(feof(file));
  printf ("%d ", i);
  fclose (file);
}
