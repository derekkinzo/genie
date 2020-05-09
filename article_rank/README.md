Genie Page Rank
===============
Builds on ideas from this website
https://www.cs.princeton.edu/~chazelle/courses/BIB/pagerank.htm

Background
----------
There are 30 million articles on pubmed. Each article references a number of other articles. To determine which article is important, genie uses the page rank algorithm to rank articles. Page rank is the algorithm developed by google to rank websites on the internet.

Concept
-------
One way to rank the articles is to count the number of citations for that article, the more citations an article has, the more articles reference that article, therefore, the more important that article should be.

However, some articles are more important than others, and their reference should be worth more. As an analogy, if us.gov links to your website, that should give your website more value than if areallylongwebsitename.com is linked to your website. Therefore, simply counting the number of citations is not sufficient. There needs to be a way to give more weight to references from important articles.

Page Rank Analogy
-----------------
Imagine there are a number of interconnected lakes. Due to the difference in elevation, the water from each lake will flow into a number of connected lakes located in lower elevation. Occasionally, it will also rain, so some water from all lakes will become rain and hydrate all the lakes. Even lakes at the highest elevation will still remain hydrated by rain even though no lakes flow into them. In the long run, the volume of water in each lake is the page rank of that lake.

Pseudocode
----------
for article in articles:
	score = 0.15
	for citation in article.citations:
		flow_from_citation = 0.85 * citation.score / citation.cited_articles
		score += flow_from_citation
	article.score = score

And that’s it! If we run the above code a few times it will converge!

Pseudocode Analogy
------------------
// first we calculate how much water is flowing into each article
for article in articles:
	// score is how much water it is getting from rain
	score = 0.15
	for citation in article.citations:
		// flow from citation is how much lake citation is flowing into the lake article. citation.score is the volume of water in lake citation. We divide by citation.cited_articles because citation’s water is flowing into citation.cited_article lakes equally. We multiply by 0.85 because 15% of water is evaporated into rain.
		flow_from_citation = 0.85 * citation.score / citation.cited_articles
		//next we just sum up all the water flowing into lake article from other lakes
		score += flow_from_citation
	article.score = score

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
