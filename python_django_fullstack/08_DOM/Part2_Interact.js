//These are for console.

var x = document.querySelector("p");

//Show text
x.textContent;

//Reassign textContent
x.textContent = "new";
//This show you the string itself. the <strong>tag doesnt' affect to the text
x.textContent = "This is <strong>STRONG TAG</strong>";

//Refreshing the page
//Show actual html
x.innerHTML;

//Edit HTML, if this string assigne to .textContent, it will show you as literal string, not tag affected
x.innerHTML = "This is <strong>STRONG TAG</strong>";

//Can't do that with just textContent

///ATTRIBUTES///

var special = document.querySelector("#special");
var specialA = y.querySelector("a");

specialA.getAttribute("href");

specialA.setAttribute("href", "https://www.amazon.com");
