// Variables
var addToCartBtn = document.getElementsByClassName('add-to-cart')
var num = document.querySelector(".num")
var	hamburger = document.getElementById('hamburger')
var menu = document.getElementById('menu')
var body = document.querySelector('.container')
var increaseBtn = document.querySelectorAll(".increase")
var reduceBtn = document.querySelectorAll(".reduce")
var total = document.querySelector(".total")


// Menu toggle
hamburger.addEventListener('click', function (){
    if (menu.style.display == "block"){
        menu.style.display = "none"
    }else{
        menu.style.display = "block"
    }
})

// Add to cart function
for (var i = 0; i < addToCartBtn.length; i++) {
	addToCartBtn[i].addEventListener('click', function(){
		let productId = this.dataset.product
		fetch(addToCartUrl, {
			method: 'POST',
			credentials: 'same-origin',
			headers: {
				"X-CSRFToken": csrfToken,
				'Content-Type':'application/json',
			},
			body: JSON.stringify({
				'productId': productId,
				'deviceId': deviceId,
			})
		})
		.then((res) => {
			return res.json()
		})
		.then(refreshCart, (data) => {alert(data)})
	})
}


// Refresh cart items function
function refreshCart(){
	fetch(refreshUrl, {
		method: 'POST',
		credentials: 'same-origin',
		headers: {
			"X-CSRFToken": csrfToken,
			'Content-Type':'application/json',
		},
		body: JSON.stringify({
			'deviceId': deviceId,
		})
	})
	.then((res) => {
		return res.json()
	})
	.then((data) => {
		num.innerHTML = data
	})
}

// Green flash to notify the custumer that an item has been added to cart
function green() {
	body.style.background = "green"
}
function grey() {
	body.style.background = "#f4f4f4"
}

// Increase units function
for (var i = 0; i < increaseBtn.length; i++) {
	increaseBtn[i].addEventListener('click', function(){
		let productId = this.dataset.product
		fetch(addToCartUrl, {
			method: 'POST',
			credentials: 'same-origin',
			headers: {
				"X-CSRFToken": csrfToken,
				'Content-Type':'application/json',
			},
			body: JSON.stringify({
				'productId': productId,
				'deviceId': deviceId,
			})
		})
		.then((res) => {
			return res.json()
		})
		.then((data) => {
			this.previousElementSibling.innerHTML = data.units
			total.innerHTML = data.total
		})
		.then(refreshCart)
	})
}

// reduce units function
for (var i = 0; i < reduceBtn.length; i++) {
	reduceBtn[i].addEventListener('click', function(){
		let productId = this.dataset.product
		fetch(reduceUrl, {
			method: 'POST',
			credentials: 'same-origin',
			headers: {
				"X-CSRFToken": csrfToken,
				'Content-Type':'application/json',
			},
			body: JSON.stringify({
				'productId': productId,
				'deviceId': deviceId,
			})
		})
		.then((res) => {
			return res.json()
		})
		.then((data) => {
			if (data.units >= 1) {
				this.nextElementSibling.innerHTML = data.units
			} else {
				this.parentNode.parentNode.parentNode.style.display = "none"
			};
			total.innerHTML = data.total
		})
		.then(refreshCart)
	})
}