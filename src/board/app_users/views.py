from django.shortcuts import render

from .forms import AuthForm, RegisterForm, RestorePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from app_users.models import Profile

from django.core.mail import send_mail
from django.contrib.auth.models import User

from django.core.cache import cache



# Create your views here.
def login_view(request):

    if request.method == 'POST': # для POST пытаемся аутентифицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно вошли в систему!')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учётная запись пользователя не активна!')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля!')
    else: # для всех остальных запросов просто отображаем саму страницу логина
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)
    
    
# class AnotherLoginView(LoginView):

    # template_name = 'users/login.html'
    
    
class MainView(View):

    def get(self, request):
        return render(request, 'main.html')
        
        
def logout_view(request):

    logout(request)
    return HttpResponse('Вы успешно вышли из своей учётной записи!')
    
    
# class AnotherLogoutView(LogoutView):

    # #template_name = 'users/logout.html'
    # next_page = '/'
    
    
def register_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
    
    
def another_register_view(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        #form = RegisterForm()
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
    
def restore_password(request):
    
    if request.method == 'POST':
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            new_password = User.objects.make_random_password()
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject='Восстановление пароля!',
                message='ТЕСТ',
                from_email='admin@company.com',
                recipient_list=[form.cleaned_data['email']]
            )
            return HttpResponse('Письмо с новым паролем было успешно отправлено!')
    restore_password_form = RestorePasswordForm()
    context = {
        'form': restore_password_form
    }
    return render(request, 'users/restore_password.html', context=context)
    
    
def user_account(request):

    username = request.user.username
    balance = get_balance()
    
    promotions_cache_key = 'promotions:{}'.format(username)
    offers_cache_key = 'offers:{}'.format(username)
    promotions = get_promotions()
    offers = get_offers()
    
    user_account_cache_data = {
        promotions_cache_key: promotions,
        offers_cache_key: offers
    }
    cache.set_many(user_account_cache_data)
    payment_history = get_payment_history()
    
    return render(request, 'users/account.html', context={
        'balance': balance,
        'promotions': promotions,
        'offers': offers,
        'payment_history': payment_history
    })
    
    
def update_user_account(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()