

function generate_post(){
    const location = document.getElementById("contentBox");

    let div = document.createElement('div');

    div.innerHTML = `
    <div class="card">
        <div class="card-body">
            <h4 class="card-title">Title</h4>
            <h6 class="text-muted card-subtitle mb-2">Subtitle</h6>
            <p class="card-text">Nullam id dolor id nibh ultricies vehicula ut id elit. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus.</p><a class="card-link" href="#">Link</a><a class="card-link" href="#">Link</a>
        </div>
    </div>`;

    div.style.cssText = 'margin:2px;';

    location.appendChild(div);
}

function sendData() {
    document.getElementById("form").addEventListener("submit", function(event){
        event.preventDefault()
        const className = document.getElementById("Classbox").value; 
        const content = document.getElementById("PostBox").value;
        const timeMade = new Date();
        var json_obj = {

            '_id':className,
            'content':content,
            'date': timeMade

        };
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/save_form_data");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(json_obj);
    }); 
}
