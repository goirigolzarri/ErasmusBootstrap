var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {

 

    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var talla;
        var color;
        var bandera;
        var fecha;

        if(document.getElementById('talla' + productId)){
            talla = document.getElementById('talla' + productId).value

        }

        if(document.getElementById('color' + productId)){
            color = document.getElementById('color' + productId).value
        }
        if(document.getElementById('bandera' + productId)){
            bandera = document.getElementById('bandera' + productId).value
        }

        if(document.getElementById('fecha' + productId)){
            fecha = document.getElementById('fecha' + productId).value
        }
        
        

        
        var action = this.dataset.action

        
        //Salvavidas
        var tallapr = this.dataset.talla
        var colorpr = this.dataset.color
        var banderapr = this.dataset.bandera
        var fechapr = this.dataset.fecha

        if(talla == undefined){
            talla = tallapr

        }
        if(color == undefined){
            color = colorpr

        }

        if(bandera == undefined){
            bandera = banderapr

        }
        if(fecha == undefined){
            fecha = fechapr

        }
        //



        console.log('productId:', productId, 'Action:', action, 'Color:', color, 'Talla:', talla, 'Bandera:', bandera, 'Fecha:', fecha)
        console.log('USER:', user)

        

        if(user == 'AnonymousUser'){

            console.log('Sin registrar')
            window.location.href = "/members/login/"
         
        }else{

            updateUserOrder(productId, action, color, talla, bandera, fecha)
        }

    })

}


function addCookieItem(productId, action){

    console.log('not logged in....')

    if (action == 'add'){

        if (cart[productId]==undefined){
            cart[productId] = {'quantity': 1}
        }else{

            cart[productId]['quantity'] += 1
            console.log('sumando')
        }
    }


    if (action == 'remove'){

        if (cart[productId]!=undefined){

            cart[productId]['quantity'] -= 1  
            console.log('restando')

            if(cart[productId]['quantity'] <= 0){

                console.log('Remove Item')
                delete cart[productId]

            }
        }
    }
    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}






function updateUserOrder(productId, action, color, talla, bandera, fecha){
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
        body:JSON.stringify({'productId': productId, 'action': action, 'color': color, 'talla': talla, 'bandera': bandera, 'fecha': fecha})
    })
    .then((response) =>{
        return response.json()

    })

    .then((data) =>{

        // console.log('data:', data)
        location.reload()
        

    });



}





