const startButton = document.getElementById("startButton")

const timeWaterCycle = document.getElementById("timeWaterCycle")
const timeStart = document.getElementById("timeStart")
const timeStop = document.getElementById("timeStop")

const bin1Nutrient1 = document.getElementById("bin1Nutrient1")
const bin1Nutrient2 = document.getElementById("bin1Nutrient2")
const bin1Nutrient3 = document.getElementById("bin1Nutrient3")
const bin1Nutrient4 = document.getElementById("bin1Nutrient4")
const bin1Nutrient5 = document.getElementById("bin1Nutrient5")
const bin1Nutrient6 = document.getElementById("bin1Nutrient6")
const bin1Nutrient7 = document.getElementById("bin1Nutrient7")
const bin1Nutrient8 = document.getElementById("bin1Nutrient8")
const bin1Nutrient9 = document.getElementById("bin1Nutrient9")

const bin2Nutrient1 = document.getElementById("bin2Nutrient1")
const bin2Nutrient2 = document.getElementById("bin2Nutrient2")
const bin2Nutrient3 = document.getElementById("bin2Nutrient3")
const bin2Nutrient4 = document.getElementById("bin2Nutrient4")
const bin2Nutrient5 = document.getElementById("bin2Nutrient5")
const bin2Nutrient6 = document.getElementById("bin2Nutrient6")
const bin2Nutrient7 = document.getElementById("bin2Nutrient7")
const bin2Nutrient8 = document.getElementById("bin2Nutrient8")
const bin2Nutrient9 = document.getElementById("bin2Nutrient9")





startButton.addEventListener("click", (e) => {
    e.preventDefault()
    fetch('http://localhost:5000/startSystem', {
        method: "POST",
        body: {}
    })

})
//console.log(logText.innerText)