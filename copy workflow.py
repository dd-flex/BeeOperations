import requests
import json
##############
aspxAuthBeeCookie = '307E4230145B3703E81D43CACF1BEDD3FE2960D0D9F78F56B6761DF48812C79C651E076DB3B0215C70E6C133EE250B14A4A42C9CFF0E72783096A9E9E58EE0B49C0C22528095D6DD885D5C67BF03E5B00F32124419BCDC90770BB3E553697199413ABEB1110AA6997BFFFBD46B225110BE6A2C734789686FF28C335B25DA408FBB95C98AAB91A5B8801BAB31DAC0C30A769F63AEC17945A0E4E2772EE22958F2BBC27E70A59C38E7604874D3265240300D342A02F76CCEF3E5F278A3BD9022EF0A2430C037EB48377A0784D01FF112CEED8D8D40F1F2A79CFD9C07306B92BF81CC21BF98'
# - TU WKLEJ COOKIE - ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    
srcPNum = "69420"
destPNums = "14049"
############

#import io # jeszcze nieużywane
attr = "personal_number"

s = requests.Session() 
r = s.get('https://app.beeoffice.com/api/employees/'+ attr +'%3BADD%3Beq%3B' + srcPNum + '/1',
    data={'.ASPXAUTHBEE': aspxAuthBeeCookie},
    headers={'Accept':'application/json',
    'Referer': "https://app.beeoffice.com/swagger/ui/index"})
respJson = json.loads(r.text)
srcID=respJson[0]['ID']
print(srcID)
r2 = s.get('https://app.beeoffice.com/api/employees/'+ attr +'%3BADD%3Beq%3B' + destPNums + '/1',
    data={'.ASPXAUTHBEE': aspxAuthBeeCookie},
    headers={'Accept':'application/json',
    'Referer': "https://app.beeoffice.com/swagger/ui/index"})
resp2Json = json.loads(r2.text)
destID=resp2Json[0]['ID']

r3 = s.get('https://app.beeoffice.com/api/employees/'+ attr +'%3BADD%3Beq%3B' + srcPNum + '/1',
    data={'.ASPXAUTHBEE': aspxAuthBeeCookie},
    headers={'Accept':'application/json',
    'Referer': "https://app.beeoffice.com/swagger/ui/index"})