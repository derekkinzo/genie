pip3 install google-cloud-bigquery
scp -i ~/.ssh/google_compute_engine geraldding@35.221.27.216:/home/geraldding/genie/article_rank/data/citations.csv data/

lldb ranker
breakpoint set --name main
breakpoint set -f ranker.c -l 16
r
