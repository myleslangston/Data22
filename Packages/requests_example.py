import requests  # a package allows you to package up some code and use it somewhere else.

request_bbc = requests.get("https://www.bbc.co.uk/")

print(request_bbc.content)  # gets all the info from the BBC website.

