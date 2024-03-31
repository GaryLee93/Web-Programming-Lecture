/*
function askAge()
{
    var x = prompt("你現在幾歲？","");
    if(x < 18)
    {
        alert("你年紀太小了喔");
        window.opener = null;
        window.close();
    }
    alert("兄弟，你好大");
}
window.addEventListener("DOMContentLoaded",askAge());
*/

function draw()
{
    var getRandomInt = (max) => {return Math.floor(Math.random() * max)};
    var sign = document.getElementById("sign");
    sign.style.borderStyle = "solid";
    sign.style.borderWidth = "medium";
    var num = getRandomInt(6)
    if(num <= 2) 
    {
        sign.style.backgroundColor = "#ff4000";
        if(num == 0)
            sign.innerHTML = "大吉";
        else if(num == 1)
            sign.innerHTML = "中吉";
        else if(num == 2)
            sign.innerHTML = "小吉";
    }
    else 
    {
        sign.style.backgroundColor = "#ff00ff";
        if(num == 3)
            sign.innerHTML = "小兇";
        else if(num == 4)
            sign.innerHTML = "中兇";
        else if(num == 5)
            sign.innerHTML = "大凶";
    }
}

var drawButton = document.getElementById("draw");
drawButton.addEventListener("click",draw);

