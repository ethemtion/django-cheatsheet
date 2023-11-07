from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from account.forms import LoginUserForm

# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Giriş başarılı")
                # return redirect("index")

                nextUrl = request.GET.get("next", None)
                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else:
                return render(request, "account/login.html", {"form": form})
        else:
            return render(request, "account/login.html", {"form": form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form": form})


def user_logout(request):
    messages.add_message(request, messages.SUCCESS, "Çıkış başarılı")
    logout(request)
    return redirect("index")


def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        # HOCA BÖYLE KOD MU YAZILIR AQ
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(
                    request, "account/register.html", {"error": "Username is taken."}
                )
            else:
                if User.objects.filter(email=email).exists():
                    request, "account/register.html", {
                        "error": "Email is already in use."
                    }
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password
                    )
                    user.save()
                    return redirect("user_login")

        else:
            return render(
                request, "account/register.html", {"error": "Passwords dont match."}
            )

    else:
        return render(request, "account/register.html")
