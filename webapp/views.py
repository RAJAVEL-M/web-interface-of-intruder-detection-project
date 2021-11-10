from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from .models import detail
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import StreamingHttpResponse
import cv2
import numpy as np
import time
import pickle
import re

@csrf_exempt
def proj(request):
    if request.method=='POST':
        json_data=json.loads(request.body.decode("utf-8"))
        print(json_data.keys())
        dummy_frame=np.asarray(json_data['frame'])
        dummy_time=json_data['time']
        outfile=""
        print(dummy_time.split())
        for each in dummy_time.split():
            outfile=outfile+each
        "".join(e for e in outfile if e.isalnum())
        outfile=re.sub(':','',outfile)
        p='media/images/'
        outfile=p+outfile+'out.jpg'
        print(outfile)
        cv2.imwrite(outfile,dummy_frame.astype(np.uint8))
        print("outfile",outfile)
        newitem = detail(time=dummy_time,frame=outfile)
        newitem.save()
        return StreamingHttpResponse('it was post request')
    else:
        obj=detail.objects.all()
        return render(request,'htmlfile.html',{'obj':obj})


