from django.shortcuts import render
from .models import info
from .forms import TForm
from django.views import View
# Create your views here.
class index(View):
 def get(self, request):
  form = TForm()
  return render(request, 'index.html', {'form':form})

 def post(self, request):
      form = TForm(request.POST, request.FILES)
      if form.is_valid():
       form.save()
      return render(request, 'index.html', {'form':form})

class CandidateView(View):
  def get(self, request):
    # candidate = info.objects.get(pk=pk)
    farmer = info.objects.all()
    return render(request, 'detail.html',{'farmer':farmer})


class detailsView(View):
  def get(self,request,id):
    farmers = info.objects.filter(id=id)
    return render(request,'details.html',{'farmers':farmers})

