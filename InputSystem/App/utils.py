import base64
import hashlib
import time

import requests


def myBase64(mstr):
    encode_mstr = base64.standard_b64encode(mstr.encode('utf-8')).decode('utf-8')
    return encode_mstr


def get_verify_code(phone):
    url = 'https://api.netease.im/sms/sendcode.action'

    nonce = hashlib.new('sha512', str(time.time()).encode('utf-8')).hexdigest()

    current_time = str(int(time.time()))

    sha1 = hashlib.sha1()
    app_secret = '55be64f746c8'
    sha1.update((app_secret + nonce + current_time).encode('utf-8'))
    check_sum = sha1.hexdigest()

    headers = {
        'AppKey': '96debd9499ef67f1f8881c2b397aff04',
        'Nonce': nonce,
        'CurTime': current_time,
        'CheckSum': check_sum
    }

    post_data = {
        'mobile': phone
    }

    resp = requests.post(url, data=post_data, headers=headers)
    return resp
