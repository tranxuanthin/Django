from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from .models import List,Product
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
def index(request):
    _list = List.objects.all()
    _product = Product.objects.all()
    _danhsach = {
        'danhsach': list,
        'Product': _product
    }
    
    

    return render(request,"trangchu/index.html",_danhsach)
@login_required
def chitietsanpham(request,id):
    
    if request.user.is_authenticated:
        _sp = Product.objects.get(id=id)
        _sanpham = {
            'sanpham' : _sp
        }
        return render(request,"trangchu/chitietsp.html",_sanpham)
def dangnhap(request):
    return render(request,"trangchu/dangnhap.html")
def dangki(request):
    return render(request,"trangchu/dangky.html")


def yeucaudangnhap(request):
    _username = request.GET['name']
    _password = request.GET['password']
    _user = authenticate(request, username=_username, password=_password)
    if _user is not None:
        login(request,_user)
        request.session['user'] = _username
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('trangchu')
        
    else:
        return HttpResponse("alert('Dang nhap that bai')")
    # try:
    #     password1 = user.objects.get(password=password , username = username)
        
        
    #     return render(request,"trangchu/index.html",{'username': username})
    # except:
    #     return HttpResponse("Dang nhap that bai")
    

    # if username1 == user.objects.filter(username=username1):
    #     if password1 == user.objects.filter(password=password1):
    #         return HttpResponse(username1)
    # else:
    #     return HttpResponse("sai gi do roi ban")
        
   
def dangkithanhvien(request):
    _name = request.POST['name']
    _password = request.POST['password']
    _email = request.POST['email']
    _user = User.objects.create_user(_name,_email,_password)
    _user.save()
    return HttpResponse('dang ki thanh cong')

def logout_view(request):
    logout(request)
    _list = List.objects.all()
    _product = Product.objects.all()
    _danhsach = {
        'danhsach': list,
        'Product': _product
    }
    return render(request,"trangchu/index.html",_danhsach)
    

@login_required
def giohang(request):
    _total = 0
    
    try:
        cart = request.session['giohang']
        for key,value in cart.items():
            _total += int(value['price'])*int(value['num'])
    except:
        _total = 0
    return render(request,"trangchu/giohang.html",{'total':_total})
_cart ={}
# cart ={1:{
#                 'id' : 0,
#                 'num' : 0
#         }}
@login_required
def addcart(request):
    if request.is_ajax():
        id = request.POST.get('id')
        sp = Product.objects.get(id=id)
        name = sp.name
        price = sp.price
        promotion = sp.promotion
        num = request.POST.get('num')
        statuss = False
        for i, element in _cart.items():
        
            try:
                print('hello try')
                if element['name'] == name:
                    x = element['num']
                   
                    _cart[i]['num'] =  int(num) + int(x)
                   
                    statuss = True     
               
            except:
                print('hello except')
                
                
        if statuss == False:
            x = len(_cart)
            _cart[x+1]={'name': name, 'num' : num, 'price' : price, 'promotion' : promotion}
        print('###cart')
        print(_cart)    
        request.session['giohang'] = _cart
        cartinfo = request.session['giohang']
        # html = request.render_to_string("trangchu/giohang.html",cartinfo)
        
    else:
        message = "Not ajax"
    return HttpResponse(json.dumps( cartinfo ))
    # return HttpResponse(html)
def xoagiohang(request):
    if request.is_ajax():
        _cart = {}
        try:
            del request.session['giohang']
            print(_cart)
        except:
            pass
        return HttpResponse("da xoa")