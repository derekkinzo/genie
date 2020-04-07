import gzip
import shutil
import os
from pubmed import ArticleSetParser, PubMedArticle
from time import time


current_path = os.path.dirname(os.path.realpath(__file__))

input_dir: [str] = os.path.join(current_path, 'input')
output_dir: [str] = os.path.join(current_path, 'output')


def unzip_article_set(file_path: str, output_file: str):
    with gzip.open(file_path, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


id_interval = 10000
curr_interval = id_interval
article_buffer: [PubMedArticle] = []
for filename in os.listdir(input_dir):
    if not filename.endswith('.gz'):
        continue
    print(f'Currently processing {filename}')
    t_start = time()
    file_path = os.path.join(input_dir, filename)
    xml_path = file_path.replace('.gz', '')
    if not os.path.exists(xml_path):
        unzip_article_set(file_path, xml_path)

    article_list = ArticleSetParser.extract_articles(xml_path)

    for article in article_list:
        curr_pmid = int(article.pmid)
        if curr_pmid > curr_interval:
            ArticleSetParser.serialize_articles(article_buffer, os.path.join(
                output_dir, str(curr_interval) + '.json'))
            article_buffer = []
            curr_interval += id_interval
        article_buffer.append(article)

    print(time() - t_start)

if len(article_buffer) > 0:
    ArticleSetParser.serialize_articles(article_buffer, os.path.join(
        output_dir, str(curr_interval) + '.json'))
