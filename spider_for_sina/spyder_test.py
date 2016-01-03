# -*- coding: UTF-8 -*-
import  requests



def login_sina_with_cookie():
	#登陆后的产生的cookie
	{'Cookie': '_T_WM=d78e8089c10b8f583eab2be0716f6d35; M_WEIBOCN_PARAMS=from%3Dhome; SUB=_2A257jTw6DeRxGeRI7lMX9CfFzziIHXVYjkRyrDV6PUJbrdAKLUj3kW0Y8kykXKtQIiEs4dAns59oCod_Rg..; gsid_CTandWM=4uyk51af1cxQwRmojonZzb7Oxfe'}

	#公孙老师的微博主页 ^_^
	url = 'http://weibo.cn/laoluoyonghao?from=home&rand=202019&vt=4'

	html = requests.get(url).content

	return html

def login_sina():
	data={'mobile':'',
		password:'',
		}
	html = requests.post(url,data = data)