let overlay = document.querySelector(".delete-confirm-overlay")
let problemNameSpan = document.querySelector("#problemName")
let problemIdLocal = 0

function showOverlay(problemId, name){
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

