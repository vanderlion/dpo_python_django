from django.contrib.auth.views import LoginView
from django.urls import path
from .views import (
    login_view,
    logout_view,
    get_cookie_view,
    set_cookie_view,
    get_session_view,
    set_session_view,
    MyLogut_view,
    AboutMeView,
    RegisterView,
    AccountCreateView,
    AccountsListView,
    AccountDetailsView,
    AccountUpdateView,
)

app_name = 'myauth'

urlpatterns = [
    # path("login/", login_view, name="login"),
    path(
        "login/",
        LoginView.as_view(
            template_name="myauth/login.html",
            redirect_authenticated_user=True
        ),
        name="login"),
    path("logout/", MyLogut_view.as_view(), name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),

    path("account-create/", AccountCreateView.as_view(), name="account_create"),
    path("accounts-list/", AccountsListView.as_view(), name="accounts_list"),
    path("account-detail/<int:pk>/", AccountDetailsView.as_view(), name="account_details"),
    path("account-detail/<int:pk>/update/", AccountUpdateView.as_view(), name="account_update"),


    path("cookie/get", get_cookie_view, name="cookie-get"),
    path("cookie/set", set_cookie_view, name="cookie-set"),

    path("session/get", get_session_view, name="session-get"),
    path("session/set", set_session_view, name="session-set"),
]
