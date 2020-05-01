page ranking 30 million pubmed articles using google's page rank algorithm:
https://www.cs.princeton.edu/~chazelle/courses/BIB/pagerank.htm

fetch.py fetches articles from out big query database.
write_binary.py converts articles ids to integers and saves it in data/links
ranker.c stores the articles in the array with its score and citations. It runs the page rank algorithm for NUM_ITERS iterations and writes the results in result_rankings.
This program performs about 5 iterations of page rank per second on 32 million articles with 16 cores.

pip3 install google-cloud-bigquery
scp -i ~/.ssh/google_compute_engine geraldding@35.221.27.216:/home/geraldding/genie/article_rank/data/citations.csv data/
ssh -i ~/.ssh/google_compute_engine geraldding@35.221.27.216

lldb ranker
breakpoint set --name main
breakpoint set -f ranker.c -l 16
r
