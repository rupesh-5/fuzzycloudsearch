from django.conf.urls.static import static
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
import searchengine
import nn

e=searchengine.searcher('wikipedia.db')
allurls=e.getallurls("functional")

# Create your views here.

def home_view(request):
  return HttpResponse(request.method)

def search_string(request):
  query=request.GET['searchquery']
  data=e.query(query)
  context_dict={'results':data,'query':query}
  return render_to_response('results_page.html', context_dict)

def train_nn(request,page_alias,selected_result):
  network=nn.searchnet('nn.db')
  words=e.getwordids(page_alias)
  if(selected_result.endswith("/")):
    selected_result=selected_result[:-1]
  urlid=e.geturlid(selected_result)
  network.trainquery(words,allurls,urlid)
  context_dict={'link':selected_result}
  return render_to_response('redirect_page.html',context_dict)

def home_page(request):
  return render_to_response('home_page.html')

