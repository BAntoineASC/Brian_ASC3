//Set up global variables first
var x,y,speed,xf,yf;
x=0;
y=0;
xf=  Math.floor((Math.random() * 100) + 1);    
yf =    Math.floor((Math.random() * 100) + 1);    
speed = 1;
w=20


  
//change the maze based on the level
function Level(newlevel){
    if(newlevel==1){
        fill(243,255,0);
        rectMode(CORNER);
        rect(50,50,200,50);
    }
    if(newlevel==2){
        fill(243,255,0);
        rectMode(CORNER); 
        rect(50,50,50,400);
        rect(180,300,50,300);
    }


}

/*check if there is overlap between colors*/
function CheckCollision(array, pixel_color){
}

//setup the canvas and background color
function setup(){
    //createCanvas(100, 50);
    //background(153);
    background(0);
    createCanvas(500,500);
}


function MovePad(value){
    if(value==="d")// && x<480);
        x+=speed;
    if((value=== "a") && (x<0));
        x += -speed;
    if((value==="s") && (y<480));
        y += speed;
    if(value ==="w" && y<0);
        y += -speed;

}
function draw() {
    
    background(0);
    rect(xf,yf,20,20);
    if (key==="d")//|| key==="D")
        //MovePad("d");
        x+=speed;
    else if(key ==="a")//|| key ==="A")
        x-=speed;
        // MovePad("a");
    else if(key ==="s" )//|| key ==="S")
        y+=speed;
         //MovePad("s");
    else if(key ==="w")// || key ==="W")
          y-=speed;
         //MovePad("w");
    else;//do nothing

    if (x > 480 )
      x = 480;
    if (x<= 0)
      x= 0;
    if (y>480)
      y = 480;
    if (y<= 0)
      y= 0;

    fill(255.255,255)
    rect(xf,yf,20,20)

    if (x === xf && y===yf) {
      w=w + 20;
    }
    //draw the walls based on the level we are at
    //draw the paddel
    rectMode(CORNER);
    fill(255,0,0);
    rect(x,y,w,20);
    
    //check
}


