import hashlib
import requests
import requests
import time
import hashlib
import json
import copy

import random

def I(t=None):
    if t is not None:
        # Generate a random hex digit similar to JavaScript's XOR and random logic
        return hex(int(t) ^ int(16 * random.random()))[2:]
    else:
        # Base UUID-like string
        base_string = "10000000-1000-4000-8000-100000000000"
        
        # Replace 0, 1, and 8 with random hexadecimal values by recursively calling I
        return ''.join([I(int(char)) if char in '018' else char for char in base_string])

# Generate a sample result
sample_result = I()
print(sample_result)



t = int(time.time() * 1000)
# Simulating o.token (undefined in JavaScript is treated as 'undefined' string)
o_token = 'undefined'


session = requests.Session()

# Parameters
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
sign = hashlib.md5(sign_string.encode('utf-8')).hexdigest()

# Set the calculated sign
params['sign'] = sign

print(params)

# Headers
headers = {
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'mtop_partitioned_detect=1',
    'pragma': 'no-cache',
    'referer': 'https://bigsale.tmall.com/',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
}

# Make the request
response = session.get(url, params=params, headers=headers)

mh5_tk_cookie = response.cookies.get('_m_h5_tk')

print(mh5_tk_cookie)

mh5_tk_cookie = mh5_tk_cookie.split('_')[0]


t = int(time.time() * 1000)
# Define the URL and parameters
url = 'https://h5api.m.tmall.com/h5/mtop.gaia.nodejs.gaia.arkact.handler/1.0/'

couponid = "9655997500"


data_dict = {
    "url": "https://bigsale.tmall.com/wow/a/act/haiwaifenzu/tmc/42015/23826/wupr",
    "cookie": "hng=TW|zh-TW|TWD|158",
    "device": "phone",
    "backupParams": "excludes,device",
    "usePrefetch": False,
    "fri": {
        "dtcUrl": "https://bigsale.tmall.com/wow/a/act/haiwaifenzu/tmc/42015/23826/wupr?wh_pid=main-542564&disableNav=YES&status_bar_transparent=true",
        "dtcFloor": ["8528522200", "4746775570", "3713732880"],
        "moduleIdList": ["6324963840",couponid],
        # "moduleIdList": ["6324963840", "5504341500", "3487070410", "9421648050", "6335955830", "1786158660", "4934247680", "9655997500", "1622330850", "9741161900", "3436597850", "1493721000", "3896910660", "5660165920", "6615946390", "4504955890", "5947324100", "7318323820", "2562439000", "6917991150", "5805324930", "7193295690", "2394361710", "1969575660", "8931034440", "1376557220", "6882844360", "5123689340", "4014336740", "3389459780", "2459064100"],
        "processedTppId": []
    },
    "excludes": "1786158660;3487070410;4934247680;5504341500;6324963840;6335955830;9421648050",
    "pvuuid": f"v1-{I()}-{t}",
    "schemaVersion": "96ce985c-21e9-40f6-8dfe-437486cd6e8c",
    "sequence": 2
}

# Encode the Python dictionary back to a JSON string
json_string = json.dumps(data_dict)


da = copy.copy(data_dict)
da['fri'] = json.dumps(data_dict['fri'])
da = json.dumps(da)
print(da)

# Define the query parameters
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

md5ha = (mh5_tk_cookie + "&" + str(t) + "&" + params['appKey'] + "&" + params['data']);
md5_hash = hashlib.md5()
md5_hash.update(md5ha.encode('utf-8'))
res = md5_hash.hexdigest()
params['sign'] = res
print(res)


# print(md5ha)
# Define the headers
headers = {
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://bigsale.tmall.com/',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
}

# %%
response = session.get(url, headers=headers, params=params)

# %%
print(response.text)

# %%
rrrr = response.text[20:-1]

# %%
r = json.loads(rrrr)

# %%
print(r['data']['resultValue']["data"]["9655997500"])
