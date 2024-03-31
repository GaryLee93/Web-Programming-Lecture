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
