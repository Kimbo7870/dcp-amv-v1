import requests
import os
from conf import RUN_DIR

import time
start = time.time()


output_run_path = os.path.join(RUN_DIR, 'run1')

url_list = []
url_list.append(("https://files.catbox.moe/cdf1hm.webm", "attack"))
url_list.append(("https://files.catbox.moe/c7wtd4.webm", "family"))
url_list.append(("https://files.catbox.moe/ef2ntg.webm", "ds"))
url_list.append(("https://files.catbox.moe/hfybji.webm", "work"))
# url_list.append(("https://files.catbox.moe/p5bjvw.webm", "one"))
# url_list.append(("https://files.catbox.moe/ya38xy.webm", "dogs"))
# url_list.append(("https://files.catbox.moe/2f4860.webm", "haikyu"))
# url_list.append(("https://files.catbox.moe/dcu52b.webm", "creators"))

for url in url_list:
    response = requests.get(url[0])
    with open(os.path.join(output_run_path, f"{url[1]}.mp4"), "wb") as f:
        f.write(response.content)

print(time.time() - start)