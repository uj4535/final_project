from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from sklearn.externals import joblib
import tensorflow as tf
import numpy as np
import pandas as pd



#def home(request):
#    data=request.GET.copy()
#    data['result']=predmodel(data['first'], data['second'])
#    return render(request, 'pred.html', context=data)
def form(request):
    return render(request, 'form.html')
def predmodel(request):
    new_model=tf.keras.models.load_model('/home/sundooedu/문서/DontBuyJustAdoptProject/finalproject/predict/new_model.h5')
    age=request.GET['age']
    weight=request.GET['weight']
    animal=request.GET['animal'] # 기본 개=1, 고양이=0
    color=request.GET['color']
    species=request.GET['species']
    neuteryn=request.GET['neuteryn']
    outer_health=request.GET['outer_health'] 
    inner_health=request.GET['inner_health']
    disable=request.GET['disable']
    personality=request.GET['personality']
    care=request.GET['care']
    sex=request.GET['sex']

    df=pd.DataFrame({'age':[age], 'weight':[weight], 'animal':[animal], 'color':[color], 'species':[species], 'neuteryn':[neuteryn], 'outer_health': [outer_health], 'inner_health':[inner_health] , 'disable':[disable], 'personality': [personality], 'care':[care], 'sex':[sex]})
    dummies=pd.get_dummies(df, columns=['animal', 'color', 'species', 'neuteryn', 'outer_health', 'inner_health', 'disable', 'personality', 'care', 'sex'], drop_first=True)

    if animal=0:
        dummies['animal_1']=0
    
    for i in (1,4):
        if color=i:
    




    #params=[
    #    int(dummies['age']), float(dummies['weight']), int(dummies['animal_1']), int(dummies['color_1']), int(dummies['color_2']), int(dummies['color_3']), int(dummies['species_1']), int(dummies['species_2']),
    #    int(dummies['species_3']), int(dummies['species_4']), int(dummies['species_5']), int(dummies['species_6']), int(dummies['species_7']), int(dummies['species_8']), int(dummies['species_9']), int(dummies['species_10']),
    #    int(dummies['species_11']), int(dummies['species_12']), int(dummies['species_13']), int(dummies['species_14']), int(dummies['species_15']), int(dummies['species_16']), int(dummies['species_17']), int(dummies['species_18']),
    #    int(dummies['species_19']), int(dummies['species_20']), int(dummies['species_21']), int(dummies['species_22']), int(dummies['species_23']), int(dummies['species_24']), int(dummies['species_25']), int(dummies['species_26']),
    #    int(dummies['species_27']), int(dummies['species_18']), int(dummies['species_29']), int(dummies['species_30']), int(dummies['species_31']), int(dummies['species_32']), int(dummies['species_33']), int(dummies['species_34']),
    #    int(dummies['species_35']), int(dummies['species_36']), int(dummies['species_37']), int(dummies['species_38']), int(dummies['species_39']), int(dummies['species_40']), int(dummies['species_41']), int(dummies['species_42']),
    #    int(dummies['species_43']), int(dummies['species_44']), int(dummies['species_45']), int(dummies['species_46']), int(dummies['species_47']), int(dummies['species_48']), int(dummies['species_49']), int(dummies['species_50']),
    #    int(dummies['species_51']), int(dummies['species_52']), int(dummies['species_53']), int(dummies['species_54']), int(dummies['species_55']), int(dummies['species_56']), int(dummies['species_57']), int(dummies['species_58']),
    #    int(dummies['neuteryn_1']), int(dummies['neuteryn_2']), int(dummies['outer_health_1']), int(dummies['outer_health_2']), int(dummies['inner_health_1']), int(dummies['inner_health_2']), int(dummies['disable_1']), int(dummies['personality_1']), int(dummies['personality_2']),
    #    int(dummies['care_1']), int(dummies['sex_1']), int(dummies['sex_2'])
    #    ]
    prob=new_model.predict([params])
    result=np.where(prob>0.5,1,0)


    return render(request, "pred.html", {'result':result, 'probability':prob})
 





# Create your views here.
