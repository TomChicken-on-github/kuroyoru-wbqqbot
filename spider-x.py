name="nii_satoru"
from msedge.selenium_tools import EdgeOptions,Edge
#import selenium.webdriver as web
from time import sleep
from random import uniform
wait=lambda :sleep(uniform(3,7))
op=EdgeOptions()
op.use_chromium=True
if __name__ != '__main__':
    op.add_argument("--headless")
    op.add_argument("disable-gpu")
op.binary_location=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"#环境配置
driver_url=r"C:\Users\HP\AppData\Local\Programs\Python\Python36\MicrosoftWebDriver.exe"#环境配置
#browser=web.Edge()
browser=Edge(options=op,executable_path=driver_url)
browser.get(url=f"https://x.com/{name}")
browser.delete_all_cookies()
[browser.add_cookie(i) for i in [{'domain': '.x.com', 'expiry': 1764082418, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v1_/DK6JOOPBkaOQi5KDozrNA=="'}, {'domain': '.x.com', 'expiry': 1764082418, 'httpOnly': False, 'name': 'twid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'u%3D1859265756137168896'}, {'domain': 'x.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'en'}, {'domain': '.x.com', 'expiry': 1766760816, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8cf5ec9e2d12c310b0f10a1ed25685cfd39ceaa7fa133aeae93fe17ebdfa3437a38bdd0625319710ac884b936f1f44942d520e41c3cea196fa85b87fa3aafaf2e1c9f65635c3a0d017ba4ebca67e65e9'}, {'domain': '.x.com', 'expiry': 1766760816, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '8c74f2ea176c21887da619369e6aefaf59a7d5dd'}, {'domain': '.x.com', 'expiry': 1766760816, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'uLkud6QMyTdIS14FuD1cDtKRj9zStpu09h2Z5DNT'}, {'domain': 'x.com', 'expiry': 1748098414, 'httpOnly': False, 'name': 'g_state', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '{"i_l":0}'}, {'domain': '.x.com', 'expiry': 1732555386, 'httpOnly': False, 'name': 'gt', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1861060550626787406'}, {'domain': '.x.com', 'expiry': 1764082417, 'httpOnly': False, 'name': 'night_mode', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2'}, {'domain': '.x.com', 'expiry': 1732632817, 'httpOnly': True, 'name': 'att', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1-hbYsccbu61PcAcxNXrZ6PXcpNITRGsuDgqtryO6d'}, {'domain': '.x.com', 'expiry': 1764082386, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '173254638629859999'}]]
browser.refresh()
wait()
article=browser.find_elements_by_tag_name("article")[1:]
print(len(article))
imgs,spans=[],[]
for i in article:
    img=[j.get_attribute("src") for j in i.find_elements_by_tag_name("img")][1:]
    #span=[j.text for j in i.find_elements_by_tag_name("span")]
    span=[j.text for j in i.find_elements_by_xpath("//div[@lang and @dir='auto']/span")]
    imgs+=img
    spans+=span
    imgs+="^"
    spans+="^"
print(imgs,"\n",spans)

