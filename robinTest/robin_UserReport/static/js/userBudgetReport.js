/*
function toggleClass(element, classToToggle)
{
    if (element.classList) {
        element.classList.toggle(classToToggle);
    } else {
        // For IE9
        var classes = element.className.split(" ");
        var i = classes.indexOf(classToToggle);
    
        if (i >= 0)
            classes.splice(i, 1);
        else
            classes.push(classToToggle);
            element.className = classes.join(" ");
    } 
}
*/

function hideElement(element)
{
    element.style.visibility = "hidden";
}

function showElement(element)
{
    element.style.visibility = "visible";
}

function showNewElementPop(element)
{

}

function hideAllPlusSigns()
{
    allPlusSigns = document.getElementsByTagName("plusButton");
    for (i = 0; i < allPlusSigns.length; i++)
    {
        allPlusSigns[i].addEventListener("onclick", showNewElementPop);
    }
}

$(document).ready(function() {
    //alert("Hello world from js script!");
    //hideAllPlusSigns();
});



