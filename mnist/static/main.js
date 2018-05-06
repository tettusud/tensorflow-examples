var canvas, ctx, flag = false,
    prevX = 0,
    currX = 0,
    prevY = 0,
    currY = 0,
    dot_flag = false;

var x = "blue",
    y = 8;

function init() {
    canvas = document.getElementById('can');
    ctx = canvas.getContext("2d");
    w = canvas.width;
    h = canvas.height;

    canvas.addEventListener("mousemove", function (e) {
        findxy('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        findxy('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        findxy('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e)
    }, false);
    
}

function color(obj) {
    switch (obj.id) {
        case "green":
            x = "green";
            break;
        case "blue":
            x = "blue";
            break;
        case "red":
            x = "red";
            break;
        case "yellow":
            x = "yellow";
            break;
        case "orange":
            x = "orange";
            break;
        case "black":
            x = "black";
            break;
        case "white":
            x = "white";
            break;
    }
    if (x == "white") y = 14;
    else y = 2;

}

function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = x;
    ctx.lineWidth = y;
    ctx.stroke();
    ctx.closePath();
}

function erase() {
    var m = confirm("Want to clear");
    if (m) {
        ctx.clearRect(0, 0, w, h);
        document.getElementById("canvasimg").style.display = "none";
        document.getElementById("class_predicted").innerText = "";
    }
}

function save() {
    document.getElementById("canvasimg").style.border = "2px solid";
    var dataURL = canvas.toDataURL();
    document.getElementById("canvasimg").src = dataURL;
    document.getElementById("canvasimg").style.display = "inline";
}

function findxy(res, e) {
    if (res == 'down') {
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft;
        currY = e.clientY - canvas.offsetTop;

        flag = true;
        dot_flag = true;
        if (dot_flag) {
            ctx.beginPath();
            ctx.fillStyle = x;
            ctx.fillRect(currX, currY, 2, 2);
            ctx.closePath();
            dot_flag = false;
        }
    }
    if (res == 'up' || res == "out") {
        flag = false;
    }
    if (res == 'move') {
        if (flag) {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
            draw();
        }
    }
}

function predict(){
    var img = new Image();
    img.onload = () => {
        var inputs = [];
        var small = document.createElement('canvas').getContext('2d');
        small.drawImage(img, 0, 0, img.width, img.height, 0, 0, 28, 28);
        var data = small.getImageData(0, 0, 28, 28).data;
        for (var i = 0; i < 28; i++) {
            for (var j = 0; j < 28; j++) {
                var n = 4 * (i * 28 + j);
                inputs[i * 28 + j] = (data[n + 0] + data[n + 1] + data[n + 2]) / 3;                
            }
        }
        if (Math.min(...inputs) === 255) {
            return;
        }
        request(inputs);
    }
    img.src = canvas.toDataURL();
}

function predict_v2(){
    var dimen=280
    var data=canvas.getContext('2d').getImageData(0,0,dimen,dimen).data
    var inputs=[]
    for (var i = 0; i < dimen; i++) {
        for (var j = 0; j < dimen; j++) {
            var n = 4 * (i * dimen + j);
            inputs[i * dimen + j] = (data[n + 0] + data[n + 1] + data[n + 2]) / 3;                
        }
        if(i==dimen-1){
            if (Math.min(...inputs) === 255) {
                return;
            }
            request(inputs);
        }
    }   
} 


/**
 * 
 * @param {*} inputs 
 */
function request(inputs){
    fetch("http://localhost:8080/predict", {
        body: JSON.stringify(inputs), // must match 'Content-Type' header
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, same-origin, *omit
        headers: {
            'user-agent': 'Mozilla/4.0 MDN Example',
            'content-type': 'application/json'
        },
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, cors, *same-origin
        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // *client, no-referrer
    })
    .then(res=>res.json())
    .then((res) => {
        console.log(res)
        document.getElementById('class_predicted').innerText=res.class;
    })
}