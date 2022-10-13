let s: string = 'my favorite ' + 'string'
let b: boolean = ! true;
let i: number = 32 + Number('10');
console.log(s,b,i);

let a1: number[] = [1,2,3,4];
let a2: Array<string> = ['a','b','c'];
let a3: Array<any> = [new Object(), true, 42, 'hello!'];
console.log(a3.length);

s = a3[2]; //allowed, but s now holds a number when run
console.log(typeof s);

class Point {
    public x: number;
    public y: number;
    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }

    public move(dx: number, dy: number) {
        this.x = this.x + dx;
        this.y = this.y + dy;
    }
}

let p: Point = new Point(1,2);
console.log(p);
p.move(-1,3);
console.log(p);

interface XY {
    x: number;
    y: number;
}

function hypot (r: XY) {
    return Math.sqrt(r.x * r.x + r.y * r.y);
}
console.log("hypot:", hypot(p));

let square: (x: number) => number = x => x * x;

// a definition with type annotation on the arrow arg.
//let square = (x: number) => x * x;

// an equivalent declaration without arrow syntax
// function square (x: number): number { return x * x; }

let a4 = a1.map((v,_) => v+1);

let h = setTimeout(() => console.log("time's up"), 1000)

// an enum
enum Color { Red, Blue, Green};

// example of built-in generics (for Map)
let m: Map <number,string> = new Map();
m.set(0,"first entry");
m.set(1,"another entry");
m.forEach((i,s) => console.log(i,':',s));

class Pair<X,Y> {
 /*   public fst : X;
    public snd : Y; */
 /*   constructor(fst : X, snd : Y) {
        this.fst = fst;
        this.snd = snd;
    } */
    constructor(public fst : X, public snd : Y) { }

    public toString() : string { 
        return "<" + this.fst + ", " + this.snd + ">"
    }
}

let mypair: Pair<number,number> = new Pair(1,2);
console.log(mypair);

let zero: 0 = 0;
//zero = 3; //type error

function myfunc(arg: number|string) { /*...*/ }

let button_state: "on" | "off" = "on";
button_state = "off";


// function overloading
function g(x: number): void;
function g(x: string): void;
function g(x: any) { 
    if (typeof x == "number") console.log("number");
    else console.log("string");
}

g(4);
g('foo');
// g({}) //error