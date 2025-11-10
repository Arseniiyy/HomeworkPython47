from django.shortcuts import render

def product_list(request):
    products = [
        {'id':1,'name':'Телефон','price':10000},
        {'id':2,'name':'Ноутбук','price':50000},
        {'id':3,'name':'Наушники','price':3000},
    ]
    return render(request, 'products/list.html',{'products':products})

def product_detail(request,product_id):
    product = {
        'id':product_id,
        'name':f'Товар {product_id}',
        'price':product_id * 1000,
        'description':f'Описание товара{product_id}'

    }
    return render(request,'products/detail.html',{'product':product})

