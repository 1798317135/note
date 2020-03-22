/**
 * [scroll 动态获取滚动条偏移距离的兼容写法]
 * scroll().top and scroll().left
 * @return {[number]} [垂直滚动条的距离 和 水平滚动条的距离]
 */
function scroll(){
	if (window.pageXOffset!==null) {
		return{
			top:window.pageYOffset,
			left:window.pageXOffset,
		}
	}else if(document.CompatMode === "CSS1Compat"){
		return {
			top:document.documentElement.scrollTop,
			left:document.documentElement.scrollLeft,
		}
	}
	return{
		top:document.body.scrollTop,
		left:document.body.scrollLeft,
	}
}
/**
 * [client 获取屏幕可视区的宽度和高度的兼容写法]
 * client().width and client().height
 * @return {[type]} [description]
 */
function client(){
	if (window.innerWidth) {
		return {
			width:window.innerWidth,
			height:window.innerHeight,
		}
	}else if(document.CompatMode === "CSS1Compat"){
		return {
			width:document.documentElement.clientWidth,
			height:document.documentElement.clientHeight,
		}
	}
	return {
		width:document.body.clientWidth,
		height:document.body.clientHeight,
	}
}
/**
* [getStyleAttr 获取css样式的兼容式写法]
* @param  {[object]} obj  [获取的对象]
* @param  {[string]} attr [属性]
* @return {[string]}      [css的属性值]
*/
function getStyleAttr(obj,attr){
	if (obj.currentStyle) { 
	//ie and opera
		return obj.currentStyle[attr];
	}else{
		//通用获取
		return window.getComputedStyle(obj,null)[attr];
	}
}
/**
 * [constantAnimation 匀速动画]
 * @param  {[object]} obj      [对象]
 * @param  {[number]} target   [目的点]
 * @param  {[number]} stepSize [步长]
 * @return {[type]}          [description]
 */
function constantAnimation(obj,target,stepSize){
	//1.0 清除动画
	clearInterval(obj.timer);
	//2.0 算出方向
	var dir = obj.offsetLeft < target?stepSize:-stepSize;
	//3.0 开启定时器
	obj.timer = setInterval(function(){
		//3.1 动起来
		obj.style.left =obj.offsetLeft + dir + "px";
		//3.2 设置临界值
		if (Math.abs(target - obj.offsetLeft)<Math.abs(dir)) {
			clearInterval(obj.timer);
			obj.style.left = target+"px";
		}
	},20);
}
/**
 * [getStyleAttr 获取节点的css属性]
 * @param  {[object]} obj  [对象]
 * @param  {[string]} attr [属性]
 * @return {[string]}      [属性值]
 */
function getCssAttrValue(obj,attr){
	if (obj.currentStyle) { 
		//兼容 ie and opera
		return obj.currentStyle[attr];
	}else{
		//兼容主流浏览器
		return window.getComputedStyle(obj,null)[attr];
	}
}
/**
 * [slowAnimation 缓动综合动画封装]
 * @param  {[object]}   obj     [对象]
 * @param  {[json]}   json    [属性和值]
 * @param  {[float]}   opacity [透明度0~1]
 * @param  {[float]}   slow    [缓动系数]
 * @param  {Function} fn      [回调函数]
 */
function slowAnimation(obj,json,slow,fn){
	//1.0 清除定时器
	clearInterval(obj.timer);
	//2.0 定义变量
	var start = 0, target=0,stepSize = 0;
	//3.0 开启定时器
	obj.timer = setInterval(function(){
		//3.1 遍历json数据 key就是属性；
		//定义旗帜
		var flag = true;
		for(key in json){
			//3.1.0 获取target的值 和 start 的值 
			if (key === "opacity") {
				//*100是用在filer里面的值
				target = parseFloat(json[key])*100;
				// 如果没有就取100;
				start = Math.round(parseFloat(getCssAttrValue(obj,key))*100);
			}else if(key === "scrollTop"){
				target = parseInt(json[key]);
				start = scroll().top;
			}else{
				target = parseInt(json[key]);
				//如果没有就取0
				start = parseInt(getCssAttrValue(obj,key))||0;
			}
			//3.1.1 计算缓动步长
			stepSize = (target - start)*slow;
			//3.1.2 取整步长
			stepSize = (target > start)?Math.ceil(stepSize):Math.floor(stepSize);
			//3.1.3 判断属性 并动起来
			if (key === "opacity") {
				// 兼容主流浏览器
				obj.style.opacity = (start + stepSize)/100;
				// 兼容ie8 
				obj.style.filter ="alpha("+(start + stepSize)+")"; 
			}else if(key ==="scrollTop"){
				obj.scrollTop=start+stepSize;
			}else if (key === "zIndex") {
				obj.style[key] = json[key];
			}else{
				obj.style[key]= start + stepSize+"px";
			}
			//3.2 设置边界值
			if (target !== start) {
				//已经全部完成
				flag = false;
			}
		}
		//4.0 判断完成之后清除定时器 并且设置回调函数
		if (flag) {
			clearInterval(obj.timer);
			//4.0.1 判断回调函数是否有值
			if (fn) {
				fn();
			}
			return false;
		}
	},20);
}
/**
 * [$ 节点选择器]
 * @param  {[string]} id [#id .class nodes]
 * @return {[object]}    [返回节点]
 */
function $(id){
	if (typeof id === "string" && document.querySelectorAll(id).length ===1) {
		return document.querySelector(id);
	}else if(typeof id ==="string" && document.querySelectorAll(id).length>1){
		return document.querySelectorAll(id);
	}else{
		return null;
	}
}
/**
 * [throttle 节流函数封装]
 * @param  {[function]} fun  [执行的函数]
 * @param  {[number]} time [节流时间]
 * @return {[function]}      [节流后返回函数]
 */
