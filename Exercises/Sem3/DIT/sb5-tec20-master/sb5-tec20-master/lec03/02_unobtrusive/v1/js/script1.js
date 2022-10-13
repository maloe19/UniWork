window.onload = () => {
	let button = document.getElementById("theButton");
	button.addEventListener("click", () => {
		document.getElementById("theOutput").innerHTML += "<br/>Button clicked.";
		console.log("Button clicked.");
	});
};