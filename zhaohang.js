const https = require('https');
//var fs = require('fs');
var cheerio = require('cheerio');
//var request = require('request');

var host = {
	hostname:'ccclub.cmbchina.com',
	port: 443,
  	path: '/mca/MQuery.aspx?WT.refp=%2Fcard-progress$',
  	method: 'GET'
}
var html = '';

const req = https.request(host, (res) => {
	  console.log('状态码：', res.statusCode);
	  console.log('请求头：', res.headers);
		
	  res.on('data', (chunk) => {
	  	html +=chunk
	  	console.log(html)
	  });
	});
	
	req.on('error', (e) => {
	  console.error(e);
	});
	
	req.on('end',()=>{
//		var $ = cheerio.load(html);
//		console.log($);
	});
