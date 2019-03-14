from django.http import HttpResponse
import pandas as pd
import os

directory = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(directory, 'data')

# Create your views here.


def homepage(request):
    return HttpResponse("Hello World!!!")


def viewCSV(request):
    if 'filename' in request.GET and request.GET['filename']:
        filename = request.GET['filename']
        df = pd.read_csv(os.path.join(DATA_DIR, filename))
        return HttpResponse(
            df.to_json(orient='records'), content_type="application/json")
    else:
        return HttpResponse('Please submit a search term.')
