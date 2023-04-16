from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView

from .forms import AccountForm
from .models import Profile, Account


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class AccountCreateView(UserPassesTestMixin, CreateView):
    model = Account
    fields = "username", "bio", "avatar"
    template_name = "myauth/account_form.html"
    success_url = reverse_lazy("myauth:accounts_list")

    def test_func(self):
        if self.request.user.is_superuser:
            return True


class AccountDetailsView(TemplateView):
    template_name = "myauth/account_details.html"
    queryset = Account.objects.prefetch_related("images")
    context_object_name = "users"


class AccountUpdateView(UpdateView):
    model = Account
    template_name_suffix = '_update_form'
    # template_name = 'myauth/marketProfile_update_form.html'
    form_class = AccountForm

    def get_success_url(self):
        return reverse(
            'myauth:account_details',
            kwargs={'pk': self.object.pk}
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class AccountsListView(ListView):
    template_name = 'myauth/accounts_list.html'
    context_object_name = 'users'
    queryset = Account.objects.all()


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)
        Account.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password2')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response

def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')

        return render(request, 'myauth/login.html')

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')

    return render(request, 'myauth/login.html', {"error": "Invalid login credentials"})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(reverse("myauth:login"))


class MyLogut_view(LogoutView):
    next_page = reverse_lazy("myauth:login")


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default value")
    return HttpResponse(f"Session value: {value!r}")
