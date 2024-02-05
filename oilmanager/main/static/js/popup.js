function openPopup() {
    document.getElementById("popupForm").style.display = "block";
}

function openPopup_client_edit() {
    document.getElementById("popupForm_edit").style.display = "block";
}

function closePopup() {
    document.getElementById("popupForm_edit").style.display = "none";
    document.getElementById("popupForm").style.display = "none";
    document.getElementById("message").style.display = "none";
}
