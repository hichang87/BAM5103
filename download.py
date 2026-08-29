import requests

r = requests.get("https://github.com/pimatskku/sturdymemory/raw/refs/heads/main/dataset.zip")
open("dataset.zip", "wb").write(r.content)

