from django import views
from django.shortcuts import render
import pandas as pd

# Create your views here.

def home(request):
    return render(request,'pagetemplate/home.html')

def scRNASeq_Report(request):
    return render(request,'pagetemplate/scRNASeq_Report.html')

def display(request):
    return render(request,'pagetemplate/display.html')

def display2(request):
    return render(request,'pagetemplate/display2.html')


def home(request):
    # Read and process the first CSV data file here with explicit data type specification
    csv_file = 'pagetemplate/data/DE_analysis_100.csv'
    csv_data = pd.read_csv(csv_file, dtype={'p_val': str, 'p_val_adj': str, 'GO_Biological_Process_2023_Term': str})
    data = csv_data.to_dict(orient='records')

    csv_file2 = 'pagetemplate/data/DEenrichR_Tables_Selected.csv'
    csv_data2 = pd.read_csv(csv_file2, dtype={'GO_Biological_Process_2023_Term': str,'GO_Biological_Process_2023_P_value':str,'GO_Biological_Process_2023_Adjusted_P_value':str})
    data2 = csv_data2.to_dict(orient='records')

    csv_file3 = 'pagetemplate/data/Hub_genes_kMEs_100.csv'
    csv_data3 = pd.read_csv(csv_file3)  # Specify data types as needed
    data3 = csv_data3.to_dict(orient='records')

    csv_file4 = 'pagetemplate/data/sc_Pathway_Analysis_Table_100.csv'
    csv_data4 = pd.read_csv(csv_file4, dtype={'Pval':str,'adjPval':str,})  # Specify data types as needed
    data4 = csv_data4.to_dict(orient='records')


    

    return render(request, 'pagetemplate/scRNASeq_Report.html', {'data': data, 'data2': data2, 'data3': data3, 'data4': data4})






import pandas as pd
from django.shortcuts import render

# Define a function to read and process CSV data
def read_csv_data(csv_file):
    csv_data = pd.read_csv(csv_file)
    return csv_data.to_dict(orient='records')

def Deanalysis(request):
    # Read and process the first CSV data file here
    csv_file1 = 'pagetemplate/data/DE_analysis_100.csv'
    data1 = read_csv_data(csv_file1)

    # Pass data1 to the template
    return {'data1': data1}

def DEenrich(request):
    # Read and process the DEenrich CSV data file
    csv_file2 = 'pagetemplate/data/DEenrichR_Tables_Selected.csv'
    data2 = read_csv_data(csv_file2)

    # Pass data2 to the template
    return {'data2': data2}

def Hub_genes_kMEs_100(request):
    # Read and process the DEenrich CSV data file
    csv_file3 = 'pagetemplate/data/Hub_genes_kMEs_100.csv'
    data3 = read_csv_data(csv_file3)

    # Pass data2 to the template
    return {'data3': data3}

def sc_Pathway_Analysis_Table_100(request):
    # Read and process the DEenrich CSV data file
    csv_file4 = 'pagetemplate/data/sc_Pathway_Analysis_Table_100.csv'
    data4 = read_csv_data(csv_file4)

    # Pass data2 to the template
    return {'data4': data4}


def combined_display(request):
    # Call Deanalysis and DEenrich views to get their respective data
    data1 = Deanalysis(request)
    data2 = DEenrich(request)
    data3 = Hub_genes_kMEs_100(request)
    data4 = sc_Pathway_Analysis_Table_100(request)


    # Combine the data from both views (data1 and data2) as needed
    combined_data = {}
    combined_data.update(data1)
    combined_data.update(data2)
    combined_data.update(data3)
    combined_data.update(data4)


    

    # Pass the combined data to the template
    return render(request, 'pagetemplate/display.html', combined_data)
