from django.shortcuts import render
from django.http import HttpResponse
import tensorflow as tf
from django.http import JsonResponse

def home(request):
    data=request.GET.copy()
    data['result']=predictwithkeras(data['first'], data['second'])
    return render(request, 'hello/home.html', context=data)
    
def form(request):
    return render(request, 'hello/form.html')
def predictwithkeras(first, second):
    new_model=tf.keras.models.load_model('hello/new_model.h5')
    params=[int(first), int(second)]
    result=new_model.predict([params])
    return result
def template(request):
    return render(request, 'hello/template.html')

#def simpleapi(request):
#    name01 = request.GET['name']
#    age02 = request.GET['age']
#    requestDict = request.GET
#    result = int(age02) + 5
#    requestDict = {‘result’:result}
#    return JsonResponse(requestDict)


# Create your views here.
