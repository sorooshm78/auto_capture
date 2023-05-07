function run_command() {
    command_element = document.getElementById("command");
    command = command_element.value;
    command_element.value = "";
}

function receiveData(data) {
    if (data['result_command']) {
        showUserInfo(data.user_info);
    }
}

$(document).ready(function () {
    webSocket = new WebSocket("ws://" + window.location.host + "/ws/command");

    webSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        receiveData(data);
    };
});