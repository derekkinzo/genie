from csv import reader
import requests
import xmltodict
import urllib.parse
import re
from datetime import datetime
import csv
import concurrent.futures

# Constants
base_url = "https://www.ncbi.nlm.nih.gov/pmc"
converter_path = "/utils/idconv/v1.0/?tool=my_tool&email=my_email@example.com&format=json"
retrieval_path = "/oai/oai.cgi?verb=GetRecord&metadataPrefix=pmc_fm&identifier=oai:pubmedcentral.nih.gov:"
api_key = "9ab4b04dcabcab740d1a297e6f3f54aa1e09"
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
dateTimeObj = datetime.now().__str__()
batch_size = 10
csv_file = "pubmed_id.csv"


def find(term, dictionary):
    for k, v in dictionary.items():
        if k == term:
            yield dictionary
        elif isinstance(v, dict):
            for result in find(term, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, dict):
                    for result in find(term, d):
                        yield result


def email_lookup(pubmed_ids):
    out_csv_file = "author_info_emails.csv"
    email_dict = dict()

    with open(out_csv_file, 'a') as csvfile:
        for pubmed_id in pubmed_ids:
            params_converter = {
                'ids': pubmed_id,
                'api_key': api_key
            }

            convert_request = requests.get(url=base_url + converter_path, params=params_converter)
            converted_data = convert_request.json()

            if list(find("errmsg", converted_data)):
                # ID not found in Pub med
                continue
            else:
                pmc_id = converted_data['records'][0]['pmcid']
                decoded_url = urllib.parse.unquote(base_url + retrieval_path + pmc_id[3:])

                retrieval_request = requests.get(url=decoded_url)

                retrieval_data = xmltodict.parse(retrieval_request.content)

                email_obj = list(find("email", retrieval_data))
                email_set = set()

                # Email could exist anywhere or everywhere up till 4th nested level
                # This is being done to get the max emails data extraction from the pubmed ids
                if email_obj:
                    if isinstance(email_obj, list) | isinstance(email_obj, dict):
                        for entry in email_obj:
                            if isinstance(entry, dict):
                                for value in entry.values():
                                    if isinstance(value, dict):
                                        for v1 in value.values():
                                            if EMAIL_REGEX.match(str(v1)):
                                                if str(v1).startswith('mailto:'):
                                                    v1 = str(v1)[7:]
                                                email_set.add(str(v1))
                                    if isinstance(value, list):
                                        for v2 in value:
                                            if isinstance(v2, dict):
                                                for v3 in v2.values():
                                                    if EMAIL_REGEX.match(str(v3)):
                                                        if str(v3).startswith('mailto:'):
                                                            v3 = str(v3)[7:]
                                                        email_set.add(str(v3))
                                            else:
                                                if EMAIL_REGEX.match(str(v2)):
                                                    email_set.add(str(v2))
                                    elif isinstance(value, dict):
                                        for v4 in value.values():
                                            if EMAIL_REGEX.match(str(v4)):
                                                if str(v4).startswith('mailto:'):
                                                    v4 = str(v4)[7:]
                                                email_set.add(str(v4))
                                    else:
                                        if EMAIL_REGEX.match(str(value)):
                                            email_set.add(str(value))
                            else:
                                if EMAIL_REGEX.match(str(entry)):
                                    email_set.add(str(entry))

                    # print(str(pubmed_id) + ", " + str(email_set))

                    for address in email_set:
                        email_dict.update({str(address): str(pubmed_id)})

                    csv_file_writer = csv.writer(csvfile)
                    for key, value in email_dict.items():
                        csv_file_writer.writerow([key, str(value)])
                    email_dict.clear()
        csvfile.close()


def main():
    with open(csv_file, 'r') as read_obj:
        csv_reader = reader(read_obj)
        pubmed_ids = list(csv_reader)
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        
        result = executor.map(email_lookup, pubmed_ids)
        print(result)


if __name__ == '__main__':
    main()
