$(document).ready(function () {
    $("#price-btn").on('click', function () {
        priceForm = new FormData(this.form);


            $.ajax({
                url: '/pred',
                type: 'POST',
                data: priceForm,
                processData: false,
                contentType: false,
                success: function (res) {
                    
                    data=`<p class="alert alert-success fs-4" role="alert">Your Predicted house price is <span class="fw-bold"> ₹${res} <span><p>`
                    $('#res').html(data);
                }

            })

    })
})