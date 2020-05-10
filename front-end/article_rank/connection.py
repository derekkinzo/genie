import os
import psycopg2
import pdb

connection = psycopg2.connect(host = "localhost", port = "5432", database = "genie", user = "genie", password = "genie123")
