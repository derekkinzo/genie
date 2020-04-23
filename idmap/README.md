idmap basically maps each article in our data base to all the genes in our database that it mentions.

gene_processor.py takes all the genes and synonyms from genes.csv (from our database) and filter out the ones that are not english words and stores them in a file.

dictionary.py then builds these genes into a trie dictionary.

lastly, idmap.py pulls each article from our database, for each article abstract, for each character in the abstract, it check all possible substrings starting from that character whether it is part of the dictionary. This is basically constant time lookup for each letter in the article since it is a trie lookup. As a result, it can process 300000 articles abstract per minute on a basic cloud machine.

note: running idmap.py requires credentials to access our database

scp -i google_compute_engine geraldding@35.236.238.216:/home/geralddzx/genie/idmap/data/abstract_genes.csv .
