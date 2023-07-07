from django.urls import path,include

from e_learning.views.client import (
    home,about, shop, checkout, shopProductDetail,
    contact, coursCategorie,cart, cours, coursDetails,
    blog, blogDetails, examen, instructors,
    instructorDetails, becomeInstructor

)

urlpatterns = [

    path('', include('e_learning.urls.studentUrl')),

    path('',home, name='home'),
    path('about', about, name='about'),

    path('shop', shop, name='shop'),
    path('checkout', checkout, name='checkout'),
    path('cart', cart, name='cart'),
    path('shopProductDetail', shopProductDetail, name='shopProductDetail'),


    path('cours', cours, name='cours'),
    path('coursCategorie', coursCategorie, name='coursCategorie'),
    path('coursDetails', coursDetails, name='coursDetails'),

    path('blog', blog, name='blog'),
    path('blogDetails', blogDetails, name='blogDetails'),

    path('contact', contact, name='contact'),

    path('examen', examen, name='examen'),

    path('instructors', instructors, name='instructors'),
    path('instructorDetails', instructorDetails, name='instructorDetails'),
    path('becomeInstructor', becomeInstructor, name='becomeInstructor'),


]