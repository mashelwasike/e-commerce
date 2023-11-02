from django.urls import path,include
from . import views
from . import authview,cart,wishlist,checkout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home' ),
    path('collection/',views.collection,name='collection'),
    path('collection/<str:slug>/',views.collectionview,name='collectionview'),
    path('collection/<str:cate_slug>/<str:prod_slug>/', views.productview, name='productview'),

    path('product-list',views.productlist,name='productlist'),
    path('searchproduct',views.searchproduct,name='searchproduct'),

    path('register/',authview.register,name='signup'),
    path('login/',authview.loginview,name='login'),
    path('logout/',authview.logoutview,name='logout'),

    path('add_to_cart/',cart.cart,name="addtocart"),
    path('cart/',cart.viewcart,name="cart"),
    path('update_cart/',cart.update_cart,name="update"),
    path('delete_cart/',cart.deleteitem,name='delete'),

    path('wishlist/',wishlist.index, name='wishlist'),
    path('add_to_wishlist/',wishlist.addtowishlist,name='addwishlist'),
    path('delete_wishlist/',wishlist.deleteitem,name='deletewishlist'),

    path('check_out/',checkout.checkout_view,name='checkout'),
    path('placeorder/',checkout.placeorder,name='placeorder'),

    #reseting password
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="authentication/passwordreset.html"),name="reset_password"), 
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="authentication/passwordreset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="authentication/passwordreset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="authentication/passwordreset_done.html"),
         name="password_reset_complete")
]