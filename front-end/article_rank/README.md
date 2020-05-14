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
```python
for article in articles:
	score = 0.15
	for citation in article.citations:
		flow_from_citation = 0.85 * citation.score / citation.cited_articles
		score += flow_from_citation
	article.score = score
```
And that’s it! If we run the above code a few times it will converge!

Pseudocode Analogy
------------------
```python
# first we calculate how much water is flowing into each article
for article in articles:
	# score is how much water it is getting from rain
	score = 0.15
	for citation in article.citations:
		# flow from citation is how much lake citation is flowing into the lake article. citation.score is the volume of water in lake citation. We divide by citation.cited_articles because citation’s water is flowing into citation.cited_article lakes equally. We multiply by 0.85 because 15% of water is evaporated into rain.
		flow_from_citation = 0.85 * citation.score / citation.cited_articles
		# next we just sum up all the water flowing into lake article from other lakes
		score += flow_from_citation
	article.score = score
```

Overview
----------------
This program requires a database of articles ids as well as the citation article ids for each article. An example row looks like this:
1234567, 23456, 5678, 982384

Where the first column is the id of the pubmed article being cited. The following columns are ids of articles that cite article 1234567. We gathered pubmed citation information as a separate task and stored them in a bigquery table called harvard-599-trendsetters.pubmed.pubmed_citation (please see fetch.py).

Therefore, the input of this program are tables likes this:
1234567, 23456, 5678, 982384
23456, 23124, 92383, 2324, 2314124, 1232

Whereas the output of the program looks like the following:
18156677,1512.463756,27466
14907713,568.630309,52368
5432063,433.904656,53474
942051,291.640087,42760
19171970,255.677059,7377
271968,227.256398,22352
2231712,199.411086,24459

Where the first column is the article id. The second column is the page rank of that article. The third column is the number of articles. The rows are sorted by page rank descending. Notice that the highest ranked article does not have the highest number of citations. This is due to the fact each citation is weighted differently and having more citations does not mean higher importance of the citations.

Procedure
---------
Here are the steps for completing this task. Please use python3 to run the python files and pip3 to install any required dependencies.

1. Obtain a google service account key in order to fetch data from our bigquery table. First, go to https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#client-libraries-install-python and follow the "Before You Begin" section to obtain a json file with your google cloud service account credentials. Next place the json file in the same folder as this README file and name the file service-account.json. Next obtain permission to pull data from our big query table with your service-account.json file. Finally, run `pip3 install google-cloud-bigquery` to install bigquery on python3.
1. fetch citation data from from google bigquery and write them to a csv file. Run `python3 fetch.py.`
1. convert article ids to integers and save them in binary file `links` where different rows are separated by the \n character and different columns are separated by \0 character. Run `python3 write_binary.py`. This will produce a file named `links` that contains the citations in binary format.
1. load the data from `links` and perform page rank. Store the results in `rankings` in descending order by page rank. To do this, run make in the current directory to compile the c program that accomplishes this task. Call ./ranker to run the complied program. The final results will be stored in `rankings`.
1. If you want to store the results in postgresql instead, run pubmed_ranks.sql in your local postgresql database to setup a table to store results. Refer to https://www.postgresql.org/ or the internet to setup postgresql on your machine. Run `python3 load_pubmed_ranks.py` to load results from `rankings` to a local psql table named `pubmed_ranks`

<!-- Dev commands
scp -i ~/.ssh/google_compute_engine geraldding@35.212.88.75:/home/geraldding/genie/article_rank/data/citations.csv data/
ssh -i ~/.ssh/google_compute_engine geraldding@35.221.27.216 -->

<!-- Debugging commands for ranker.code
lldb ranker
breakpoint set --name main
breakpoint set -f ranker.c -l 16
r -->
