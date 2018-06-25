function swapElementDisplay(element)
{
    if("block" == element.style.display)
    {
        element.style.display = "none";
    }
    else
    {
        element.style.display = "block";
    }
}

var popUpModalId = 'newDataInputModal';
var popUpModalSubmitButtonId = 'newDataInputSubmit';
var newSpendingTargetCategoryId = 'newSpendingTargetCategory';

function cleanUpNewDataInput(element)
{
    //  clean up the form of any previously inserted data (browsers seem to remember this)
    document.getElementById('newDataInputValue').value = '';
    document.getElementById('newDataInputName').value = '';
    document.getElementById('newDataInputFileName').value = '';
    document.getElementById(newSpendingTargetCategoryId).innerHTML = "";
}

function getTextForCategoryId(cagetoryId)
{
    // js_plusButtonId_The-Name-Of-category_4
    var valuesFromId = cagetoryId.split("_");
    var finalValue = '';
    if(4 == valuesFromId.length)
    {
        finalValue = valuesFromId[2];
        finalValue.replace("-"," ");
    }
    return finalValue;
}

function showNewElementPop(element)
{
    var newDataInput = document.getElementById(popUpModalId);
    cleanUpNewDataInput(newDataInput);
    swapElementDisplay(newDataInput);
    var newSpendingCategory = document.getElementById(newSpendingTargetCategoryId);
    newSpendingCategory.innerHTML = getTextForCategoryId(element.id);
}

function saveNewDataInputValues(element)
{
    // saves the data that user put in the input form
    // to a global storage for later submittion.
}

function updateCurrentlyDisplayedValues(element)
{
    // updates all the displayed data based on the
    // values held in the global storage
}

function setupPopUpModal()
{
    var spanCloseButton = document.getElementsByClassName("close")[0];
    var newDataInput = document.getElementById(popUpModalId);
    spanCloseButton.addEventListener("click", function(){swapElementDisplay(newDataInput);});

    var newDataInputButton  = document.getElementById(popUpModalSubmitButtonId);
    newDataInputButton.addEventListener("click", function(){
        saveNewDataInputValues(newDataInput);
        updateCurrentlyDisplayedValues(newDataInput);
        swapElementDisplay(newDataInput);
    });
}

function hideAllPlusSigns()
{
    allPlusSigns = document.getElementsByTagName("plusButton");
    for (i = 0; i < allPlusSigns.length; i++)
    {
        var plusSignElement = allPlusSigns[i];
        plusSignElement.addEventListener("click", function(){
            showNewElementPop(plusSignElement);
        });
    }
}

$(document).ready(function() {;
    hideAllPlusSigns();
    setupPopUpModal();
});

/*function swapElementVisibility(element)
{
    if("hidden" == element.style.visibility)
    {
        element.style.visibility = "visible";
    }
    else
    {
        element.style.visibility = "hidden";
    }
}*/