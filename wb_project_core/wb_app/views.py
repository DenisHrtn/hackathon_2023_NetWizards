from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from .forms import LoginForm, RegistrationForm, AddProductForm
from .models import Product


def index(request):
    context = {}
    return render(request, 'index.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('wb_app:index')
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wb_app:index')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def account_view(request):
    return render(request, 'account.html', {})


@login_required
def add_product(request):
    form_class = AddProductForm
    template_name = '#'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = get_context_data(**kwargs)
        w = context(title='Главная страница')
        return dict(list(context.items) + list(w.items))


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'title': product.title,
        'description': product.description,
        'price': product.price,
        'on_stock': product.on_stock,
        'available': product.available,
        'photo': product.photo
    }
    return render(request, 'product_detail.html', context)


def product_view(request):
    products = Product.objects.all()
    context = {}
    for index, product in enumerate(products, start=1):
        context[f'product_{str(index)}'] = {'title': product.title,
                                            'description': product.description}
    return render(request, 'product_view.html', context=context)


@login_required()
def logout(request):
    logout(request.user)
    return render(request, 'index.html', {})