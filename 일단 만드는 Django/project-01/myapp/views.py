from django.shortcuts import render

# 어떤 요청이 들어왔을 때 그 요청과 함께 first.html을 화면에 찍어주는 함수
def first(request):
    return render(request, 'first.html') 

    
def second(request):
    return render(request, 'second.html') 