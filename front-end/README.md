Prerequisites
=============
Supports MacOS and linux
Hosting this application requires python3, pip3 and postgresql

Mac Users
---------
If you don't have postgresql on MAC run
---
```
brew install postgresql
brew services start postgresql
psql postgres
```

Please verify that `psql postgres` works before proceeding

If you don't have python3 run
`brew install python3`

Please verify that `python3` and `pip3` works before proceeding

Linux Users
-----------
Your operating system should have python3 already. You should be able to proceed to the next step.

Setup and start server
-----
This application runs on postgresql and python flask.
1. Run `bash setup.sh` to setup postgresql and flask dependencies. This will install postgresql on linux.
2. go to http://0.0.0.0:5000/

To start the server after initial setup:
`bash app.sh`

Getting Data
------------
If you tried to run the server, there is probably no data. In order to get data from our big query table, please obtain a google service account key.

First, go to https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#client-libraries-install-python and follow the "Before You Begin" section to obtain a json file with your google cloud service account credentials. Next place the json file in the front-end folder and name the file `service-account.json`. Next obtain permission to pull data from our big query table with your service account key.

Run `python3 loader/fetch_relationships.py` to fetch the main table from bigquery. Keep in mind that there may be millions of articles and each fetch could take some time.

After the fetch is complete, run `python3 app.py` and you should see data in the table.

You can also run any combination of the following commands to get data for supporting tables.
```
python3 loader/fetch_journals.py
python3 loader/fetch_paper_links.py
python3 loader/pubs.py
python3 loader/fetch_sjr.py
```

Genie Page Rank
---------------
Finally, you can upgrade from citation ranking to page ranking pubmed articles by running `bash article_rank/setup.sh`. Keep in mind this can take up to 30 minutes since there are 30 million records.
