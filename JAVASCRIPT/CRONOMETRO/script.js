let centiseconds = 0;
let seconds = 0;
let minutes = 0;
let timerInterval;
let isPaused = false;

function startTimer() {
    if (!timerInterval) {
        timerInterval = setInterval(updateTime, 10);  // Atualiza a cada 10ms para capturar centésimos
    }
}

function updateTime() {
    if (!isPaused) {
        centiseconds++;
        if (centiseconds === 100) {
            centiseconds = 0;
            seconds++;
        }
        if (seconds === 60) {
            seconds = 0;
            minutes++;
        }

        document.getElementById("display").innerHTML = 
            (minutes < 10 ? "0" + minutes : minutes) + ":" + 
            (seconds < 10 ? "0" + seconds : seconds) + ":<span class='centiseconds'>" + 
            (centiseconds < 10 ? "0" + centiseconds : centiseconds) + "</span>";

        document.getElementById("progress-bar").style.width = `${(centiseconds / 100) * 100}%`;
    }
}

function pauseTimer() {
    isPaused = !isPaused; // Alterna entre pausar e retomar
}

function resetTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
    centiseconds = 0;
    seconds = 0;
    minutes = 0;
    isPaused = false;
    document.getElementById("display").innerHTML = "00:00:00";
    document.getElementById("progress-bar").style.width = "0%";
}
