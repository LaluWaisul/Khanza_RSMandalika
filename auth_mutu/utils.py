import base64
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
    

def get_chart(chart_type, data, **kwargs):
    # print(data['Indikator Mutu'])
    # print(data['numerator'])
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(15,8))
    if chart_type == 'bar':
        print('barchart')
        data.plot(kind='bar', figsize=(10,8))
        # plt.bar(data['numerator'], data['total_persen'])
    elif chart_type == 'line':
        print('pie chart')
        data.plot(kind='line', figsize=(12,8), marker='o', rot=90)
        plt.xticks(np.arange(13), data.index)
        plt.show()
    elif chart_type == '#3':
        print('line chart')
    else:
        print('ups ada kesalahan')
    
    plt.tight_layout()
    chart = get_graph()
    return chart

def get_chart_series(chart_type, data, set_indikator,**kwargs):
    # print(data['Indikator Mutu'])
    # print(data['numerator'])
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot()
    if chart_type == 'line':
        if set_indikator:
            data.plot(kind='line', figsize=(12,8), marker='o', rot=90, ax=ax)
            ax.legend([x[1] for x in data.columns])
        else:
            plt.plot(data.index, data['total_hari'], marker='o')
            ax.set_xlabel('Tanggal')
        # plt.xticks(np.arange(13), data.index)
        # plt.show()
    elif chart_type == '#3':
        print('pie chart')
    else:
        print('ups ada kesalahan')
    plt.tight_layout()
    chart = get_graph()
    return chart

def get_chart_series_bulan(chart_type, data, set_indikator,**kwargs):
    # print(data['Indikator Mutu'])
    # print(data['numerator'])
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot()
    if chart_type == 'line':
        if set_indikator:
            data.plot(kind='line', figsize=(12,8), marker='o', rot=90, ax=ax)
            ax.legend([x[1] for x in data.columns])
        else:
            plt.plot(data.index, data['total_hari'], marker='o')
            ax.set_xlabel('Bulan')
        # plt.xticks(np.arange(13), data.index)
        # plt.show()
    elif chart_type == '#3':
        print('pie chart')
    else:
        print('ups ada kesalahan')
    plt.tight_layout()
    chart = get_graph()
    return chart

def get_chart_instalasi(chart_type, data, **kwargs):
    # print(data['Indikator Mutu'])
    # print(data['numerator'])
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(15,8))
    if chart_type == 'bar':
        print('barchart')
        data.plot(kind='bar', figsize=(10,8))
        # plt.bar(data['numerator'], data['total_persen'])
    elif chart_type == 'line':
        print('pie line')
        data.plot(kind='line', figsize=(12,8), marker='o', rot=90)
        plt.xticks(np.arange(2), data.index)
        plt.show()
    elif chart_type == '#3':
        print('line chart')
    else:
        print('ups ada kesalahan')
    
    plt.tight_layout()
    chart = get_graph()
    return chart