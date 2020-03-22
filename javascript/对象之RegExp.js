var str="179831646@qq.com,456131@Qq.com";
var re = new RegExp(/(\d+)@qq.com/g);
let temp;
while (temp = re.exec(str)) {
    console.log(temp[1])
}
console.log(str.);
