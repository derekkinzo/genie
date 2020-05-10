Prerequisites
=============
Hosting this application requires python3, pip3 and postgresql

If you don't have postgresql on MAC run
---
```
brew install postgresql
brew services start postgresql
psql postgres
```

Setup and start server
-----
This application runs on postgresql and python flask.
1. Run `sh setup.sh` to setup postgresql and flask dependencies. This will install postgresql on linux.
2. go to http://0.0.0.0:5000/

To start the server after initial setup:
python3 app.py