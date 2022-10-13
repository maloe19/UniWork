function greeter(person: string) {
    return "Hello, " + person;
}

let user: string = prompt("What is your name?");
document.body.textContent = greeter(user);