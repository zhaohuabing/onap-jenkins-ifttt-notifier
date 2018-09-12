import requests

url = 'https://jenkins.onap.org/view/msb/'
src = requests.get(url)
src.encoding = 'utf-8'
html = src.text

if html.find("icon-red") >=0:
    report = {}
    report["value1"] = "https://jenkins.onap.org/view/msb/"
    requests.post("https://maker.ifttt.com/trigger/your_maker_event/with/key/your_ifttt_api_key", data=report)
