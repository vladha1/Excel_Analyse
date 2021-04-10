from django.shortcuts import render
from django.shortcuts import HttpResponse

import openpyxl
import pandas as pd

def index(request):
    if "GET" == request.method:
        return render(request, 'myapp/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        excel_data=pd.read_excel(excel_file).describe().to_html()

        # getting all sheets
        
        # getting a particular sheet
        
        # iterating over the rows and
        # getting value from each cell in row
        
        return HttpResponse(excel_data)
        #return render(request, 'myapp/index.html', {"excel_data":excel_data})









