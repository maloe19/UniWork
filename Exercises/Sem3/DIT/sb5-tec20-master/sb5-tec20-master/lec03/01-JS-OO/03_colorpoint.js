class Point {
    constructor(x,y) {
        this.x = x;
        this.y = y;
    }

    move(dx, dy) {
        this.x = this.x + dx;
        this.y = this.y + dy;
    }
}

class ColorPoint extends Point {
    constructor(x,y,color = "black") {
        super(x,y);
        this.color = color;
    }
}
let p = new Point(1,2);
console.log(p);
p.move(-1,3);
console.log(p);
let cp = new ColorPoint(1,2);
console.log(cp);
