function draw()
{
    var getRandomInt = (max) => {return Math.floor(Math.random() * max)};
    var sign = document.getElementById("sign");
    sign.style.borderStyle = "solid";
    sign.style.borderWidth = "medium";
    var num = getRandomInt(6)
    if(num == 0)
        sign.innerHTML = "大吉";
    else if(num == 1)
        sign.innerHTML = "中吉";
    else if(num == 2)
        sign.innerHTML = "小吉";
    else if(num == 3)
        sign.innerHTML = "末吉";
    else if(num == 4)
        sign.innerHTML = "小兇";
    else if(num == 5)
        sign.innerHTML = "大凶";
}
function countDown()
{
    var counter_text = document.getElementById("counter");
    var diff = new Date("2025/1/1 00:00:00") - new Date();
    var seconds = Math.floor(diff/1000)
    var minutes = Math.floor(seconds/60)
    var hours = Math.floor(minutes/60)
    var days = Math.floor(hours/24)
    seconds %= 60;
    minutes %= 60;
    hours %= 24;
    if(counter_text === null)
        console.log("not found")
    else 
        counter_text.innerHTML = days + "天" + hours + "時" + minutes + "分" + seconds + "秒"
    return ;
}
setInterval(countDown,1000)