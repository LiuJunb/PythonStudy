const http = require('http');
const https = require('https');
const request = require('request');

const hostname = '127.0.0.1';
const port1 = 51599;
const port2 = 51588;

// 创建一个 API 代理服务
const apiServer = http.createServer((req, res) => {
  const url = 'https://httpbin.org/get';
  console.log(req.url);
  const options = {
    url: url
  };

  function callback (error, response, body) {
    if (!error && response.statusCode === 200) {
      // 设置编码类型，否则中文会显示为乱码
      res.setHeader('Content-Type', 'text/plain;charset=UTF-8');
      // 设置所有域允许跨域
      res.setHeader('Access-Control-Allow-Origin', '*');
      // 返回代理后的内容
      res.end(body);
    }
  }
  request.get(options, callback);
});
// http 监听 51599 端口
apiServer.listen(port1, hostname, () => {
  console.log(`接口代理运行在 http://${hostname}:${port1}/`);
});


//======================================================

const apiServers = https.createServer({},(req, res) => {
  const url = 'https://httpbin.org/get';
  console.log(req.url);
  const options = {
    url: url
  };
  console.log(url)
  function callback (error, response, body) {
    if (!error && response.statusCode === 200) {
      // 设置编码类型，否则中文会显示为乱码
      res.setHeader('Content-Type', 'text/plain;charset=UTF-8');
      // 设置所有域允许跨域
      res.setHeader('Access-Control-Allow-Origin', '*');
      // 返回代理后的内容
      res.end(body);
    }
  }
  request.get(options, callback);
});

// https监听 51588 端口
apiServers.listen(port2, hostname, () => {
  console.log(`接口代理运行在 https://${hostname}:${port2}/`);
});