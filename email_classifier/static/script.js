let message= document.querySelector("textarea")
let model = document.querySelector('[name="model"]')
let vectorizer=document.querySelector('[name="vectorizer"]')
let button=document.querySelector("button")

let resultSection = document.querySelector(".result-section");
resultSection.style.display="none";


button.addEventListener("click", async function(event) {

    event.preventDefault();

    if (!validateInput()) {
        return;
    }

    let userData = getUserInput();

    let formData = new FormData();

    formData.append("message", userData.message);
    formData.append("model", userData.model);
    formData.append("vectorizer", userData.vectorizer);

    try {

        let response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        let data = await response.json();

        if (!response.ok) {
            alert(data.error);
            return;
        }

        displayResult(data.prediction, userData);

    } catch (error) {
        console.log(error);
        alert("Something went wrong!");
    }

});


function validateInput() {

    let userMessage = message.value.trim();
    let selectedModel = model.value;
    let selectedVectorizer = vectorizer.value;

    if (userMessage === "") {
        alert("Please enter a message");
        return false;
    }

    if (selectedModel === "") {
        alert("Please select an algorithm");
        return false;
    }

    if (selectedVectorizer === "") {
        alert("Please select a vectorizer");
        return false;
    }

    return true;
}

function getUserInput() {

    let userData = {
        message: message.value.trim(),
        model: model.value,
        vectorizer: vectorizer.value
    };

    return userData;
}

function analyzeMessage() {

    if (!validateInput()) {
        return;
    }

    let userData = getUserInput();

    console.log("Message:", userData.message);
    console.log("Selected Model:", userData.model);
    console.log("Selected Vectorizer:", userData.vectorizer);

}


function displayResult(prediction, userData) {

    document.getElementById("predictionStatus").textContent = prediction;

    document.getElementById("resultModel").textContent = userData.model;

    document.getElementById("resultVectorizer").textContent = userData.vectorizer;

    document.getElementById("resultMessage").textContent = userData.message;

    resultSection.style.display = "block";
}
