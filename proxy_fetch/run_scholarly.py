from scholarly import *
import csv
import os
import pdb

with open("articles.csv", "r") as results_file:
    reader = csv.reader(results_file)
    next(reader)
    for row in reader:
        pdb.set_trace()
        paper_search_query = search_pubs_query(row[1])
        paper_result = next(paper_search_query)
        pdb.set_trace()
#
# results = query_job.result()
# for row in results:
#     results = scholarly.search_pubs_query('dremel')
#     print
#     print(results)
# with open('output_subset.csv') as f:
#     articles = [line.strip().split(',') for line in f]
#
# pmid_titles = [(article[0], article[1]) for article in articles]
#
# n=0
#
# for pmid, title in pmid_titles[0:3]:
# 	# try:
#     print(title)
#     title_test='dremel'
#     pdb.set_trace()
#     paper_search_query = scholarly.search_pubs_query('dremel')
#     print(paper_search_query)
#     paper_result = next(paper_search_query)
#     print(paper_result)
#     # Extract data from result of paper metadata
#     paper_citation_count = paper_result.citedby
#     paper_abstract = paper_result.bib['abstract']
#     paper_primary_author = paper_result.bib['author'].split(' and ')[0] # First author only.
#
#     author_query = scholarly.search_author(paper_primary_author)
#     author_result = next(author_query).fill()
#
#     # Extract data from result of author metadata
#     author_citation_count = author_result.citedby
#     author_citation_by_year = author_result.cites_per_year
#     author_affiliation = author_result.affiliation
#     author_email = author_result.email
#     author_id = author_result.id
#     author_name = author_result.name
#     author_pub_count = len(author_result.publications)
#     author_hindex = author_result.hindex
#     author_hindex5y = author_result.hindex5y
#     author_i10index = author_result.i10index
#     author_i10index5y = author_result.i10index5y
#     author_interests = author_result.interests
#
#     data_to_write = [[
# 		pmid,
#         paper_citation_count,
#         paper_abstract,
#         paper_primary_author,
#         author_citation_count,
#         author_citation_by_year,
#         author_affiliation,
#         author_email,
#         author_id,
#         author_name,
#         author_pub_count,
#         author_hindex,
#         author_hindex5y,
#         author_i10index,
#         author_i10index5y,
#         author_i10index5y,
#         author_interests
#         ]]
#
#     with open('author_metadata.csv','a') as result_file:
#         wr = csv.writer(result_file)
#         wr.writerows(data_to_write)
