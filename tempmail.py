import requests
class Client():
	def __init__(self):
		self.api="https://api.tempmail.lol/v2"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.token=None
	def create_email(self,community:str=None):
		if community:data={"community":True}
		else:data={"community":False}
		req=requests.post(f"{self.api}/inbox/create",json=data,headers=self.headers).json()
		self.token=req["token"]
		return req
	def email_indox(self,token:str=None):
		if token:token=token
		else:token=self.token
		return requests.get(f"{self.api}/inbox?token={token}",headers=self.headers).json()
	def stats_email(self):
		return requests.get(f"{self.api}/stats",headers=self.headers).json()