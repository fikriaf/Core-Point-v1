import time, sys, json, random
from requests import post, get


def CekPlag(tex):
    url_cookies = "https://papersowl.com/free-plagiarism-checker"
    baca=open('ua.txt', 'r').read().splitlines()
    ua_acak=random.choice(baca)
    head_cookies = {
        "Host" : "papersowl.com",
        "user-agent": ua_acak,
    }

    req_cookies = get(url_cookies, headers=head_cookies).cookies
    cook  = []
    for cookie in req_cookies:
        cook.append(f"{cookie.name}={cookie.value}")

    cookies = ";".join(cook)
    text = tex.replace("\n", " ").replace(", ", "%2C+").replace("", "+")
    url_plagiarisme = "https://papersowl.com/plagiarism-checker-send-data"
    """
    head_plag = {
        "Host" : "papersowl.com",
        "user-agent": ua_acak,
        "origin": "https://papersowl.com",
        "referer": "https://papersowl.com/plagiarism-checker-send-data",
        "cookie": cookies+";device_type_pwa=0;sbjs_migrations=1418474375998%3D1;sbjs_current_add=fd%3D2023-10-01%2023%3A03%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker%7C%7C%7Crf%3D%28none%29;sbjs_first_add=fd%3D2023-10-01%2023%3A03%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker%7C%7C%7Crf%3D%28none%29;sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29;sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29;sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20U%3B%20Android%2011%3B%20zh-CN%3B%20Infinix%20X662%20Build%2FMRA58K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Version%2F4.0%20Chrome%2F92.0.4515.131%20HiBrowser%2Fv2.6.3.1%20UWS%2F%20Mobile%20Safari%2F537.36;sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker;_fbp=fb.1.1696176233911.1486632952;_hjSessionUser_265290=eyJpZCI6IjI2ODFkZTAwLTJhMjgtNTVhYi1iNmYwLTA3OGE0MzVmMzJmNiIsImNyZWF0ZWQiOjE2OTYxNzYyMzQ3NzUsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample_265290=1;_hjSession_265290=eyJpZCI6IjI1ZWM5YThmLWQ4MjktNDYzOC04YzY2LWQ4NDkzMWU5YzUzMCIsImNyZWF0ZWQiOjE2OTYxNzYyMzQ3ODMsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;is_arrow_tip_shown=true;COOKIE_PLAGIARISM_CHECKER_TERMS=1"
    }
    """
    head_plag = {
        "Host": "papersowl.com",
        "content-length":"2078",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": ua_acak,
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://papersowl.com",
        "referer": "https://papersowl.com/free-plagiarism-checker",
    }

    dat = {
        "is_free": "false",
        "plagchecker_locale" : "en",
        "title": "",
        "text": text
    }

    req_plag  = json.loads(post(url_plagiarisme, data=dat, headers=head_plag).text)
    return req_plag