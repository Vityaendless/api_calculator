function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


async function makeRequest(url, body, method='GET') {
    let headers = {};
    if(method !== "GET") {
        const csrftoken = getCookie('csrftoken');
        headers['X-CSRFToken'] = csrftoken;
    }
    let response = await fetch(url, {method, body, headers});
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}


async function onClick(e) {
    e.preventDefault();
    let first = document.getElementById('first');
    let second = document.getElementById('second');
    let body = {
        "first": first.value,
        "second": second.value
    };
    console.log(body);
    let data = await makeRequest(e.target.dataset['operation'], JSON.stringify(body), "POST");
    console.log(data);
}


function onLoad() {
    let operations = document.getElementsByClassName("operation");
    for (let operation of operations) {
        operation.addEventListener('click', onClick);
    }
}


window.addEventListener('load', onLoad);
