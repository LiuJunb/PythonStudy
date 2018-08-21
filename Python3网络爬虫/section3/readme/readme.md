# 不验证SSL

    import ssl
    
    # 2.设计urllib 不进行证书验证
    context = ssl._create_unverified_context()
    
    # 3.百度的https就是一个重新加载HTTP而已，<noscript></noscript>就是对不支持javascript的浏览器的一个支持，采用refresh的方法，还是重定向到http了
    response = urllib.request.urlopen('https://www.baidu.com', context=context)

# 全局不验证SSL

    import ssl
    # 第二种配置全局的 不验证ssl
    ssl.create_default_context = ssl._create_unverified_context
    
# 代理

    # 这个代理要起作用必须要手动：实现对下面ip和端口的监听
    proxy_handler = ProxyHandler({
         'http': 'http://127.0.0.1:51599',
         'https': 'https://127.0.0.1:51599'
    })
    c = ssl._create_unverified_context()
    s = HTTPSHandler(context=c)
    opener = build_opener(s, proxy_handler)
    
    resposne = opener.open('http://httpbin.org/get')
    print(resposne.read().decode('utf-8'))    

## 错误信息HTTPConnectionPool

* 错误信息：equests.exceptions.ConnectionError: HTTPConnectionPool(host='www.zssfgfgdfgdfdgdfgdsdfhu.com', port=80): Max retries exceeded with url: /exp/expl
* 错误图片：
![](https://note.youdao.com/yws/public/resource/2c69ccd7c071e122aada0d09d6a84867/xmlnote/67BABBA9726640AAB7C1AA79F31796E7/3679)