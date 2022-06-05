from django.shortcuts import render
from django.http import HttpResponse
import json
import random


# Create your views here.
def home(request):
    return render(request,"index.html")
    

def generate(request):
    lower = 22
    upper = 78
    computerGuess = random.randint(lower, upper)
    print(computerGuess)
    return HttpResponse(json.dumps({'computerguess':computerGuess},indent=3),content_type='application/json')


def checkans(request):
    flag=int(request.GET['flag'])
    flag+=1
    userans=int(request.GET['userans'])
    computerguess=int(request.GET['computerguess'])
    if userans < 22 or userans >78:
        output="number entered is out of bound"

    elif computerguess == userans:
        output="Congratulations you won the game"
                            
    elif computerguess > userans:
        output="You guessed too small!, your guess is less than "
                            
    elif computerguess < userans:
        output="You Guessed too high!, your guess is more than "
                            
    if flag==5:
        output="you loose!"
    resultdict={'finalResult':output,'flag':flag}
    json_response=json.dumps(resultdict,indent=5)
    return HttpResponse(json_response,content_type='application/json')
                        
