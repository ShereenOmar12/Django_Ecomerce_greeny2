from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductImages ,Brand , Catergory
from django.db.models import Count , Q , F , Value
from django.db.models.functions import Concat
from django.db.models.aggregates import Min,Max,Sum,Avg,Count
# Create your views here.


def post_list(request):
    objects= Product.objects.all()
    #objects = Product.objects.filter(category__id__gt=3)
    #objects = Product.objects.filter(price__range=(30,50))
    #cobjects = Product.objects.filter(name__contains='sarah')
    #objects = Product.objects.filter(name__startswith='sa')
    #objects = Product.objects.filter(name__endswith='e')
    #objects = Product.objects.filter(desc__isnull='True')
    #objects = Product.objects.filter(quantity__gt=10 , price__gt=50)
    #objects = Product.objects.filter(Q(quantity__gt=10) | Q(price__gt=50))
    #objects = Product.objects.filter(Q(quantity__gt=10) & Q(price__gt=50))
    #objects = Product.objects.filter(Q(quantity__gt=10) & ~Q(price__gt=50))
    #objects = Product.objects.filter(quantity=F('price'))
    #objects = Product.objects.filter(quantity=F('category_id'))
    #objects = Product.objects.order_by('name','-price')
    #objects = Product.objects.all().order_by('-name')[:10]
    #objects = Product.objects.latest('name')
    #objects = Product.objects.earliest('name')

    #objects = Product.objects.all()[10:20]
    #dectionary data
    #objects = Product.objects.values('id','name','category__name')
    #tuple data
    #objects = Product.objects.values_list('id','name','category__name')
    #objects = Product.objects.values_list('id','name','category__name','brand')
    #objects = Product.objects.only('id','name')
    #objects = Product.objects.select_related('category').all() # with one to one relation 
    #objects = Product.objects.prefetch_related('category').all() # with many to many relation 
    #objects = Product.objects.annotate(is_new=Value(True))
    #objects = Product.objects.annotate(
    #   full_name = Concat('name',Value(''), 'flag'))
    #objects = Product.objects.aggregate(Sum('price') , Max('price'))
    #print(objects)
    #objects = Product.objects.all()
    objects = Product.objects.price_greater_than(40)

    #print(objects)



    





    return render(request , 'products/test_list.html',{'products':objects})





class ProductList(ListView):
    model=Product
    paginate_by=100

class ProductDetail(DetailView):
    model=Product


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        myproduct=self.get_object()
        context["images"]=ProductImages.objects.filter(product=myproduct)
        context["related"]=Product.objects.filter(category=myproduct.category)

        return context


class BrandList(ListView):
    model=Brand
    paginate_by=6



    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"]=Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context



class BrandDetail(DetailView):
    model=Brand 

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        brand=self.get_object()
        context["brand_products"]=Products.objects.filter(brand=brand)
        return context


class CategoryList(ListView):
    model=Catergory



    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["category"]=Catergory.objects.all().annotate(product_count=Count('product_catrgory'))
        return context
