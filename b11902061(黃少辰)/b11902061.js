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