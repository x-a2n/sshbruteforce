import requests,json,os,sys
#check access_token
def main():
    if not os.path.isfile('access_token.txt'):
        print ('[info]:access_token file is not exist, please login')
        login()
    else:
      cek()
 #cek
def cek():
  os.system('clear')
  print('[!] Checking validation access_token....')
  access_token = open('access_token.txt','r').read()
  headers = {'Authorization':'JWT '+access_token,'User-Agent':'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36','Content-Type': 'application/json'}
  r = requests.get('https://api.zoomeye.org/resources-info',headers=headers)
  if r.status_code == 200:
    os.system('clear')
    print('[*] checking Success...!!')
    search()
  elif 401:
    os.system('clear')
    print('[!] Unauthorization\nPlease login again...')
    login()
  else:
    os.system('clear')
    print('[!] Error')
    login()
 #login
def login():
  sv = open('access_token.txt','w')
  user = input('Username : ')
  passwd = input('Password : ')
  data = {'username':user,'password':passwd}
  headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36','Content-Type': 'application/json'}
  api_url = 'https://api.zoomeye.org/user/login'
  try:
    r_login = requests.post(api_url,data=json.dumps(data),headers=headers)
    r_decode = json.loads(r_login.text)
    token = r_decode['access_token']
    os.system('clear')
    sv.write(token)
    print('[*] Login success...')
    search()
  except:
    exit('[!]Invalid username or password')
#search
def search():
  sv = open('hasil.txt','a')
  qsearch = str(input('Search : '))
  print('[!]Page ex: 1-??')
  page = int(input('Page : '))
  for s in range(page):
    s +=1
    access_token = open('access_token.txt','r').read()
    headers = {'Authorization':'JWT '+access_token,'User-Agent':'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36','Content-Type': 'application/json'}
    api_url = 'https://api.zoomeye.org/host/search'
    r_search = requests.get(api_url, headers=headers,params={'query': qsearch, 'page': s})
    r_decode = json.loads(r_search.text)
    for res in r_decode['matches']:
      ip = res['ip']
      print('%s'%(ip))
      sv.write('%s\n'%(ip))
  print('\nsuccessDone grabbing %s page'%(page))

if __name__ == '__main__':
  main()