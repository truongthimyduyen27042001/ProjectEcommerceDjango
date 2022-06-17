var updateBtns = document.getElementsByClassName('update-cart')


for (var i = 0 ; i < updateBtns.length ; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product 
        var action = this.dataset.action
        console.log('productID: ', productId, 'action: ', action )

        console.log('user day ne: ' , user)
        if(user === 'AnonymousUser') {
            console.log('Not logged in')
            window.location.assign("http://localhost:8000/login/")
        }else {
            updateUserOdrder(productId,action)
        }
    })
}

function updateUserOdrder(productId, action) {
    console.log('User is authenticated, sending data...')
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    }).then((response)=> {
        return response.json()
    }).then((data)=> {
        console.log('Data: ', data)
        location.reload()
    }).catch((error)=> {
        console.log('Error: ',error)
    })
}