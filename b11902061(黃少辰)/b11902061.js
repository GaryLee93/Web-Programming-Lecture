function withdraw_NASA(){
    if (confirm("確定要停修NASA嗎？")){
        var lesson = document.getElementById("lesson");
        var nasa = document.getElementById("nasa");
        var button = document.getElementById("withdraw_button");
        lesson.removeChild(nasa);
        lesson.removeChild(button);

        var nasa_col = document.getElementsByClassName("nasa_col");
        for(var i=0; i<nasa_col.length; i++){
            nasa_col[i].innerHTML = "";
        }
        alert("恭喜你已停修NASA！");
    }
    else{
        alert("還不快停修！");
    }
}

var problem2038 = new Date("2038/1/19 3:14:07");
window.onload = init;

function init(){
    countTime();
    setInterval(countTime, 1000);
}

function countTime(){
    var timerElement = document.getElementById("timer");
    if(timerElement == null)
        console.warn("timer null");
    
    var nowDate = new Date();
    var timeDiff = Math.floor((problem2038 - nowDate)/1000);

    var sec = timeDiff % 60;
    var min = Math.floor(timeDiff/60) % 60;
    var hour = Math.floor(timeDiff/3600) % 24;
    var day = Math.floor(timeDiff/86400);

    timerElement.innerHTML = day + " 天 " + hour + " 小時 " + min + " 分 " + sec + " 秒";
}