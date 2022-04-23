/*
Variables for home page buttons and fields
 */
const startButton = document.getElementById("startButton")
const stopButton = document.getElementById("killButton")
const statusText = document.getElementById("statusText")

const timeWaterCycleBin1 = document.getElementById("timeWaterCycleBin1")
const timeStartBin1 = document.getElementById("timeStartBin1")
const timeStopBin1 = document.getElementById("timeStopBin1")

const timeWaterCycleBin2 = document.getElementById("timeWaterCycleBin2")
const timeStartBin2 = document.getElementById("timeStartBin2")
const timeStopBin2 = document.getElementById("timeStopBin2")

const bin1Nutrient1 = document.getElementById("bin1Nutrient1")
const bin1Nutrient2 = document.getElementById("bin1Nutrient2")
const bin1Nutrient3 = document.getElementById("bin1Nutrient3")
const bin1Nutrient4 = document.getElementById("bin1Nutrient4")
const bin1Nutrient5 = document.getElementById("bin1Nutrient5")
const bin1Nutrient6 = document.getElementById("bin1Nutrient6")
const bin1Nutrient7 = document.getElementById("bin1Nutrient7")
const bin1Nutrient8 = document.getElementById("bin1Nutrient8")
const bin1lights = document.getElementById("bin1Nutrient9")

const bin2Nutrient1 = document.getElementById("bin2Nutrient1")
const bin2Nutrient2 = document.getElementById("bin2Nutrient2")
const bin2Nutrient3 = document.getElementById("bin2Nutrient3")
const bin2Nutrient4 = document.getElementById("bin2Nutrient4")
const bin2Nutrient5 = document.getElementById("bin2Nutrient5")
const bin2Nutrient6 = document.getElementById("bin2Nutrient6")
const bin2Nutrient7 = document.getElementById("bin2Nutrient7")
const bin2Nutrient8 = document.getElementById("bin2Nutrient8")
const bin2lights = document.getElementById("bin2Nutrient9")



if(startButton.disabled === false){
    stopButton.disabled = true
}
statusText.innerText = "Status: Not opperational"
/*
Whenever the start button is clicked, the start button is disabled and the stop button is enabled, makes a POST request
to the server to start the water cycle with the pre-selected values
 */
startButton.addEventListener("click", (e) => {
    e.preventDefault()
    if(startButton.disabled === true){
        return
    }
    else{
        fetch('http://localhost:5000/startSystem', { // POST request to start the system
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({timeWaterCycleBin1: timeWaterCycleBin1.value, timeStartBin1: timeStartBin1.value, timeStopBin1: timeStopBin1.value,
                timeWaterCycleBin2: timeWaterCycleBin2.value, timeStartBin2: timeStartBin2.value, timeStopBin2: timeStopBin2.value,
                bin1Nutrient1: bin1Nutrient1.checked, bin1Nutrient2: bin1Nutrient2.checked,
                bin1Nutrient3: bin1Nutrient3.checked, bin1Nutrient4: bin1Nutrient4.checked,
                bin1Nutrient5: bin1Nutrient5.checked, bin1Nutrient6: bin1Nutrient6.checked,
                bin1Nutrient7: bin1Nutrient7.checked, bin1Nutrient8: bin1Nutrient8.checked,
                bin1lights: bin1lights.checked, bin2Nutrient1: bin2Nutrient1.checked,
                bin2Nutrient2: bin2Nutrient2.checked, bin2Nutrient3: bin2Nutrient3.checked,
                bin2Nutrient4: bin2Nutrient4.checked, bin2Nutrient5: bin2Nutrient5.checked,
                bin2Nutrient6: bin2Nutrient6.checked, bin2Nutrient7: bin2Nutrient7.checked,
                bin2Nutrient8: bin2Nutrient8.checked, bin2lights: bin2lights.checked }) // JSON object with the values of the fields
        })
            .then(res => res.json())
            .then(data => {
                console.log(data)
                if (data.success) {
                    statusText.innerText = "Status: Started System"
                    startButton.disabled = true
                    stopButton.disabled = false
                    return
                }
                else{
                    console.log("Error: " + data.error)
                    statusText.innerText = "Status: " + data.error
                    return
                }
            }).catch(err => console.log(err))
    }
})

/*
Whenever the stop button is clicked, the stop button is disabled and the start button is enabled, makes a POST request to
the server to stop the water cycle
 */
stopButton.addEventListener("click", (e) => {
    e.preventDefault()
    if(stopButton.disabled === true){
        return
    }
    else{
        fetch('http://localhost:5000/stopSystem', { // POST request to stop the system
            method: "POST"
        })
            .then(res => res.json())
            .then(data => {
                console.log(data)
                if (data.success) {
                    statusText.innerText = "Status: Stopped System"
                    startButton.disabled = false
                    stopButton.disabled = true
                    return
                }
            }).catch(err => console.log(err))
    }
})
