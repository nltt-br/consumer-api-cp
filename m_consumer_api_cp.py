import requests, json
    
class MainConsumerApiCp:

    def __init__(self, api_user, api_password, domain, ip_ws):
        self._api_user = api_user
        self._api_password = api_password
        self._domain = domain
        self._ip_ws = ip_ws

    def api_call_mod(self, path, json_data, sid):
        if sid == '':
            request_headers = {'Content-Type' : 'application/json'}
        else:
            request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
        r = requests.post(path, data=json.dumps(json_data), headers=request_headers, verify=False)
        return r.json()

    def api_login(self):
        path = self.url_web_server("login")
        data = {'user':self._api_user, 'password':self._api_password, 'domain':self._domain}
        response = self.api_call_mod(path, data, '')
        return response["sid"]

    def url_web_server(self, payload):
        str_url = 'https://{}/web_api/{}'.format(self._ip_ws, payload)
        return str_url

    def publish(self):
        url_publish = self.url_web_server("publish")
        return url_publish

    def logout(self):
        url_logout = self.url_web_server("logout")
        return url_logout    

    def add_host_group(self, hostname, group, ip_src):
        sid = self.api_login()
        url = self.url_web_server("add-host")
        data = {"name":hostname, "ip-address":ip_src, "groups":group}
        self.api_call_mod(url, data, sid)
        self.api_call_mod(self.publish(), {}, sid)
        self.api_call_mod(self.logout(), {}, sid)

    def install_policy_access(self, policy_pkg, target):
        sid = self.api_login()
        url = self.url_web_server("install-policy")
        data = {"policy-package":policy_pkg, "targets":target "access":"true", "desktop-security":"false", "qos":"false", "threat-prevention":"false"}
        self.api_call_mod(url, data, sid)
        self.api_call_mod(self.logout(), {}, sid)

def teste:

