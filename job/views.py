from django.shortcuts import render ,redirect
from .models import job
from django.core.paginator import Paginator
from .form import ApplyForm ,jobForm
from django.urls import reverse

def job_list(request):
    job_list = job.objects.all()

    
    paginator = Paginator(job_list, 2) # Show 1 jobs per page.
    page_number = request.GET.get('page')
    job_list = paginator.get_page(page_number)

    context = {'jobs': job_list} #template name
    return render(request,'job/job_list.html',context)


def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()


    else:
        form = ApplyForm()    
    context = {'job': job_detail , 'form':form} #template name
    return render(request,'job/job_detail.html',context)
   





def add_job(request):
   
    if request.method == 'POST':
        form = jobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))   
    else:
        form = jobForm()

    return render(request,'job/add_job.html',{'form':form}) #template name