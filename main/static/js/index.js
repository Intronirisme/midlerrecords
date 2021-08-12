const contentDiv = document.querySelector('#content');
let tup;
let left;
let right;
let bottom;

document.addEventListener("DOMContentLoaded", function(event) {
    setTimeout(enableNavigation, 4000);
});

function enableNavigation() {
    console.log('давай !');
    injectTemplate(activePage);
    let hammerCube = new Hammer(document.querySelector('#cube'));
    hammerCube.get('tap').set({ enable: false });
    hammerCube.get('doubletap').set({ enable: false });
    hammerCube.get('press').set({ enable: false });
    hammerCube.get('swipe').set({ direction: Hammer.DIRECTION_ALL });

    hammerCube.on('swiperight', leftNav);
    hammerCube.on('swipeleft', rightNav);
    hammerCube.on('swipedown', upNav);
    hammerCube.on('swipeup', downNav);
}

//Navigation functions

async function upNav() {
    if(tup != 'None') {
        contentDiv.classList.remove('expand');
        await upAnimation();
        injectTemplate(tup);
        contentDiv.classList.add('expand');
    }
}

async function leftNav() {
    if(left != 'None') {
        contentDiv.classList.remove('expand');
        await leftAnimation();
        injectTemplate(left);
        contentDiv.classList.add('expand');
    }
}

async function rightNav() {
    if(right != 'None') {
        contentDiv.classList.remove('expand');
        await rightAnimation();
        injectTemplate(right);
        contentDiv.classList.add('expand');
    }
}

async function downNav() {
    if(bottom != 'None') {
        contentDiv.classList.remove('expand');
        await downAnimation();
        injectTemplate(bottom);
        contentDiv.classList.add('expand');
    }
}

//Animation functions

async function upAnimation() {
    document.querySelector("#cube").classList.add('up');
    return new Promise(resolve => {
        setTimeout(() => {
            document.querySelector("#cube").classList.remove('up');
            resolve('end rotate up animation');
        }, 800);
    });
}

async function downAnimation() {
    document.querySelector("#cube").classList.add('down');
    return new Promise(resolve => {
        setTimeout(() => {
            document.querySelector("#cube").classList.remove('down');
            resolve('end rotate down animation');
        }, 800);
    });
}

async function leftAnimation() {
    document.querySelector("#cube").classList.add('left');
    return new Promise(resolve => {
        setTimeout(() => {
            document.querySelector("#cube").classList.remove('left');
            resolve('end rotate left animation');
        }, 800);
    });
}

async function rightAnimation() {
    document.querySelector("#cube").classList.add('right');
    return new Promise(resolve => {
        setTimeout(() => {
            document.querySelector("#cube").classList.remove('right');
            resolve('end rotate right animation');
        }, 800);
    });
}

function setCaroussels() {
    let caroussels = document.querySelectorAll('.caroussel')
    let cards;
    let card;
    let angleD;
    let angleR;
    for(const caroussel of caroussels) {
        cards = caroussel.querySelectorAll('.card');
        if(cards.length != 0) {
            cardSize = +getComputedStyle(cards[0]).getPropertyValue('--size').slice(0, -2);
            angleD = 360/cards.length;
            angleR = (2*Math.PI)/cards.length;
            caroussel.style.cssText = `--d: ${Math.round((cardSize/2)/Math.tan(angleR/2))}px; --duration: ${cards.length * 3}s`;
            for(let i=0; i<cards.length; i++) {
                card = cards[i];
                card.style.setProperty('--rot', angleD*i+'deg');
            }
        }
    }
}

function injectTemplate(name) {
    let pageTemplate = document.querySelector('#'+name);
    contentDiv.innerHTML = '';
    contentDiv.appendChild(document.importNode(pageTemplate.content, true));
    setCaroussels();
    contentDiv.classList.add('expand');
    tup = pageTemplate.dataset.top;
    left = pageTemplate.dataset.left;
    right = pageTemplate.dataset.right;
    bottom = pageTemplate.dataset.bottom;
    activePage = name;
    setCSSvariable();
}

function setCSSvariable() {
    let color = document.querySelector('#'+activePage).dataset.color;
    let icon = document.querySelector('#'+activePage).dataset.icon;
    document.documentElement.style.setProperty('--front-color', color);
    document.documentElement.style.setProperty('--front-icon', "url('"+icon+"')");

    if(tup != 'None') {
        console.log(tup);
        color = document.querySelector('#'+tup).dataset.color;
        icon = document.querySelector('#'+tup).dataset.icon;
        document.documentElement.style.setProperty('--top-color', color);
        document.documentElement.style.setProperty('--top-icon', "url('"+icon+"')");
    }
    if(left != 'None') {
        color = document.querySelector('#'+left).dataset.color;
        icon = document.querySelector('#'+left).dataset.icon;
        document.documentElement.style.setProperty('--left-color', color);
        document.documentElement.style.setProperty('--left-icon', "url('"+icon+"')");
    }
    if(right != 'None') {
        color = document.querySelector('#'+right).dataset.color;
        icon = document.querySelector('#'+right).dataset.icon;
        document.documentElement.style.setProperty('--right-color', color);
        document.documentElement.style.setProperty('--right-icon', "url('"+icon+"')");
    }
    if(bottom != 'None') {
        color = document.querySelector('#'+bottom).dataset.color;
        icon = document.querySelector('#'+bottom).dataset.icon;
        document.documentElement.style.setProperty('--bottom-color', color);
        document.documentElement.style.setProperty('--bottom-icon', "url('"+icon+"')");
    }
}