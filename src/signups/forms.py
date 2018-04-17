# -*- coding: utf-8 -*-

from django import forms

from .models import SighUp, Patient

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SighUp
        
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        labels = {
            "ivhun_type":"סוג האבחון (פרטי/עבור צד שלישי)",
            "full_name":"שם מלא",
            "patient_id":"תעודת זהות",
            "date_of_birth":"תאריך לידה",
            "address":"כתובת",
            "father_phone":"טלפון האב",
            "mother_phone":"טלפון האם",
            "grade":"כיתה",
            "educational_instatute":"מוסד חינוכי",
            "relevant_background":"רקע רלוונטי",
            "overall":"כללי",
            "thinking_skills":"כישורי חשיבה",
            "verbal_thinking_general":"חשיבה מילולית כללי",
            "verbal_thinking_conclusion":"חשיבה מילולית הסקת מסקנות",
            "verbal_thinking_gizra_shava":"חשיבה מילולית - גזרה שווה",
            "verbal_thinking_pitgamim":"חשיבה מילולית - פתגמים",
            "verbal_thinking_sivug":"חשיבה מילולית - סיווג",
            "verbal_thinking_miyun":"חשיבה מילולית - מיון",
            "verbal_thinking_hagdara":"חשיבה מילולית - הגדרה",
            "verbal_thinking_mahutiyut":"חשיבה מילולית מהותיות",
            "verbal_thinking_nirdfot":"חשיבה מילולית - מילים נרדפות",
            "verbal_thinking_nigudim":"חשיבה מילולית - ניגודים",
            "yeda_ortography_general":"ידע אורטוגרפי - כללי",
            "yeda_ortography_kriat_milim_beheksher_diyuk":"ידע אורטורפי - קריאת מילים בהקשדר דיוק",
            "yeda_ortography_kriat_milim_bodedot_diyuk":"ידע אורטוגרפי -קריאת מילים בודדות דיוק",
            "yeda_ortography_kriat_milot_tefel_diyuk":"ידע אורטוגרפי - קריאת מילות תפל דיוק",
            "yeda_ortography_kriat_itzurim_vetnuot_diyuk":"ידע אורטוגרפי - עיצורים ותנועות דיוק",
            "yeda_ortography_kriat_milim_beheksher_ketzev":"ידע אורטוגרפי - קריאת מילים בהקשר קצב",
            "yeda_ortography_kriat_milim_bodedot_ketzev":"ידע אורטוגרפי - קריאת מילים בודדות קצב",
            "yeda_ortography_kriat_milot_tefel_ketzev":"ידע אורטוגרפי - קריאת מילות תפל קצב",
            "yeda_ortography_kriat_itzurim_vetnuot_ketzev":"ידע אורטוגרפי - קריאת עיצורים ותנועות קצב",
            "havanat_hanishma":"הבנת הנשמע",
            "haarahat_kosher_ktiva":"הערכת כושר כתיבה",
            "mudaut_fonologit":"מודעות פונולוגית",
            "ran_test": "מבחן RAN",
            "shetef_miluli": "שטף מילולי",
            "eranut_morpho_tahbirit": "ערנות מורפו-תחבירית",
            "eranut_tahbirit": "ערנות תחבירית",
            "kidron": "מבחן קדרון",
            "rey": "מבחן ריי",
            "tifkudim_nihuliyim_hazutiim_merhaviim": "תפקודים ניהוליים חזותיים מרחביים",
            "shlifa_mehazikaron": "שליפה מהזיכרון",
            "yahalom": "יהלום",
            "five_nine_two": "592",
            "conclusion": "סיכום",
            "hamlatzot": "המלצות",
        }
        
