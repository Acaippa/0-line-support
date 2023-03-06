
// function checkClick(card, problemId){ // Sjekk om brukeren trykker på kortet eller editerings ikonet.
//     if (card.querySelector('.auth-div') == null){ // Om endre ikonet er ikke er tilstedet så går vi rett til problemets side
//         window.location.href = `/problem/${problemId}`
//     } else { // Om endre ikonet er tilstedet sjekker vi om brukeren IKKE trykker på den. Om det ikke er sant går vi til problemets side
//         if (this.event.target != document.querySelector(".edit-icon") && this.event.target != document.querySelector(".delete-icon")) {
//             window.location.href = `/problem/${problemId}`
//         }
//     }
// }
function checkClick(e, link){ // Sjekk om brukeren trykker på kortet eller editerings ikonet.
    if (!e) e = window.event;
        e.stopPropagation();
        window.location.href = link
}