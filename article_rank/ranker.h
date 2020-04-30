#define HYDRATION 0.15
#define DEHYDRATION 0.85
#define NUM_CORES 4
#define NUM_ITERS 10

typedef struct Article {
    long double score;
    int num_citations;
    int num_cited;
    int* citations;
} Article;
