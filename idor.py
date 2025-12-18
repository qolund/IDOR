import requests

with requests.session() as s:
    for i in range(0, 100):
        response = s.get("http://testphp.vulnweb.com/artists.php?artist=%s" % (str(i)))
        if "lyzae" in response.text:
            print(response.url)
