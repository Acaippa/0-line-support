let overlay = document.querySelector(".delete-confirm-overlay")
let problemNameSpan = document.querySelector("#problemName")
let problemIdLocal = 0

function showOverlay(e, problemId, name){
    if (!e) e = window.event;
        e.stopPropagation(); // Gjør at bildets funskjon blir kjørt istedet for divisjonens.
        window.location.href = "#" // Uten denne linjen blir brukeren sendt til problemets side.
        problemNameSpan.innerHTML = name
        problemIdLocal = problemId
        overlay.style.display = "block"
}

function hideOverlay(confirm){
    if (confirm){
        overlay.style.display = "none"
        window.location.href = `deleteproblem/${problemIdLocal}`
    } else {
        overlay.style.display = "none"
    }
}

