$(document).ready(function () {
    
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value,10)
        value= isNaN(value) ? 0: value;
        if (value < 10){
            value ++ ;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value,10)
        value= isNaN(value) ? 0: value;
        if (value >1 ){
            value -- ;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.addToCart').click(function (e) { 
        e.preventDefault();
        
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add_to_cart/",
            data:{  
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status)
            }
        });
    });

    $('.addToWishlist').click(function (e) { 
        e.preventDefault();
        
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add_to_wishlist/",
            data:{  
                'product_id':product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status)
            }
        });
    });

    $('.changeQuantity').click(function (e) { 
        e.preventDefault();
        
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/update_cart/",
            data:{  
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                // alertify.success(response.status)
            }
        });
    });

    $(document).on('click','.delete-cart-item', function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "/delete_cart/",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status)
                $('.cartdata').load(location.href + " .cartdata")
            }
        });
    });
});

$(document).on('click','.delete-wishlist-item', function (e) {
    
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    
    $.ajax({
        method: "POST",
        url: "/delete_wishlist/",
        data: {
            'product_id': product_id,
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            alertify.success(response.status)
            $('.wishlistdata').load(location.href + " .wishlistdata")
        }
    });
});