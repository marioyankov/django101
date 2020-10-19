function expandCollapse() {
    if (this.parentElement.className.indexOf('collapsed') < 0) {
        this.parentElement.className += ' collapsed';
    } else {
        this.parentElement.className = this.parentElement.className.replace('collapsed', '');
    }
}

function initExpand () {
    const items = [...document.getElementsByClassName('collapse-toggle')];
    items.forEach(item => {
        item.addEventListener('click', expandCollapse);
    })
}

initExpand();
