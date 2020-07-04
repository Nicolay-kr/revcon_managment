from django.shortcuts import render
from . import models
from django.shortcuts import redirect
from .forms import OrderForm
from django.views.generic import View
from django.core.mail import send_mail


class Index(View):
    def get(self, request):
        return render(request, 'mainsite/index.html')

# class CreateOrder(View):
#
#     def get(self, request):
#         form = OrderForm()
#         return render(request, 'mainsite/index.html', context={'form': form})
#
#     def post(self, request):
#         bound_form = OrderForm(request.POST)
#
#         if bound_form.is_valid():
#             new_order = bound_form.save()
#
#             return redirect('mainsite:index_url')
#
#         return render(request, 'mainsite:index_url',
#                       context={'form': bound_form})
def forma(request,string = '#'):
    if request.method == "POST":
        user = models.Order.objects.create(first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        mob_number=request.POST['mobile'],
        message=request.POST['message']
        )
        send_mail('order','message','email',
        ['nicolay.krischenovich@gmail.com'], fail_silently=False,)
        return render(request, 'mainsite/index.html')
