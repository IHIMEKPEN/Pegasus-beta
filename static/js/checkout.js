function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
var payButton = document.getElementById('payButton')
payButton.addEventListener('click', function (e) {
	e.preventDefault()
	fetch(paymentInitUrl, {
		method: 'POST',
		credentials: 'same-origin',
		headers: {
			"X-CSRFToken": csrftoken,
			"Content-Type": "applicatio/json",
		},
		body: JSON.stringify({
			"email": email,
			"amount": amount,
			"callback_url": "https://prj-django-ecomm.herokuapp.com/checkout/verify/",
			"reference": reference,
			"firs_tname": firstname,
			"last_name": lastname,
		})
	})
	.then((res) => res.json())
	.then((data) => {
		console.log(data)
		if (data.status === false){
			alert(data.message)
		} else {
			var paymentUrl = data.data.authorization_url
			window.open(paymentUrl)
		}
	})
})

// sk_test_82a06115f060a7f760a4d7b9e56967ec954bea45