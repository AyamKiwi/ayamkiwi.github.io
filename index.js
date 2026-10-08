
const button = document.getElementById("info-btn")
const info_card = document.getElementById("info-card")
const info_close = document.getElementById("info-close")

button.addEventListener("click", (event) => {
    event.preventDefault()
    info_card.showModal()
})

info_card.addEventListener("click", (event) => {
    info_card.close()
})