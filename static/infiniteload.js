var scroller = document.querySelector('#scroller');
var template = document.querySelector('#mii_template');
var loaded = document.querySelector("#loaded")
var end = document.querySelector("#itstheend")
var counter = 0;

function loadItems(){
    fetch("/load?page=${counter}").then((response) => {
        response.json().then((data) => {
            if (!data.length) {
                end.innerHTML = "<p class=\"text-muted\">No more Miis</p>";
                return;
            };
            for (var i = 0; i < data.length; i++) {
                let template_clone = template.loneNode(true);

                template_clone.querySelector("#username").innerHTML = "<p class=\"text-muted\">uhh idk how to do this</p>";
                template_clone.querySelector("#mii").attributes.src.value = "/miis/" + data[i];
                scroller.appendChild(template_clone);
                counter++;
            }
        });
    });
}

var observer = new IntersectionObserver(entries => {
    if (entries[0].intersectionRatio <= 0) {
        return;
    }
    loadItems();
})
observer.observe(end)

