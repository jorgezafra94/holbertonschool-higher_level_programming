#!/usr/bin/python3
""" getting info from twitter API
"""
if __name__ == "__main__":
    import sys
    import requests
    import base64

    API = "https://api.twitter.com/"
    # get the costumer key and secret key
    cos_key = sys.argv[1]
    sec_key = sys.argv[2]
    # string to search
    string = sys.argv[3]
    # get the bearer key using base64 decode with cos_key and sec_key
    # first decode the cos_key and sec_key
    key_secret = '{}:{}'.format(cos_key, sec_key).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_key = b64_encoded_key.decode('ascii')
    # get bearer
    # all this steps are in
    # https://developer.twitter.com/en/docs/basics/authentication/oauth-2-0/application-only
    complete_API = API + "oauth2/token"
    headers = {
        'Authorization': 'Basic {}'.format(b64_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    data = {'grant_type': 'client_credentials'}
    r = requests.post(complete_API, headers=headers, data=data)
    # we get a 200 if all is fine print(r.status_code)
    # r.json().keys()
    access_token = r.json().get('access_token')
    # now we search the word
    se_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    se_params = {
        'q': string,
        'result_type': 'recent',
        'count': 5
    }

    se_url = '{}1.1/search/tweets.json'.format(API)
    search_resp = requests.get(se_url, headers=se_headers, params=se_params)
    # we get the answers
    tweet_data = search_resp.json()
    for x in tweet_data['statuses']:
        print("[{}] {} by {}".format(x.get('id'), x.get('text'),
                                     x.get('user').get('name')))
