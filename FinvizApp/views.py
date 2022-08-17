from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
import time
import json
from sqlalchemy.orm import sessionmaker, Session
import codecs


path = "postgresql://postgres:123@localhost:5432/Test_db"
engine = create_engine(path, echo=True)

def Fetch_Data_From_DB_Wiki():
    table_name = "wikipedia"
    meta = MetaData()
    table_entity = Table(table_name, meta, autoload=True, autoload_with=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    table_data = session.query(table_entity)
    return table_data

def Fetch_Data_From_DB_Detail():
    table_name = "details"
    meta = MetaData()
    table_entity = Table(table_name, meta, autoload=True, autoload_with=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    table_data = session.query(table_entity)
    return table_data
    #return HttpResponse("Details function")

def Search_for_Graph(symbol):
    pe =0
    eps_ttm = 0
    forward_pe = 0
    s=""
    for i,j in zip(Fetch_Data_From_DB_Wiki(),Fetch_Data_From_DB_Detail()):
        if i.symbol==symbol:
            s=i.symbol
            pe=j.pe
            eps_ttm=j.eps_ttm
            forward_pe=j.forward_pe
            break
    return {"symbol":s ,"pe":pe,"eps_ttm":eps_ttm,"forward_pe":forward_pe}

def Show_Details(request):
    stri=""
    return HttpResponse("Hellow Details function called")

def Show_Wikipedia(request):

    stri = ""
    dicti_my2 = {"data": []}
    for i in Fetch_Data_From_DB_Wiki():
        stri = str(i.id) + i.symbol
        dicti_my2['data'].append(stri)
        stri = ""
    return HttpResponse(json.dumps(dicti_my2['data']), content_type="application/json")

def page(request):
    table_wiki=Fetch_Data_From_DB_Wiki()
    table_detail=Fetch_Data_From_DB_Detail()
    symbol=[]
    pe=[]
    eps_ttm=[]
    forward_pe=[]
    for i,j in zip(table_wiki,table_detail):
        if i.id==j.fid:
            symbol.append(i.symbol)
            pe.append(j.pe)
            eps_ttm.append(j.eps_ttm)
            forward_pe.append(j.forward_pe)
    return render(request,"index.html",context={'mydata':zip(symbol,pe,eps_ttm,forward_pe)})


def Graph_data(request):
    symbol=""
    if request.method=="POST":
        symbol=request.POST.get('a')
    return render(request,'Graph.html',context=Search_for_Graph(symbol))



