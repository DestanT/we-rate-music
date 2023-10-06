// Close alert messages automatically
function timeout() {
    let messages = document.querySelectorAll("div.custom-alert");
    messages.forEach(message => {
        let customAlerts = new bootstrap.Alert(message);
        setTimeout(function() {
            customAlerts.close();
        }, 2500);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    timeout();
})