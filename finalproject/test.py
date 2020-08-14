from sklearn.externals import joblib
import warnings
warnings.filterwarnings("ignore")


def predmodel(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12):
    # sex=request.GET['sex']
    # neuteryn=request.GET['neuteryn']
    # inner_health=request.GET['inner_health']
    # outer_health=request.GET['outer_health']
    # personality=request.GET['personality']
    # care=request.GET['care']
    # disable=request.GET['disable']

    model=joblib.load('predict/logis.pkl')
    params=[int(x1), int(x2), int(x3), int(x4), int(x5), int(x6), int(x7), int(x8), int(x9), int(x10), int(x11), int(x12)]
    result=model.predict([params])
    return result


predmodel(1,0,1,1,1,1,1,1,1,1,0,1)