// 和 python 类似

try {
     // 执行代码
     throw "哈哈"; //抛出错误

 } catch(e) {
     // 捕获错误
     console.log(e); 

 } finally {
     // 无论怎样都会执行
     console.log("完毕");
 } 
