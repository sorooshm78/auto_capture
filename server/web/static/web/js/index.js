function run_command() {
    command_element = $('#command');
    result_command_element = $('#result_command');

    command = command_element.val();
    const data = JSON.stringify({ "command": command });
    webSocket.send(data);

    command_element.val("");
    result_command_element.val("client -> " + command);
}

function showResultCommand(data) {
    result_command_element = $('#result_command');
    result_command_element.val(result_command_element.val() + '\n' + data);
}

function receiveData(data) {
    if (data['result_command']) {
        showResultCommand(data.result_command);
    }
}

$(document).ready(function () {
    webSocket = new WebSocket("ws://" + window.location.host + "/ws/command");

    webSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        receiveData(data);
    };
});