length  //检查字符，数组，伪数组长度
console.log() //打印到控制台
alert(text) // 弹出框子

$.holdReady() //暂停jQuery暂停 入口函数执行 传入true暂停 传入false恢复

$.each(array/object, function(index, val) {
	 //遍历数组和伪数组
});
$.map(array, function(item, index) {
	return something;
	//静态遍历数组 each默认的遍历方法是遍历谁就返回谁 map默认返回空数组可以用return 回调中组成新的数组
});
$.trim('string') //去除字符串中的空格 需要重新接受一个下新的返回的字符串

$.isWindow('') //判断是否是windon对象 返回true 或 false

$.isArray() //判断是否是真数组 只有真数组才会返回true

$.isFunction(obj)//判断是否是一个函数

$.type()//判断数据类型

:has(contained selector/element)//找到包含制定子元素的元素
:parent(selector)//包含元素中特定文字的元素
:empty//选择所有没有子元素的元素（包括文本节点）。

.attr('attribute', 'value'); //传递一个参数 返回第一个找到属性节点的值 二个参数是设置属性节点的值 如果是设置参数 就会把找到的全部设置 如果属性节点不存在就会新增一个属性节点

.removeAttr('attribute name') //删掉所有找到属性元素的节 点 后面接续添加要删除的属性节点 用空格隔开

.eq(index)//找到第几个指定元素

.addClass('class_name')//添加一个类 添加多个用空格隔开

.removeClass('class name')//删除一个类 删多个用空格隔开

.toggleClass('selector');//有就删除 没有就添加

.html()//在元素里面设置子元素

.text('some text')//在元素里面设置文本

.val(text)//设置输入框里面的文本

.css('property', 'value');//元素设置样式

.width(integer)//获取元素的宽度 和设置元素宽度。

.height(integer)

.offset(coordinates);//获取或者设置元素到窗口左边的偏移量

.scrollTop(value)//获取和是设置滚动条的偏移位

$('html,body').scrollTop(30)//设置网页滚动条偏移位置

.click()

.off() //移除所有事件 传一个是移除指定事件 两个参 移除指定事件的地几个

在function（event）｛
return false;//阻止父亲触发儿子的事件阻止事件冒泡
event.stopPronpagetion();//阻止让元素也触发子元素的事件
｝
function(event){
	return false;//阻止触发标签的默认事件譬如a的跳转 提交按钮的提交等默认事件
	event.prevetDdfault（）;
}

trigger('click')//自动触发事件 会触发父亲的冒泡 会触发默认行为如果是a标签请用span包裹触发span的就可以了跳转了
triggerHandler('event name')//不会触发事件冒泡 不会触发默认行为

.on('click', '.selector', function(event) {
	event.preventDefault(); //用on来自定义事件满足连个条件 用on自定义事件 、用tirgger自动触发自定义事件名称
	/* Act on the event */
});
.trigger('chilc');

.on('click.命名空间', '.selector', function(event) {
	event.preventDefault();//事件的命名空间有效必须用on来命名，必须tirgger触发事件
	/* Act on the event */
});
//用事件命名空间的事件会产生父命名空间的冒泡 用事件父元素的所有同种类型的事件会冒泡
.delegate('selector', 'eventType', function(event) {
	selector//用已经有的父元素来监听动态添加的子元素的事件叫做事件委托
});
.index(selector/element);//拿到元素在兄弟中排第几

.siblings('selector');//拿到非当前的兄弟元素

.eq(index)和.get(element index)//拿到第几个指定的元素eq包装get不包装的html

.show('slow/400/fast', function() {
	//动画显示
});
.hide('slow/400/fast', function() {
	//动画隐藏
});

.toggle(slow/400/fast)//切换动画

$(window).scroll(function(event) {
	/* 监听网页滚动*/

});

.children('selector')//找到某个元素的子元素

.stop(clearQueue, gotoEnd)//执行动画之前先.stop 避免动画时长堆积

.delegate('selector', 'propertychange input', function(event) {
	selector //事实监听input和textare的输入
});