function throttle(fun,time){
	var timer = null;
	return function(){
		clearTimeout(timer);
		tiemr = setTimeout(fun,time);
	}
}
/**
 * [ajax 异步请求数据]
 * @param  {[object]} option [{提交方式：type,提交地址：url,超时时间：timeout，成功执行函数：success，错误执行函数：error}]
 * @return {[type]}        [description]
 */
function ajax(option) {
	//0.0 get请求后面传递参数
	option.t = new Date().getTime();
	var arr = [];
	for(var key in option.data){
		//0.1 放置get参数出现中文进行转码
		arr.push(encodeURIComponent(key)+"="+encodeURIComponent(option.data[key]));
	}
	var str = arr.join("&");
	//1.0 创建一个XMLHttpRequest异步对象兼容模式。
	var xmlhttp,timer;
	if (window.XMLHttpRequest) {
		xmlhttp = new XMLHttpRequest();
	}else{
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	//2-3 判断请求方式
	if (option.type.toLowerCase() === "post"){
			//3.0 post请求
			xmlhttp.open(option.type,option.url,true);
			// post请求注意点以下代码必须卸载open 和 send的中间 否则无效
			xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
			xmlhttp.send(str);
		}else if(option.type.toLowerCase() === "get"){
			//2.0 get 请求
			xmlhttp.open(option.type,option.url+"?"+str,true);
			//2.1 发送请求
			xmlhttp.send();
		}
	//4.0 动态监听变化
	xmlhttp.onreadystatechange = function(){
		//4.1 判断变化
		if (xmlhttp.readyState === 4) {
			//4.2 判断服务器返回编号确定是否请求成功
			clearInterval(timer);	
			if (xmlhttp.status>=200 && xmlhttp.status < 300 || xmlhttp.status === 304) {
				//4.3 成功执行函数 并且把异步对象传个他
				option.success(xmlhttp);
			}else{
				//4.4 不成功执行函数传个他
				option.error(xmlhttp);
			}
		}
	}
	//5.0 设置响应时间
	if (option.timeout) {
		timer = setInterval(function(){
			console.log("请求中断");
			xmlhttp.abort();
			clearInterval(timer);
		},option.timeout);
	}
}
/**
 * [addCookie 添加cookie]
 * @param {[string]} key    [键]
 * @param {[string]} value  [值]
 * @param {[num]} day    [保存期限 负数是删除]
 * @param {["/"]} path   ["/"根路径]
 * @param {[type]} domain [主域名为了让二级域名也可以访问]
 */
function addCookie(key,value,day,path,domain){
	var index = window.location.pathname.lastIndexOf("/");
	var currentPath = window.location.pathname.slice(0,index);
	path = path || currentPath;
	domain = domain || window.domain;
	if (!day) {
		document.cookie = key+"="+value+";path="+path+";domain:"+domain+";";
	}else{
		var d = new Date();
		d.setDate(d.getDate()+day);
		document.cookie = key+"="+value+";path="+path+";domain:"+domain+";expires="+d.toGMTString()+";";
	}
}
/**
 * [getCookie 获取cookie]
 * @param  {[string]} cname [要获取的键 名称]
 * @return {[string]}       [如后获取就返回值否则返回null]
 */
function getCookie(cname){
	var name = cname + "=";
	var ca = document.cookie.split(';');
	for(var i=0; i<ca.length; i++) {
		var c = ca[i].trim();
		if(c.indexOf(name)==0) {
			return c.substring(name.length,c.length); 
		}
	}
	return "";
}

/**
 * [removeCookie 删除cookie]
 * @param  {[string]} name [需要删除的键]
 * @param  {[“/”]} path [可选,如果要删除根目录里面的cookie需要添加"/"属性]
 * @return {[type]}      [description]
 */
function removeCookie(key,path){
	addCookie(key,getCookie(key),-1,path);
}
/**
 * [getStrLength 获取符串的长度]
 * @param  {[string]} str [检测的字符串]
 * @return {[type]}     [返回长度]
 */
function getStrLength(str){
	//定义变量
			var len =0;
	var code;
	//遍历
	for (var i = 0; i < str.length; i++) {
		code= str.charCodeAt(i);
		if (code>=0&&code<=127) {
			len+=1;
		}else{
			len+=2;
		}
	}
	return len;
}
/**
 * [getMost 获取数组当中重复次数最多的元素]
 * @param  {[arr]} arr [数组]
 * @return {[type]}     [description]
 */
function getMost(arr){
var hash = {};
var m = 0; 
var trueEl;
var el;
for(var i = 0,len = arr.length; i < len; i++ ) {
	el = arr[i];
	hash[el] === undefined ? hash[el] = 1 : (hash[el] ++);
	 	if(hash[el] >= m){
    		m = hash[el];
    		trueEl = el; 
		}
}
	return trueEl;
}
/**
 * [gethex 给一个rgb 转换为16进制颜色]
 * @param  {[type]} r [description]
 * @param  {[type]} g [description]
 * @param  {[type]} b [description]
 * @return {[type]}   [description]
 */
function gethex(r,g,b){ 
  r = r.toString(16); 
  g = g.toString(16); 
  b = b.toString(16); 

  // 补0 
  r.length==1? r = '0' + r : ''; 
  g.length==1? g = '0' + g : ''; 
  b.length==1? b = '0' + b : ''; 

  var hex = r + g + b; 

  // 简化处理,如 FFEEDD 可以写为 FED 
  if(r.slice(0,1)==r.slice(1,1) && g.slice(0,1)==g.slice(1,1) && b.slice(0,1)==b.slice(1,1)){ 
    hex = r.slice(0,1) + g.slice(0,1) + b.slice(0,1); 
  } 

  return hex; 
} 