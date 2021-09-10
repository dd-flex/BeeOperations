<<<<<<< Updated upstream
from http.client import HTTPSConnection
from base64 import b64encode
#This sets up the https connection
c = HTTPSConnection("app.beeoffice.com")
#we need to base 64 encode it 
#and then decode it to acsii as python 3 stores it as a byte string
userAndPass = b64encode(b"automat1:Haslo123").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass,}
#then connect
c.request('GET', '/api/utils/whoiam?org=flexfilm.demo', headers=headers)
#get the response back
res = c.getresponse()
# at this point you could check the status etc
# this gets the page text
data = res.read()
print(data)  
=======
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
    'ASP.NET_SessionId': 'srtagc0iza5wniaarnzgfv5b',
    '__RequestVerificationToken': 'gcVRUFwlOIOdEOQoHRThdP-skGsu6aH4YyN0UC4hmPV7s3BHpwLl_Be3GcPdxmMIvMGJ3EB1viQN3fzuXQ7DyI7EGy01',
    '.ASPXAUTHBEE': '79A837C0CACB9FE688746490EB8E01079B1255AAC754E47DB06CAE83FA4CDBBE217E6CC9ACF77EC40764B8F0F06E5CF16ABC80C737735FAA21C765E072BEE8C28830258055481AB0C8D32524B7C5D9FCACF2892E1A497BECF2E2CC9317135E0F0679694330629BF790AC8A9D5E1B7091565751AA365D1A7570E4E348D973A7E3A1FDFB24D5322F2D18F98536ACEECFE69DCC0AD71A4FC89083FAE588380C10735EACC31FB4A7B67B211288E28772F191AB6A430A7978E5D775D3C35AD3C6ABD6458203CEABA97E802E220300F4736F3DF73423080AFCFF70CC3C6ADCD2C105E4AB0C410E',
    'Accept':'text/json'
    }
r = s.get('https://app.beeoffice.com/api/utils/whoiam', data=payload)#, auth = ('automat1', 'Haslo123') )
respfile = io.open("index.html", "w", encoding="utf-8")
respfile.write(r.text)
respfile.close
print(r.text)
>>>>>>> Stashed changes
