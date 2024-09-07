import hashlib
import requests
import time
import random
import json
import copy

# Function to generate a random hex string or UUID-like string
def I(t=None):
    if t is not None:
        # Generate a random hex digit similar to JavaScript's XOR and random logic
        return hex(int(t) ^ int(16 * random.random()))[2:]
    else:
        # Base UUID-like string
        base_string = "10000000-1000-4000-8000-100000000000"
        # Replace 0, 1, and 8 with random hexadecimal values by recursively calling I
        return ''.join([I(int(char)) if char in '018' else char for char in base_string])

# Function to calculate MD5 hash
def generate_md5_hash(data_string):
    md5_hash = hashlib.md5()
    md5_hash.update(data_string.encode('utf-8'))
    return md5_hash.hexdigest()

# Function to send request and handle response
def send_request(session, url, headers, params):
    response = session.get(url, headers=headers, params=params)
    return response

# Main script execution
if __name__ == "__main__":
    # Timestamp for 't' parameter
    t = int(time.time() * 1000)
    
    # Simulating o.token (undefined in JavaScript is treated as 'undefined' string)
    o_token = 'undefined'
    
    # Session to handle cookies
    session = requests.Session()

    # Initial parameters
    url = 'https://h5api.m.tmall.com/h5/mtop.gaia.nodejs.gaia.arkact.handler/1.0/'
    params = {
        'jsv': '2.6.1',
        'appKey': '12574478',
        't': t,
        'sign': '',  # To be calculated
        'api': 'mtop.gaia.nodejs.gaia.arkact.handler',
        'v': '1.0',
        'type': 'jsonp',
        'dataType': 'jsonp',
        'jsonpIncPrefix': 'kangaroo',
        'timeout': '5000',
        'preventFallback': 'true',
        'x-biz-type': 'ald',
        'x-biz-info': 'business=haiwaifenzu',
        'callback': 'mtopjsonpkangaroo1',
        'data': '{"url":"https://bigsale.tmall.com/wow/a/act/haiwaifenzu/tmc/42015/23826/wupr","cookie":"","device":"phone","backupParams":"device","usePrefetch":false}'
    }

    # Calculate the sign (md5 hash of o.token + "&" + t + "&" + appKey + "&" + data)
    sign_string = f"{o_token}&{params['t']}&{params['appKey']}&{params['data']}"
    params['sign'] = generate_md5_hash(sign_string)

    print(params)

    # Headers for the first request
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-TW,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'mtop_partitioned_detect=1',
        'pragma': 'no-cache',
        'referer': 'https://bigsale.tmall.com/',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    }

    # First request to get cookies
    response = send_request(session, url, headers, params)
    mh5_tk_cookie = response.cookies.get('_m_h5_tk')
    print(mh5_tk_cookie)

    # Split the _m_h5_tk cookie to get the first part
    mh5_tk_cookie = mh5_tk_cookie.split('_')[0]

    # Updated timestamp for the second request
    t = int(time.time() * 1000)

    # Coupon ID for the second request
    couponid = "9655997500"

    # Prepare data for the second request
    data_dict = {
        "url": "https://bigsale.tmall.com/wow/a/act/haiwaifenzu/tmc/42015/23826/wupr",
        "cookie": "hng=TW|zh-TW|TWD|158",
        "device": "phone",
        "backupParams": "excludes,device",
        "usePrefetch": False,
        "fri": {
            "dtcUrl": "https://bigsale.tmall.com/wow/a/act/haiwaifenzu/tmc/42015/23826/wupr?wh_pid=main-542564&disableNav=YES&status_bar_transparent=true",
            "dtcFloor": ["8528522200", "4746775570", "3713732880"],
            "moduleIdList": ["6324963840", couponid],
            "processedTppId": []
        },
        "excludes": "1786158660;3487070410;4934247680;5504341500;6324963840;6335955830;9421648050",
        "pvuuid": f"v1-{I()}-{t}",
        "schemaVersion": "96ce985c-21e9-40f6-8dfe-437486cd6e8c",
        "sequence": 2
    }

    # Copy the dictionary and adjust 'fri'
    da = copy.copy(data_dict)
    da['fri'] = json.dumps(data_dict['fri'])
    da = json.dumps(da)

    # Parameters for the second request
    params = {
        'jsv': '2.6.1',
        'appKey': '12574478',
        't': t,
        'api': 'mtop.gaia.nodejs.gaia.arkact.handler',
        'v': '1.0',
        'type': 'jsonp',
        'dataType': 'jsonp',
        'jsonpIncPrefix': 'kangaroo',
        'timeout': '5000',
        'preventFallback': 'true',
        'x-biz-type': 'ald',
        'x-biz-info': 'business=haiwaifenzu',
        'callback': 'mtopjsonpkangaroo2',
        'data': da
    }

    # Calculate the sign for the second request
    md5ha = f"{mh5_tk_cookie}&{t}&{params['appKey']}&{params['data']}"
    params['sign'] = generate_md5_hash(md5ha)

    # Headers for the second request
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://bigsale.tmall.com/',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    }

    # Second request
    response = send_request(session, url, headers, params)

    # Extract and parse the response
    response_data = json.loads(response.text[20:-1])
    print(response_data['data']['resultValue']["data"][couponid])
