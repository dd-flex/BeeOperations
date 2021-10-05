import requests
loginData = {
    "ctl00$ContentBodyBase$CustomLogin$Languages": "en",
    "ctl00$ContentBodyBase$CustomLogin$LoginButton": "Login",
    "ctl00$ContentBodyBase$CustomLogin$Password": "Haslo123",
    "ctl00$ContentBodyBase$CustomLogin$System": "flexfilm.demo",
    "ctl00$ContentBodyBase$CustomLogin$UserName": "automat1",

    "__VIEWSTATEGENERATOR": "B19C5E38",
    "__EVENTVALIDATION":"/wEdAAf8EZ+/v32ClUtiROzFd83Q3381zWkNwoq9WoKcErEmnYv5bWRkei0sVqSNvssrOhySCEVyGo2tGZrnDfiVCGsXwhQxF3sj8LvSS76boHPAs1GxssFWY+Fnwrk0XJKJAhsccjyOmRKbImHdgZkAa9ETl7LSs6zWzSP5YeQyP6iFBFeCHi8=",
    "loginData" : "userName=automat1&system=flexfilm.demo&language=en",
    "__RequestVerificationToken": "I_Kc_a-2X_N1KYL8055JcQbbw_OR3bD6RIpwUWpyISEy7y_LJJLiu6ffvRFBiqf91VS7Keh0H5Fu0pyZF9ZlnRqM17I1"
}

loginHeaders = {
    "Referer": "https://app.beeoffice.com/NeOLogin.aspx?ReturnUrl=%2fDefault.aspx",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Origin":"https://app.beeoffice.com",
    "Content-Type": "application/x-www-form-urlencoded"
}

resp = requests.Session().get("https://app.beeoffice.com/NeOLogin.aspx?ReturnUrl=%2fDefault.aspx",)

for i in resp.cookies:
    if i.name == "__RequestVerificationToken" :
        loginData["__RequestVerificationToken"] = i.value
print(loginData)


resp2 = requests.Session().post("https://app.beeoffice.com/NeOLogin.aspx?ReturnUrl=%2fDefault.aspx",cookies = resp.cookies, data = loginData, headers = loginHeaders)

print(resp2.text)
print(resp2.headers)
print(resp2)