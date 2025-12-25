import requests

i = 0

with requests.session() as s :
    while True:
        response = s.get("http://testphp.vulnweb.com/artists.php?artist=%s" % (str(i)))
        if "lyzae" in response.text:
            print(f"Trouvé {response.url}")
            break
        i += 1
