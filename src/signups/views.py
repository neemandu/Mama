# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import SighUp, Patient
from .forms import SignUpForm, PatientForm
from django.core.mail import send_mail
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import registerFontFamily,registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT
from django.contrib.auth.models import User
from smtplib import SMTPException
from reportlab.lib import colors  


def downloadivhun(request, ivhun_id):
    doc = SimpleDocTemplate("somefilename.pdf")
    styles = getSampleStyleSheet()
    Story = [Spacer(1,2*inch)]
    style = styles["Normal"]
    for i in range(100):
       bogustext = ("This is Paragraph number %s.  " % i) * 20
       p = Paragraph(bogustext, style)
       Story.append(p)
       Story.append(Spacer(1,0.2*inch))
    doc.build(Story)

    fs = FileSystemStorage("/tmp")
    with fs.open("somefilename.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        return response

    return response
"""
    if request.user.is_superuser:
        ivhun = Patient.objects.get(id=ivhun_id)
        
        response = HttpResponse(content_type='application/pdf')
        file_name = ivhun.patient_id + '".pdf"'
        response['Content-Disposition'] = 'attachment; filename='+ file_name
        registerFont(TTFont("Times_New_Roman", "Times_New_Roman.ttf"))
        
        canv = Canvas(response, pagesize = A4)

        canv.setFont("Times_New_Roman", 15)
        #date
        canv.drawString(30,750,ivhun.timestamp.strftime("%d/%m/%Y"))
        #subject
        canv.setFont("Times_New_Roman", 24)
        canv.drawString(150,710,"יטקדיד ןוחבא ךמס לע תעד תווח")
        canv.line(145,705,410,705)
        
        canv.setFont("Times_New_Roman", 12)
        canv.drawRightString(500,650,":קדבנה םש")
        canv.drawRightString(430,650, ivhun.full_name[::-1])
        canv.drawRightString(500,630,":תוהז תדועת")
        canv.drawRightString(430,630, ivhun.patient_id[::-1])
        canv.drawRightString(500,610,":הדיל ךיראת")
        canv.drawRightString(430,610, ivhun.date_of_birth.strftime("%d/%m/%Y"))
        canv.drawRightString(500,590,":תבותכ")
        canv.drawRightString(430,590, ivhun.address[::-1])
        canv.drawRightString(500,570,":התיכ")
        canv.drawRightString(430,570, ivhun.grade[::-1])
        canv.drawRightString(500,550,":ידומיל דסומ")
        canv.drawRightString(430,550, ivhun.educational_instatute[::-1])

        canv.drawRightString(500,520,":יטנוולר עקר")
        canv.line(450,517,500,517)
        
        styleSheet = getSampleStyleSheet()
        style = ParagraphStyle(name='Normal',
                                  fontName='Times_New_Roman',
                                  fontSize=12,
                                  leading=12,
                                  alignment=TA_RIGHT)
        reversed = ivhun.relevant_background[::-1].replace("\n", "<br />")
        
        rev= reverseParagraph(reversed)
        P=Paragraph(rev ,style)
        
        aW = 500    # available width and height
        aH = 515
        
        w,h = P.wrap(aW, aH)    # find required space
        if w<=aW and h<=aH:
            aH = aH - h         # reduce the available height
            P.drawOn(canv,0,aH)           
        else:
            raise ValueError, "Not enough room"
        
        height = aH - 20
        canv.drawRightString(500,height,":תיללכ תומשרתה")
        canv.line(430,height - 3,500,height - 3)
        
        reversed = ivhun.overall[::-1].replace("\n", "<br />")
        
        rev= reverseParagraph(reversed)
        P=Paragraph(rev ,style)
        aH = aH - 25
        w,h = P.wrap(aW, aH)    # find required space
        if w<=aW and h<=aH:
            aH = aH - h         # reduce the available height
            P.drawOn(canv,0,aH)           
        else:
            raise ValueError, "Not enough room"
        
        height = aH - 20
        canv.drawRightString(500,height,":הבישח ירושיכ")
        canv.line(430,height - 3,500,height - 3)
        
        reversed = ivhun.thinking_skills[::-1].replace("\n", "<br />")
        
        rev= reverseParagraph(reversed)
        P=Paragraph(rev ,style)
        aH = aH - 25
        w,h = P.wrap(aW, aH)    # find required space
        if w<=aW and h<=aH:
            aH = aH - h         # reduce the available height
            P.drawOn(canv,0,aH)           
        else:
            raise ValueError, "Not enough room"
        
        height = aH - 20
        canv.drawRightString(500,height,":תילולימ הבישח")
        canv.line(430,height - 3,500,height - 3)
        
        reversed = ivhun.yeda_ortography_general[::-1].replace("\n", "<br />")
        
        rev= reverseParagraph(reversed)
        P=Paragraph(rev ,style)
        aH = aH - 25
        w,h = P.wrap(aW, aH)    # find required space
        if w<=aW and h<=aH:
            aH = aH - h         # reduce the available height
            P.drawOn(canv,0,aH)           
        else:
            raise ValueError, "Not enough room"
        
        height = aH - 20
        canv.drawRightString(500,height,":טבלה")
        canv.line(430,height - 3,500,height - 3)
        data=[(1,2),(3,4)]
        table = Table(data, colWidths=200 , rowHeights=30)
        table.setStyle(TableStyle([
                       ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))
        aH = aH - 30
        w,h = table.wrap(aW, aH)    # find required space
        if w<=aW and h<=aH:
            aH = aH - h         # reduce the available height
            table.drawOn(canv,80,aH)           
            
        else:
            raise ValueError, "Not enough room"
        canv.save()
        
        return response
        
    return render_to_response('401.html',
                                            locals(),
                                            context_instance=RequestContext(request))
"""

def reverseParagraph(p):
    newWord = 6
    partWord = ""
    completeWord = ""
    for i in range(0, len(p)):        
        if newWord  < 6:
            newWord = newWord + 1
            continue
        c = p[i]
        if i == (len(p) - 1):
            partWord += c
            completeWord = partWord + "<br />" + completeWord
        if c != '<':
           partWord += c
        elif i + 5 < len(p) and p[i : (i + 6)] == "<br />":
            completeWord = partWord + "<br />" + completeWord
            partWord = ""
            newWord  = 0
        
    return completeWord

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
    if request.user.is_superuser:
        ivhun = Patient.objects.get(id=ivhun_id)
        user = User.objects.get(id=ivhun.owner.id)
    else:
        return render_to_response('401.html',
                                locals(),
                                context_instance=RequestContext(request))
    subject =  u'אבחון - ' + ivhun.full_name
    msg = U"שלום,\n\n"
    msg += U'האבחון של ' + ivhun.full_name + U' מוכן,' + "\n"
    msg += U"לצפייה באבחון, ניתן להיכנס ל- www.ayaneeman.co.il" + "\n"
    msg += U"תחת \"האבחונים שלי\":" + "\n\n"
    msg += U"שם משתמש: " + user.username + "\n"
    msg += U"שם סיסמא: " + user.username + "\n\n"
    msg += U"אני זמינה לכל שאלה!\n\n"
    msg += U"איה."
    from_email = settings.EMAIL_HOST_USER
    to = [settings.EMAIL_HOST_USER]
    try:
        send_mail(subject,
                  msg,
                  from_email,
                  to,
                  fail_silently=False)
        messages.success(request, '!קישור לאבחון נשלח בהצלחה')
    except SMTPException:
        messages.error(request, 'השליחה נכשלה')
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
