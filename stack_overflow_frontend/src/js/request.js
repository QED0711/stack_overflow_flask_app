
import $ from 'jquery'

const request = (text, setPrediction) => {
    const settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://127.0.0.1:5000/",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache",
        },
        "processData": false,
        "data": JSON.stringify({user_input: text})
    }

    $.ajax(settings).done(function (response) {
        setPrediction(`${response.prediction}`);
    });
}

export default request