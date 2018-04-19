# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from .models import SighUp, Patient
from .forms import SignUpForm, PatientForm

 
def home(request):
    
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'thank you for joining')
        return HttpResponseRedirect('/thank-you/')
    
    return render_to_response("home.html",
                              locals(),
                              context_instance=RequestContext(request))
def thankyou(request):
    
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))
def allivhunim(request):
    
    if request.user.is_superuser:
        ivhunim = Patient.objects.all().order_by('timestamp')
    else:
        ivhunim = Patient.objects.filter(owner=request.user).order_by('timestamp')
    return render_to_response("allivhunim.html",
                              { 'ivhunim' : ivhunim },
                              context_instance=RequestContext(request))
def newpatient(request, ivhun_id):
    if ivhun_id == -1:
        pForm = PatientForm(request.POST or None)
    else:
        try:
            ivhun = Patient.objects.get(id=ivhun_id, owner=request.user)
            pForm = PatientForm(request.POST or None, instance=ivhun)
        except Patient.DoesNotExist:
            return render_to_response('401.html',
                                        locals(),
                                        context_instance=RequestContext(request))
       
    
    if pForm.is_valid():
        save_it = pForm.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('/allivhunim/')

    return render_to_response("newpatient.html",
                              locals(),
                              context_instance=RequestContext(request))
