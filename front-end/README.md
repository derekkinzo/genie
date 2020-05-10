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
`python3 app.py`
