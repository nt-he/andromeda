var counter = 0;
var scrollend = document.querySelector("#itstheend")
var scroller = document.querySelector("#scroller");
var template = document.querySelector('#mii_template');
var loaded = document.querySelector("#loaded")
function loadItems(){
    fetch(`/load?page=${counter}`).then((response) => {
        response.json().then((data) => {
            if (!data.miis.length) {
                scrollend.innerHTML = "<p class=\"text-muted\">No more Miis</p>";counter += 1;
                return;
            };
            for (var i = 0; i < data.miis.length; i++) {
                let template_clone = template.content.cloneNode(true);

                template_clone.querySelector("#username").innerHTML = "<p class=\"text-muted\">uhh idk how to do this</p>";
                template_clone.querySelector("#mii").attributes.src.value = "/miis/" + data.miis[i];
                scroller.appendChild(template_clone);
                counter += 1;
            }
        });
    });
}

var observer = new IntersectionObserver(entries => {
    if (entries[0].intersectionRatio <= 0) {
        return;
    }
    loadItems();
});

observer.observe(scrollend)