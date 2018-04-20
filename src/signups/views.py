# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from .models import SighUp, Patient
from .forms import SignUpForm, PatientForm
from django.core.mail import send_mail
from django.conf import settings


 
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
        ivhunim = Patient.objects.all().order_by('-updated')
    else:
        ivhunim = Patient.objects.filter(owner=request.user).order_by('-updated')
    return render_to_response("allivhunim.html",
                              { 'ivhunim' : ivhunim },
                              context_instance=RequestContext(request))


def upsertivhun(request, ivhun_id):
    print ivhun_id
    if ivhun_id == '0':
        print ivhun_id
        pForm = PatientForm(request.POST or None)
    else:
        try:
            if request.user.is_superuser:
                ivhun = Patient.objects.get(id=ivhun_id)
            else:
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


def confirmdelete(request, ivhun_id):
    try:
        if request.user.is_superuser:
            ivhun = Patient.objects.get(id=ivhun_id)
        else:
            ivhun = Patient.objects.get(id=ivhun_id, owner=request.user)
    except Patient.DoesNotExist:
        return render_to_response('401.html',
                                    locals(),
                                    context_instance=RequestContext(request))
    return render_to_response("confirmdelete.html",
                                { 'ivhun':ivhun },
                                context_instance=RequestContext(request))



def deleteivhun(request, ivhun_id):
    if request.user.is_superuser:
        ivhun = Patient.objects.get(id=ivhun_id)
    else:
        return render_to_response('401.html',
                                    locals(),
                                    context_instance=RequestContext(request))
    Patient.objects.filter(id=ivhun_id).delete()

    return HttpResponseRedirect('/allivhunim/')
    
    
def emailivhun(request, ivhun_id):
    try:
        if request.user.is_superuser:
            ivhun = Patient.objects.get(id=ivhun_id)
        else:
            ivhun = Patient.objects.get(id=ivhun_id, owner=request.user)
        
    except Patient.DoesNotExist:
        return render_to_response('401.html',
                                    locals(),
                                    context_instance=RequestContext(request))
    subject =  u'אבחון - ' + ivhun.full_name 
    msg = 'Here is the message.'
    from_email = settings.EMAIL_HOST_USER
    to = [settings.EMAIL_HOST_USER]
    send_mail(subject,
              msg,
              from_email,
              to,
              fail_silently=False)
    
    return HttpResponseRedirect('/allivhunim/')




def copyivhun(request, ivhun_id):
    if request.user.is_superuser:
        ivhun = Patient.objects.get(id=ivhun_id)
    else:
        return render_to_response('401.html',
                                locals(),
                                context_instance=RequestContext(request))
    
    new_ivhun = Patient.objects.create(ivhun_type = ivhun.ivhun_type,
                                                    full_name = "copy - " + ivhun.full_name ,
                                                    patient_id = ivhun.patient_id,
                                                    date_of_birth = ivhun.date_of_birth,
                                                    address = ivhun.address,
                                                    father_phone = ivhun.father_phone,
                                                    mother_phone = ivhun.mother_phone,
                                                    grade = ivhun.grade,
                                                    educational_instatute = ivhun.educational_instatute,
                                                    relevant_background = ivhun.relevant_background,
                                                    overall = ivhun.overall,
                                                    thinking_skills = ivhun.thinking_skills,
                                                    verbal_thinking_general = ivhun.verbal_thinking_general,
                                                    verbal_thinking_conclusion = ivhun.verbal_thinking_conclusion,
                                                    verbal_thinking_gizra_shava = ivhun.verbal_thinking_gizra_shava,
                                                    verbal_thinking_pitgamim = ivhun.verbal_thinking_pitgamim,
                                                    verbal_thinking_sivug = ivhun.verbal_thinking_sivug,
                                                    verbal_thinking_miyun = ivhun.verbal_thinking_miyun,
                                                    verbal_thinking_hagdara = ivhun.verbal_thinking_hagdara,
                                                    verbal_thinking_mahutiyut = ivhun.verbal_thinking_mahutiyut,
                                                    verbal_thinking_nirdfot = ivhun.verbal_thinking_nirdfot,
                                                    verbal_thinking_nigudim = ivhun.verbal_thinking_nigudim,
                                                    yeda_ortography_general = ivhun.yeda_ortography_general,
                                                    yeda_ortography_kriat_milim_beheksher_diyuk = ivhun.yeda_ortography_kriat_milim_beheksher_diyuk,
                                                    yeda_ortography_kriat_milim_bodedot_diyuk = ivhun.yeda_ortography_kriat_milim_bodedot_diyuk,
                                                    yeda_ortography_kriat_milot_tefel_diyuk = ivhun.yeda_ortography_kriat_milot_tefel_diyuk,
                                                    yeda_ortography_kriat_itzurim_vetnuot_diyuk = ivhun.yeda_ortography_kriat_itzurim_vetnuot_diyuk,
                                                    yeda_ortography_kriat_milim_beheksher_ketzev = ivhun.yeda_ortography_kriat_milim_beheksher_ketzev,
                                                    yeda_ortography_kriat_milim_bodedot_ketzev = ivhun.yeda_ortography_kriat_milim_bodedot_ketzev,
                                                    yeda_ortography_kriat_milot_tefel_ketzev = ivhun.yeda_ortography_kriat_milot_tefel_ketzev,
                                                    yeda_ortography_kriat_itzurim_vetnuot_ketzev = ivhun.yeda_ortography_kriat_itzurim_vetnuot_ketzev,
                                                    havanat_hanishma = ivhun.havanat_hanishma,
                                                    haarahat_kosher_ktiva = ivhun.haarahat_kosher_ktiva,
                                                    mudaut_fonologit = ivhun.mudaut_fonologit,
                                                    ran_test = ivhun.ran_test,
                                                    shetef_miluli = ivhun.shetef_miluli,
                                                    eranut_morpho_tahbirit = ivhun.eranut_morpho_tahbirit,
                                                    eranut_tahbirit = ivhun.eranut_tahbirit,
                                                    kidron = ivhun.kidron,
                                                    rey = ivhun.rey,
                                                    tifkudim_nihuliyim_hazutiim_merhaviim = ivhun.tifkudim_nihuliyim_hazutiim_merhaviim,
                                                    shlifa_mehazikaron = ivhun.shlifa_mehazikaron,
                                                    yahalom = ivhun.yahalom,
                                                    five_nine_two = ivhun.five_nine_two,
                                                    conclusion = ivhun.conclusion,
                                                    hamlatzot = ivhun.hamlatzot,
                                                    owner = ivhun.owner)

    return HttpResponseRedirect('/allivhunim/')
