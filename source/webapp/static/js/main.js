async function makeRequest(url, method='GET') {
    let response = await fetch(url, {method});
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}


async function onAddClick(e) {
    e.preventDefault();
    let data = await makeRequest(e.target.dataset['operation']);
    console.log(data);
}


async function onSubtractClick(e) {
    e.preventDefault();
    let data = await makeRequest(e.target.dataset['operation']);
    console.log(data);
}


async function onMultiplyClick(e) {
    e.preventDefault();
    let data = await makeRequest(e.target.dataset['operation']);
    console.log(data);
}


async function onDivideClick(e) {
    e.preventDefault();
    let data = await makeRequest(e.target.dataset['operation']);
    console.log(data);
}


function onLoad() {
    let add = document.getElementById('add');
    add.addEventListener('click', onAddClick);

    let subtract = document.getElementById('subtract');
    subtract.addEventListener('click', onSubtractClick);

    let multiply = document.getElementById('multiply');
    multiply.addEventListener('click', onMultiplyClick);

    let divide = document.getElementById('divide');
    divide.addEventListener('click', onDivideClick);
}


window.addEventListener('load', onLoad);
