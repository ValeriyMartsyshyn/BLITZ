$('.delete').unbind().click(function(){
    product = $(this).attr('id');

    $.ajax({
            url: '../api/checkout/delete',
            method: 'GET',
            data: {
            'id': product
            }
        })
})