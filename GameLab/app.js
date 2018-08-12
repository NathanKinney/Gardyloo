
// Ball creation
var ballX = 75
var ballY = 75
var ballSpeedX = 5
var ballSpeedY = 7

const PADDLE_WIDTH = 100
const PADDLE_THICKNESS = 10
const PADDLE_DIST_FROM_EDGE = 60
var paddleX = 400


var canvas, canvasContext

var mouseX = 0
var mouseY = 0

function updateMousePos(evt) {
	var rect = canvas.getBoundingClientRect();
	var root = document.documentElement;

	mouseX = evt.clientX - rect.left - root.scrollLeft;
	mouseY = evt.clientY - rect.top - root.scrollTop;

	paddleX = mouseX - PADDLE_WIDTH/2;
}

window.onload = function() {
    canvas = document.getElementById('gameCanvas')
    canvasContext = canvas.getContext('2d')

    var framesPerSecond = 30
    setInterval(updateAll, 1000/framesPerSecond)

    canvas.addEventListener('mousemove', updateMousePos)
};

function updateAll() {
    moveAll()
    drawAll()

}

function ballReset(){
    ballX = canvas.width/2
    ballY = canvas.height/2
}

function moveAll(){
    ballX += ballSpeedX
    if(ballX < 0){ // left
        ballSpeedX *= -1;
    }
    if(ballX > canvas.width) { // right
        ballSpeedX *= -1;
    }

    ballY+= ballSpeedY

    if(ballY < 0) { // top edge
        ballSpeedY *= -1;
    }
    if(ballY > canvas.height) { // bottom edge
        ballReset()
    }

    var paddleTopEdgeY = canvas.height-PADDLE_DIST_FROM_EDGE
    var paddleBottomEdgeY = paddleTopEdgeY + PADDLE_THICKNESS
    var paddleLeftEdgeX = paddleX
    var paddleRightEdgeX = paddleLeftEdgeX + PADDLE_WIDTH

    // PADDLE COLLISION CHECKING AND DETERMINING ANGLE
    if(ballY > paddleTopEdgeY -10 && //  top of paddle
       ballY < paddleBottomEdgeY -10 && // bottom of paddle
       ballX > paddleLeftEdgeX && // right of the left side of the paddle
       ballX < paddleRightEdgeX) { // left of the right side of the paddle

        ballSpeedY *= -1
        // X SPEED DETEMRINATION
        var centerofPaddleX =  paddleX + PADDLE_WIDTH/2  // CREATING REFRENCE POINT FOR RATE OF X CHANGE
        var ballDistFromPaddleCenterX = ballX - centerofPaddleX // POS OR NEGATIVE NUMBER
        ballSpeedX = ballDistFromPaddleCenterX * 0.35; // FACTOR OF X CHANGE
    }
}

function drawAll(){

    colorRect(0,0, canvas.width, canvas.height,'black') //clear screen

    colorCircle(ballX,ballY, 10, 'white') // draw ball

    colorRect(paddleX, canvas.height-PADDLE_DIST_FROM_EDGE, //draw paddle
        PADDLE_WIDTH,PADDLE_THICKNESS, 'white')

    colorText(mouseX+","+mouseY, mouseX,mouseY, 'yellow')
}

function colorRect(topLeftX, topLeftY, boxWidth, boxHeight, fillColor){
    canvasContext.fillStyle = fillColor;
    canvasContext.fillRect(topLeftX,topLeftY, boxWidth,boxHeight)
}

function colorCircle(centerX,centerY, radius, fillColor){
    canvasContext.fillStyle = fillColor
    canvasContext.beginPath()
    canvasContext.arc(centerX,centerY, radius,0,Math.PI*2, true)
    canvasContext.fill()
}

function colorText(showWords, textX,textY, fillColor){
    canvasContext.fillStyle = fillColor
    canvasContext.fillText(showWords, textX,textY)
    console.log(mouseX, mouseY)
}