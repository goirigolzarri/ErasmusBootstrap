var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {

 

    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var talla;
        var color;
        // var bandera;
        // var fecha;

        if(document.getElementById('talla' + productId)){
            talla = document.getElementById('talla' + productId).value

        }

        if(document.getElementById('color' + productId)){
            color = document.getElementById('color' + productId).value
        }
   
        var action = this.dataset.action

        
        //Salvavidas
        var tallapr = this.dataset.talla
        var colorpr = this.dataset.color
        // var banderapr = this.dataset.bandera
        // var fechapr = this.dataset.fecha

        if(talla == undefined){
            talla = tallapr

        }
        if(color == undefined){
            color = colorpr

        }

        console.log('productId:', productId, 'Action:', action, 'Color:', color, 'Talla:', talla)
        console.log('USER:', user)


        if(user == 'AnonymousUser'){

            console.log('Sin registrar')
            // window.location.href = "/login/"
         
        }else{

            updateUserOrder(productId, action, color, talla)
        }

    })

}






function updateUserOrder(productId, action, color, talla){
    console.log('User is authenticated, sending data...')

    var url = '/shop/update_item/'
   
    console.log('ProductId:', productId)
    console.log('action:', action)
    console.log('color:', color)
    console.log('talla:', talla)
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action, 'color': color, 'talla': talla})
    })
    .then((response) =>{
        return response.json()

    })

    .then((data) =>{

        // console.log('data:', data)
        location.reload()
        

    });



}

