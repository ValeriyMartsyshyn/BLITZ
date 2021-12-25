$('input.filter').click( function(){
        let nature = document.forms[0][0].checked
        let memorial = document.forms[0][1].checked
        let art = document.forms[0][2].checked
        let gallery = document.forms[0][3].checked
        let history = document.forms[0][4].checked
        let price_min = document.forms[1][0].value
        let price_max = document.forms[1][1].value
        let rating = document.forms[1][2].value

        if (!price_min){
            price_min = 0
        }

        if (!price_max){
            price_max = 500
        }

        if (!rating){
            rating = 0
        }

        $.ajax({
            url: '../api/museums/filter',
            method: 'GET',
            data: {
            'nature': nature,
            'memorial': memorial,
            'art': art,
            'gallery': gallery,
            'history': history,
            'price_min': price_min,
            'price_max': price_max,
            'rating': rating
            }
        }).done(function(data, textStatus, jqXHR){
        $('div.content').html(jqXHR.responseText);
        });
    }
)