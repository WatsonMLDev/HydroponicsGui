/*
Variables for home page buttons and fields
 */
const startButton = document.getElementById("startButton")
const stopButton = document.getElementById("killButton")
const statusText = document.getElementById("statusText")

const bin1On = document.getElementById("bin1On")
const bin2On = document.getElementById("bin2On")
const timeWaterCycleBin1 = document.getElementById("timeWaterCycleBin1")
const timeWaterCycleLastsBin1 = document.getElementById("timeWaterCycleLastsBin1")
const timeStartBin1 = document.getElementById("timeStartBin1")
const timeStopBin1 = document.getElementById("timeStopBin1")

const timeWaterCycleBin2 = document.getElementById("timeWaterCycleBin2")
const timeWaterCycleLastsBin2 = document.getElementById("timeWaterCycleLastsBin2")
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
const bin1lights = document.getElementById("bin1Lights")

const bin1Nutrient1Amount = document.getElementById("nutrient1bin1Amount")
const bin1Nutrient2Amount = document.getElementById("nutrient2bin1Amount")
const bin1Nutrient3Amount = document.getElementById("nutrient3bin1Amount")
const bin1Nutrient4Amount = document.getElementById("nutrient4bin1Amount")
const bin1Nutrient5Amount = document.getElementById("nutrient5bin1Amount")
const bin1Nutrient6Amount = document.getElementById("nutrient6bin1Amount")
const bin1Nutrient7Amount = document.getElementById("nutrient7bin1Amount")
const bin1Nutrient8Amount = document.getElementById("nutrient8bin1Amount")

const bin2Nutrient1 = document.getElementById("bin2Nutrient1")
const bin2Nutrient2 = document.getElementById("bin2Nutrient2")
const bin2Nutrient3 = document.getElementById("bin2Nutrient3")
const bin2Nutrient4 = document.getElementById("bin2Nutrient4")
const bin2Nutrient5 = document.getElementById("bin2Nutrient5")
const bin2Nutrient6 = document.getElementById("bin2Nutrient6")
const bin2Nutrient7 = document.getElementById("bin2Nutrient7")
const bin2Nutrient8 = document.getElementById("bin2Nutrient8")
const bin2lights = document.getElementById("bin2Lights")

const bin2Nutrient1Amount = document.getElementById("nutrient1bin2Amount")
const bin2Nutrient2Amount = document.getElementById("nutrient2bin2Amount")
const bin2Nutrient3Amount = document.getElementById("nutrient3bin2Amount")
const bin2Nutrient4Amount = document.getElementById("nutrient4bin2Amount")
const bin2Nutrient5Amount = document.getElementById("nutrient5bin2Amount")
const bin2Nutrient6Amount = document.getElementById("nutrient6bin2Amount")
const bin2Nutrient7Amount = document.getElementById("nutrient7bin2Amount")
const bin2Nutrient8Amount = document.getElementById("nutrient8bin2Amount")

const primePumpButton = document.getElementById("primePumpButton")
const primePumpText = document.getElementById("primePumpsText")



if (startButton.disabled === false) {
    stopButton.disabled = true
}
statusText.innerText = "Status: Not opperational"
/*
Whenever the start button is clicked, the start button is disabled and the stop button is enabled, makes a POST request
to the server to start the water cycle with the pre-selected values
 */
startButton.addEventListener("click", (e) => {
    e.preventDefault()
    if (startButton.disabled === true) {
        return
    } else {
        fetch('http://localhost:5000/startSystem', { // POST request to start the system
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                bin1On: bin1On.checked,
                bin2On: bin2On.checked,
                timeWaterCycleBin1: timeWaterCycleBin1.value,
                timeWaterCycleLastsBin1: timeWaterCycleLastsBin1.value,
                timeStartBin1: timeStartBin1.value,
                timeStopBin1: timeStopBin1.value,
                timeWaterCycleBin2: timeWaterCycleBin2.value,
                timeWaterCycleLastsBin2: timeWaterCycleLastsBin2.value,
                timeStartBin2: timeStartBin2.value,
                timeStopBin2: timeStopBin2.value,
                bin1Nutrient1: bin1Nutrient1.checked,
                bin1Nutrient2: bin1Nutrient2.checked,
                bin1Nutrient3: bin1Nutrient3.checked,
                bin1Nutrient4: bin1Nutrient4.checked,
                bin1Nutrient5: bin1Nutrient5.checked,
                bin1Nutrient6: bin1Nutrient6.checked,
                bin1Nutrient7: bin1Nutrient7.checked,
                bin1Nutrient8: bin1Nutrient8.checked,
                bin1Nutrient1Amount: bin1Nutrient1Amount.value,
                bin1Nutrient2Amount: bin1Nutrient2Amount.value,
                bin1Nutrient3Amount: bin1Nutrient3Amount.value,
                bin1Nutrient4Amount: bin1Nutrient4Amount.value,
                bin1Nutrient5Amount: bin1Nutrient5Amount.value,
                bin1Nutrient6Amount: bin1Nutrient6Amount.value,
                bin1Nutrient7Amount: bin1Nutrient7Amount.value,
                bin1Nutrient8Amount: bin1Nutrient8Amount.value,
                bin1lights: bin1lights.checked,
                bin2Nutrient1: bin2Nutrient1.checked,
                bin2Nutrient2: bin2Nutrient2.checked,
                bin2Nutrient3: bin2Nutrient3.checked,
                bin2Nutrient4: bin2Nutrient4.checked,
                bin2Nutrient5: bin2Nutrient5.checked,
                bin2Nutrient6: bin2Nutrient6.checked,
                bin2Nutrient7: bin2Nutrient7.checked,
                bin2Nutrient8: bin2Nutrient8.checked,
                bin2Nutrient1Amount: bin2Nutrient1Amount.value,
                bin2Nutrient2Amount: bin2Nutrient2Amount.value,
                bin2Nutrient3Amount: bin2Nutrient3Amount.value,
                bin2Nutrient4Amount: bin2Nutrient4Amount.value,
                bin2Nutrient5Amount: bin2Nutrient5Amount.value,
                bin2Nutrient6Amount: bin2Nutrient6Amount.value,
                bin2Nutrient7Amount: bin2Nutrient7Amount.value,
                bin2Nutrient8Amount: bin2Nutrient8Amount.value,
                bin2lights: bin2lights.checked
            }) // JSON object with the values of the fields
        })
            .then(res => res.json())
            .then(data => {
                console.log(data)
                if (data.success) {
                    statusText.innerText = "Status: Started System"
                    startButton.disabled = true
                    stopButton.disabled = false
                    return
                } else {
                    console.log("Error: " + data.error)
                    statusText.innerText = "Status: " + data.error
                    return
                }
            }).catch(err => console.log(err))
    }
})

primePumpButton.addEventListener("click", (e) => {
    e.preventDefault()
    if (!(statusText.innerText === "Status: Not opperational")){
        primePumpText.innerText = "Operation failed, system already started"
        return
    }
    primePumpText.innerText = "Priming pumps..."
    fetch('http://localhost:5000/primePumps', { // POST request to prime the pumps
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            return
        }).catch(err => console.log(err))
    primePumpText.innerText = "Successfully primed pumps"
})

/*
Whenever the stop button is clicked, the stop button is disabled and the start button is enabled, makes a POST request to
the server to stop the water cycle
 */
stopButton.addEventListener("click", (e) => {
    e.preventDefault()
    if (stopButton.disabled === true) {
        return
    } else {
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
