from django.http import HttpResponse, redirect

def login(request):
    return HttpResponse("欢迎登录")


def index(request):
    user = request.user
    if not user.is_auth():
        return redirect("/index")
