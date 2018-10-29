//Some Events samples!

var headOne = document.querySelector('#one');
var headTwo = document.querySelector('#two');
var headThree = document.querySelector('#three');

//Hover (mouseover and mouseout)
headOne.addEventListener('mouseover', function() {
    headOne.textContent = "Mouse currently Over";
    headOne.style.color = 'red';
})

headOne.addEventListener('mouseout', function() {
    headOne.textContent = "Mouse Not On Me";
    headOne.style.color = 'green';
})

//On Click
headTwo.addEventListener('click', function() {
    headTwo.textContent = "Clicked On";
    headTwo.style.color = 'pink';
})

//Double Click
headThree.addEventListener('dblclick', function() {
    headThree.textContent = "DoubleClicked!";
    headThree.style.color = 'red';
})

// mouseover, mouseout, click, dblclick -> those are keywords!
