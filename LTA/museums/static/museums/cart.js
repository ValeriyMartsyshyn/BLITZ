$('.add').click(function (){
    product = $(this).children('p').attr('id')

    $.ajax({
            url: '../api/checkout/add',
            method: 'GET',
            data: {
            'id': product
            }
        })
})

