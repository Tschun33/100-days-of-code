from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.amazon.de/HUAWEI-intelligenter-Ger%C3%A4uschunterdr%C3%BCckung-3-Mikrofon-System"
                 "-Schnellladung-Silver-Frost/dp/B08GPTC52S/?_encoding=UTF8&pd_rd_w=TGKTM&content-id=amzn1.sym"
                 ".41b7e53c-0745-4c02-89a0-d1731ab85153&pf_rd_p=41b7e53c-0745-4c02-89a0-d1731ab85153&pf_rd_r"
                 "=2YW6QMV176N7YZVZT7WW&pd_rd_wg=C1WvV&pd_rd_r=61880958-f832-4c9b-8032-c63492770180&ref_"
                 "=pd_gw_ci_mcx_mr_hp_atf_m")
page_text = r.text
soup = BeautifulSoup(page_text, "html.parser")
print(soup.prettify())

price = soup.find(class_="a-price-whole")

print(price)