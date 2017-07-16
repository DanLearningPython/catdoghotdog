from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from .predict import CatDogHotDog
import cv2
import numpy as np    
import json

# Create your views here.
def index(request):
	return render(request, 'homepage.html', {'data': '','page_name' :'Home'})

def predict(request):

	results = None
	upload_folder = "classify/uploads/"

	if request.method == 'POST' and request.FILES['predict']:
		myfile = request.FILES['predict']
		fs = FileSystemStorage(
			location="classify/uploads"
		)
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)

		predict_model = CatDogHotDog()
		results = predict_model.run_prediction(upload_folder+filename)

		results = json.dumps(results)

		#cleanup uploaded file 
		fs.delete(filename)

	return HttpResponse(results, content_type="application/json")