# import requests module
import requests
import io
  

s = requests.Session()
#s.auth = ('automat1', 'Haslo123')
payload = {
    #'ctl00$ContentBodyBase$CustomLogin$UserName':'automat1',
    #'ctl00$ContentBodyBase$CustomLogin$Password':'Haslo123',
    #'ctl00$ContentBodyBase$CustomLogin$System':'flexfilm.demo',
    #'loginData':'userName=automat1&system=flexfilm.demo&language=pl',
    #'Authorization':'YXV0b21hdDE6SGFzbG8xMjM=',
    #'ibm-mq-rest-csrf-token':'',
    #'ASP.NET_SessionId': 'srtagc0iza5wniaarnzgfv5b',
    #'__RequestVerificationToken': 'gcVRUFwlOIOdEOQoHRThdP-skGsu6aH4YyN0UC4hmPV7s3BHpwLl_Be3GcPdxmMIvMGJ3EB1viQN3fzuXQ7DyI7EGy01',
    '.ASPXAUTHBEE': '307E4230145B3703E81D43CACF1BEDD3FE2960D0D9F78F56B6761DF48812C79C651E076DB3B0215C70E6C133EE250B14A4A42C9CFF0E72783096A9E9E58EE0B49C0C22528095D6DD885D5C67BF03E5B00F32124419BCDC90770BB3E553697199413ABEB1110AA6997BFFFBD46B225110BE6A2C734789686FF28C335B25DA408FBB95C98AAB91A5B8801BAB31DAC0C30A769F63AEC17945A0E4E2772EE22958F2BBC27E70A59C38E7604874D3265240300D342A02F76CCEF3E5F278A3BD9022EF0A2430C037EB48377A0784D01FF112CEED8D8D40F1F2A79CFD9C07306B92BF81CC21BF98',
    'Accept':'text/json',
    'Referer': "https://app.beeoffice.com/swagger/ui/index"
    }
r = requests.get('https://app.beeoffice.com/api/utils/whoiam', data=payload, headers={'.ASPXAUTHBEE': '307E4230145B3703E81D43CACF1BEDD3FE2960D0D9F78F56B6761DF48812C79C651E076DB3B0215C70E6C133EE250B14A4A42C9CFF0E72783096A9E9E58EE0B49C0C22528095D6DD885D5C67BF03E5B00F32124419BCDC90770BB3E553697199413ABEB1110AA6997BFFFBD46B225110BE6A2C734789686FF28C335B25DA408FBB95C98AAB91A5B8801BAB31DAC0C30A769F63AEC17945A0E4E2772EE22958F2BBC27E70A59C38E7604874D3265240300D342A02F76CCEF3E5F278A3BD9022EF0A2430C037EB48377A0784D01FF112CEED8D8D40F1F2A79CFD9C07306B92BF81CC21BF98',
    'Accept':'text/json',
    'Referer': "https://app.beeoffice.com/swagger/ui/index"})#, auth = ('automat1', 'Haslo123') )
respfile = io.open("index.html", "w", encoding="utf-8")
respfile.write(r.text)
respfile.close
print(r.text)
print(r)
