from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def calc(request):

    val1 = int(request.POST['num1'])
    op = (request.POST["op"])
    val2 = int(request.POST["num2"])


    if op == "+":
        res = val1 + val2
    elif op == "-":
        res = val1 - val2
    elif op == "*":
        res = val1 * val2
    elif op == "%":
        res = val1 % val2
    elif op == "/":
        res = val1 / val2
    else:
        res = "Invalid Operator"

    return render(request, "result.html", {"result" :res})