
function Snake() {
  this.x = 0;
  this.y = 0;
  this.xspeed = 1;
  this.yspeed = 0;
  this.total = 0;
  this.tail = [];

  this.eat = function(pos) {
    let d = dist(this.x, this.y, pos.x, pos.y);
    if (d < 1) {
      this.total++;
      return true;
    } else {
      return false;
    }
  };

  this.dir = function(x, y) {
    this.xspeed = x;
    this.yspeed = y;
  };

  this.death = function() {
    for (let i = 0; i < this.tail.length; i++) {
      let pos = this.tail[i];
      let d = dist(this.x, this.y, pos.x, pos.y);
      if (d < 1) {
        console.log('starting over');
        this.total = 0;
        this.tail = [];
      }
    }
  };

  this.update = function() {
    for (let i = 0; i < this.tail.length - 1; i++) {
      this.tail[i] = this.tail[i + 1];
    }
    if (this.total >= 1) {
      this.tail[this.total - 1] = createVector(this.x, this.y);
    }

    this.x = this.x + this.xspeed * scl;
    this.y = this.y + this.yspeed * scl;

    this.x = constrain(this.x, 0, width - scl);
    this.y = constrain(this.y, 0, height - scl);
  };

  this.show = function() {
    fill(255);
    for (let i = 0; i < this.tail.length; i++) {
      rect(this.tail[i].x, this.tail[i].y, scl, scl);
    }
    rect(this.x, this.y, scl, scl);
  };
}





//sketch
let s;
let scl = 40;
let food;

function setup() {
  createCanvas(200,200);
  s = new Snake();
  frameRate(10);
  pickLocation();
}

function pickLocation( x, y) {
  // let cols = floor(width / scl);
  // let rows = floor(height / scl);
  food = createVector(x,y);
  food.mult(scl);
}

// function mousePressed() {
//   s.total++;
//   console.log("asdfadfasdf");
// }
function delay_frame(t){
  t = 50*t;
  while(t > 0){
    t = t - 1;
  }
}
function draw() {
  console.log("{{all_position}}");
  background(51);
  if (s.eat(food)) {
    pickLocation();
  }
  s.death();
  s.update();
  s.show();
  fill(255, 0, 100);
  rect(food.x, food.y, scl, scl);
  delay_frame(1000000);
}

// function play(){
//     background(51);
//     if (s.eat(food)) {
//       pickLocation();
//     }
//     s.death();
//     s.update();
//     s.show();
//     fill(255, 0, 100);
//     rect(food.x, food.y, scl, scl);
// }


function motion(turn) {
  if (turn === 8) {
    s.dir(0, -1);
  } else if (turn === 2) {
    s.dir(0, 1);
  } else if (turn === 6) {
    s.dir(1, 0);
  } else if (turn === 4) {
    s.dir(-1, 0);
  }
}






