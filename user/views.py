from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("storeView")
        else:
            return render(request, "login.html", {
                "error": "bu kullani adi veya sifresi bulunmamaktadir"
            })
    else:
        return render(request, "login.html")






def registerUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "register.html", {
                    "error": "Bu kullanici adi ile kayidimiz mevcuttur.",
                    "username": username,
                    "email": email,
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "register.html", {
                        "error": "Bu kullanici email ile kayidimiz mevcuttur.",
                        "username": username,
                        "email": email,
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'register.html',{
                "error": "Parolaniz eslesmiyor",
                "username": username,
                "email": email
            })

    return render(request, "register.html")





def logoutUser(request):
    logout(request)
    return redirect("login")