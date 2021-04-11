from django.shortcuts import render
from django.shortcuts import HttpResponse

import openpyxl
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
def index(request):
    if "GET" == request.method:
        return render(request, 'myapp/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        def leftn(row):
            return str(row['IGP Date'])[0:7]

        excel_data=pd.read_excel(excel_file)
        excel_data['ddmm']=excel_data.apply(leftn,axis=1)

        describe=excel_data.describe().to_html()
        pd.options.display.float_format = '{:,.0f}'.format
        summary=excel_data.groupby(['Supplier Name'])['Total Value'].sum().reset_index().to_html()
        pd.options.display.float_format = '{:,.0f}'.format
        summary_date=excel_data.groupby(['ddmm'])['Total Value'].sum().reset_index().to_html()
        #summary['Value']=summary['Value'].astype(int)/100000


        response=HttpResponse()
        
        response.write("<h1>Statistics</h1>")
        response.write(describe)
        response.write("<BR/><H1>Summary by supplier</H1>")
        response.write(summary)
        response.write("<BR/><H1>Summary by Date</H1>")
        response.write(summary_date)
        
        return response









