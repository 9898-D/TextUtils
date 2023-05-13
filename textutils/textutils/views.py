# Create By Me Myself This Views.py
import os.path

from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("Hello Dhruv How ARE yOU")

# def add(request):
#     return HttpResponse(1+1)
#
# def htmlres(request):
#     return HttpResponse("<h1> Sexy Dhruv </h1>")
#
# def task(request):
#     # md=os.path.dirname('D:/Django_Full_Course/textutils/textutils/self.txt')
#     # file_nm=os.path.join(md,'self.txt')
#     file_read=open('D:/Django_Full_Course/textutils/textutils/self.txt','r')
#     file_read_v=file_read.read()
#     # with open('self.txt','r') as f:
#     #     tk=f.read()
#     return HttpResponse(file_read_v)
#
# def task1(request):
#     return HttpResponse("<a href='https://openai.com/blog/chatgpt'> CHAT GPT LOGIN </a>")


# TODO ANOTHER TASK ------

def index(request):
    # info={'name':'Dhruv','Place':'Ahmedabad'}
    return render(request,'index.html')

def analyse(request):
    print(request.POST.get('text', 'default'))
    tt=request.POST.get('text','default')
    print(tt)
    res1=request.POST.get('removepun','off')
    res2=request.POST.get('capitalizr','off')
    res3=request.POST.get('charzount','off')
    res4=request.POST.get('spaceremove','off')
    if res1=='on':
        # user_txt = request.POST.get('text', 'default')
        analyzed_txt=tt.replace(':','').replace(',','').replace('"','').replace("'","").replace(';','').replace('!','')
        pass_dict={'input_text':tt,'analyzed_text':analyzed_txt,'purpose':'Remove Punctuations'}
        tt = analyzed_txt
        # return render(request,'analyze.html',pass_dict)
    if res2=='on':
        # user_txt = request.POST.get('text', 'default')
        analyzed_txt =tt.capitalize()
        pass_dict = {'input_text': tt, 'analyzed_text': analyzed_txt,'purpose':'CAPITALIZE'}
        tt = analyzed_txt
        # return render(request, 'analyze.html', pass_dict)
    if res3=='on':
        # user_txt = request.POST.get('text', 'default')
        analyzed_txt = len(tt)
        pass_dict = {'input_text': tt, 'analyzed_text': analyzed_txt,'purpose':'CHAR COUNT'}
        tt = analyzed_txt
        # return render(request, 'analyze.html', pass_dict)
    if res4=='on':
        # user_txt = request.POST.get('text', 'default')
        analyzed_txt = tt.replace(' ','')
        pass_dict = {'input_text': tt, 'analyzed_text': analyzed_txt,'purpose':'SPACE REMOVE'}
        tt=analyzed_txt

    if res4 != 'on' and res1 != 'on' and res2 != 'on' and res3 != 'on':
        return render(request,'Error.html')


        # return render(request, 'analyze.html', pass_dict)
    return render(request, 'analyze.html', pass_dict)

# def capitalfirst(request):
# #     print(request.GET.get('text','default'))
# #     tt=request.GET.get('text','default')
# #     ctt=tt.capitalize()
# #     return HttpResponse(f"capitalfirst You Capitilize text is {ctt} <br> <a href='/'> Back </a>")
# #
# # def spaceremove(request):
# #     return HttpResponse("spaceremove <a href='/'> Back </a>")
# #
# # def charcount(request):
# #     return HttpResponse("charcount <a href='/'> Back </a>")
#
