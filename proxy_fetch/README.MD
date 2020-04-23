The proxy fetch attempts to fetch articles from google scholar at high speed.
It does this by reusing code from the scholarly package:
https://pypi.org/project/scholarly/

This package is able to process articles but not at scale because it makes requests from the same ip address and gets blocked.

So I tried to use methods from here: https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/

to use different proxies to request these search results using different ip addresses.

The files in this folder is the result of pulling available proxy servers and attempting to make requests to google scholar.

However, it did not work because all the proxies were blocked. Note: parts of the code were reused from the above two sources. Also the code commented out is from another team member who wants to get certain results if this succeeded.
