#define HYDRATION 1
#define DEHYDRATION 0.9
#define NUM_CORES 16
#define NUM_ITERS 20

typedef struct Article {
  long double score;
  int num_citations;
  int num_cited;
  int* citations;
} Article;

typedef struct Result {
  int index;
  long double score;
} Result;
