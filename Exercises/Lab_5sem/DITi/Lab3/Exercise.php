//Exercise 1----------------------------------------------------
/*
let hashtag = "";
	
	let triangle = function(x) {
	        for (i = 0; i < x; i++) {
	        console.log(hashtag += "#")
	    }
	}
	
	triangle(5)
	
	---
	
	let hashtag = "";
	
	let triangle = function(x, y) {
	        for (i = 0; i < x; i++) {
	        console.log(hashtag += y)
	    }
	}
	
	triangle(5, "%")
*/

<!DOCTYPE html>
<html>
<body>

<?php
$hashtag = "";

function triangle($x){
    for($y = 0; $y < $x; $y++){
        echo "$hashtag += #"; 
    }
}
triangle(5)
?>

</body>
</html>

//Exercise 2----------------------------------------------------
/*
class Vec {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        length = Math.sqrt(this.x * this.x + this.y * this.y);
        }
    plus(v) {
        return { x: this.x + v.x, y: this.y + v.y };
    }
    minus(v) {
        return { x: this.x - v.x, y: this.y - v.y };
    }

}
*/
<?php
class Vector{
	function __construct($x,$y){
		$this->x = $x;
		$this->y = $y;
		$length = sqrt($this->x*$this->x + $this->y*$this->y);
	}
	function plus($v){
		return $this->x + $v->x. $this->y + $v->y;
	}
	function minus($v){
		return $this->x - $v->x. $this->y - $v->y;
	}
}
$vec1 = new Vector(1,2);
echo $vec->plus(new Vector(2,3));
$vec2 = new Vector(1,2);
echo $vec->plus(new Vector(2,3));
$vec3 = new Vector(3,4);
echo $vec->length; 
?>