#define HYDRATION 0.15
#define DEHYDRATION 1 - HYDRATION

typedef struct Article {
    long double score;
    int num_citations;
    int* citations;
} Article;
