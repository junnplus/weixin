# weixin-demo

> 实现『微信公众平台』的『网页授权获取用户基本信息』功能

## 流程：
- [申請測試號](http://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index)
- [接入指南](http://mp.weixin.qq.com/wiki/8/f9a0b8382e0b77d87b3bcc1ce6fbc104.html)
- 填寫授權回調頁面域名

微信文檔見 https://open.weixin.qq.com

Oauth2.0 认证使用 [@lepture](https://github.com/lepture) 的 [`Flask-oauthlib`](https://github.com/lepture/flask-oauthlib) 库。

由於微信的[Oauth2.0授權登錄](https://open.weixin.qq.com/cgi-bin/showdocument?action=dir_list&t=resource/res_list&verify=1&id=open1419316505&token=&lang=zh_CN)系統與標準的[Oauth2.0](http://oauth.net/2/)有所出入，所以擴展支持微信的Oauth2.0登錄，感謝[@tonyseek](https://github.com/tonyseek)提供的[代碼片段](https://gist.github.com/tonyseek/c31557e70065948a849d)參考。
