

function api(){
    console.log('Nos conectamos')

    var url = 'http://docs.housinganywhere.com/feed'
   
  
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({})
    })
    .then((response) =>{
        return response.json()

    })

    .then((data) =>{

        // console.log('data:', data)
        location.reload()
        

    });



}

window.onload = function() {
    init();
    api();
   
};
