from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView

# Models
from App_Shop.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#from .forms import ReviewForm
#from django.contrib import messages


class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'
'''
def submit_review(request,product_id):
    template_name = 'App_Shop/product_detail.html'
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id,product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request,'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                date=ReviewRating()
                date.subject = form.cleaned_data['subject']
                date.rating = form.cleaned_data['subject']
                date.review = form.cleaned_data['subject']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request,'Thank you! Your review has been submitted.')
                return redirect(url)
'''
