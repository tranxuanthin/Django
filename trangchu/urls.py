from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views 

urlpatterns = [ 
    path('',views.index,name='trangchu'),
    path('chitietsanpham/<int:id>/',views.chitietsanpham,name='chitietsp'),
    path('dangnhap/',views.dangnhap,name='dangnhap'),
    path('dangki/',views.dangki,name='dangki'),
    path('yeucaudangnhap/',views.yeucaudangnhap,name='yeucaudn'),
    path('dangkithanhvien/',views.dangkithanhvien,name='dangkithanhvien'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('giohang/',views.giohang,name='giohang'),
    path('addcart/',views.addcart,name='addcart'),
   path('xoagiohang/',views.xoagiohang,name='xoagiohang'),
]
