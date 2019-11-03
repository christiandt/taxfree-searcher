# taxfree-searcher
Simple code to generate a database comparing airport tax-free and vinmonopolet using their respective APIs.


# Structure
- db_creator.py - create sqlite database to store values
- filedump.py - simple file to dump output to file
- main.py - file to search tax-free.no for goods, and lookup at vinmonopolet for corresponding prices
- taxfree.py - lookup taxfree products using the algoli api
- vinmonopolet.py - lookup for products using the vinmonopolet api


# Required keys
A app id and secret is needed for the algoli api with search priveliges.
An api key is needed for the vinmonopolet api with access to the "open" api.