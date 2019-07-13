import base64
import logging

import openpyxl
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.urls import reverse

from Clustering import KMeansMethod
import pandas as pd

from Export import ExportSpreadSheet
from Import import SpreadSheet2DataFrame

from django.http import HttpResponse


def view_alpha(request):
    data_to_cluster = []

    columns_name = ['PROVEDOR', 'TIPO_ATIVO', 'INDEXADOR', 'QTDE.', 'RATING_AQUISICAO', 'rating_atual', 'EMISSOR',
                    'CODIGO', 'TAXA_EMISSAO', 'TAXA_AQUISICAO', 'PORC_INDEX_EMISSAO', 'PORC_INDEX_AQUISICAO',
                    'PU_AQUISICAO', 'PU_EMISSAO', 'DATA_EMISSAO', 'DATA_AQUISICAO', 'DATA_VENCIMENTO', 'NOME_MITRA',
                    'DU']

    df_to_cluster = pd.DataFrame(data_to_cluster, columns=columns_name)

    graphic = None

    return render(request, 'textos_alpha.html', {'graphic': graphic, 'tables': None})



def upload_spreadsheet_file(request):
    if "GET" == request.method:
        return HttpResponseRedirect(reverse("datas:home"))

    try:
        spreadsheet_file = request.FILES["spreadsheet_file"]
        if (not spreadsheet_file.name.endswith('.xlsx')):
            messages.error(request, 'File is not XLSX type')
            return HttpResponseRedirect(reverse("datas:home"))
        ss2df = SpreadSheet2DataFrame(spreadsheet_file)
        ss2df.converter()
        df_to_cluster = ss2df.getDataFrame()

        ratings = df_to_cluster['rating_atual'].dropna().unique()
        n_rating = ratings.shape[0]
        result = KMeansMethod(df_to_cluster[['DU', 'TAXA_AQUISICAO']], n_clusters=n_rating)
        result.startProcessing()

        tables = dict()
        df_to_cluster['Clusters'] = result.get_clusters()
        color = {1:'rgba(255, 0, 0, 1)', 2:'rgba(125, 0, 0, 1)', 3:'rgba(0, 255, 0, 1)',
                 4:'rgba(0, 125, 0, 1)', 5:'rgba(0, 0, 255, 1)', 6:'rgba(0, 0, 125, 1)',
                 7:'rgba(125, 125, 0, 1)', 8:'rgba(0, 125, 125, 1)', 0:'rgba(125, 0, 125, 1)'}

        for index, cluster in enumerate(df_to_cluster['Clusters'].unique()):
            dict_cluster = dict()
            dict_cluster['Data'] = dict()
            dict_cluster['Data'] = (df_to_cluster[df_to_cluster['Clusters'] == cluster].transpose().to_dict())
            dict_cluster['Color'] = color[index]
            dict_cluster['Name'] = cluster
            tables[index] = dict_cluster

        # this is my output data a list of lists
        ess = ExportSpreadSheet("Data")
        ess.addDataFrameTab(df_to_cluster, 'Clustered')
        # set the mime type so that the browser knows what to do with the file

        # set the file name in the Content-Disposition header
        return render(request, 'textos_alpha.html', {'tables': tables, 'datas': df_to_cluster[['DU','TAXA_AQUISICAO']].values})


    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))

    return HttpResponseRedirect(reverse("datas:home"))



def download_spreadsheet_file(request):
    if "GET" == request.method:
        return HttpResponseRedirect(reverse("datas:home"))

    try:
        spreadsheet_file = request.FILES["spreadsheet_file"]
        if (not spreadsheet_file.name.endswith('.xlsx')):
            messages.error(request, 'File is not XLSX type')
            return HttpResponseRedirect(reverse("datas:home"))
        ss2df = SpreadSheet2DataFrame(spreadsheet_file)
        ss2df.converter()
        df_to_cluster = ss2df.getDataFrame()

        ratings = df_to_cluster['rating_atual'].dropna().unique()
        n_rating = ratings.shape[0]
        result = KMeansMethod(df_to_cluster[['DU', 'TAXA_AQUISICAO']], n_clusters=n_rating)
        result.startProcessing()

        tables = list()
        df_to_cluster['Clusters'] = result.get_clusters()
        for cluster in df_to_cluster['Clusters'].unique():
            tables.append(df_to_cluster[df_to_cluster['Clusters'] == cluster].transpose() .to_dict())

        # this is my output data a list of lists
        ess = ExportSpreadSheet("Data")
        ess.addDataFrameTab(df_to_cluster, 'Clustered')
        # set the mime type so that the browser knows what to do with the file
        response = HttpResponse(ess.getSpreadSheet(),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        # set the file name in the Content-Disposition header
        response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format(ess.getFilename())

        return response


    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))

    return HttpResponseRedirect(reverse("datas:home"))