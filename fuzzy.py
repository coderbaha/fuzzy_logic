# -*- coding: utf-8 -*-

import skfuzzy as fuzz
import numpy as np
import skfuzzy.membership as mf
import matplotlib.pyplot as plt


def egitim(input_km,input_yil,input_vites,input_yakit):
    
    x_fiyat= np.arange(30000,450000,1)
    x_km= np.arange(0,400000,1)
    x_yil= np.arange(1999,2021,1)
    x_seri= np.arange(0,13,1)
    x_vites= np.arange(0,3,1)
    x_yakit= np.arange(0,3,1)


    km_dusuk= mf.trimf(x_km,[-1,40000,100000])
    km_orta= mf.trimf(x_km,[75000,110000,155000])
    km_yuksek= mf.trimf(x_km,[140000,200000,320000])

    yil_eski= mf.trimf(x_yil,[1999,2005,2009])
    yil_orta= mf.trimf(x_yil,[2007,2010,2016])
    yil_yeni= mf.trimf(x_yil,[2014,2017,2021])

    seri_eski= mf.trimf(x_seri,[0,2,6])
    seri_orta= mf.trimf(x_seri,[4,6,8])
    seri_yeni= mf.trimf(x_seri,[6,10,12])

    vites_manuel= mf.trimf(x_vites,[0,0,0])
    vites_oto= mf.trimf(x_vites,[1,1,1])
    vites_yarioto= mf.trimf(x_vites,[2,2,2])

    yakit_dizel= mf.trimf(x_yakit,[1,1,1])
    yakit_benzin= mf.trimf(x_yakit,[0,0,0])
    yakit_lpgbenzin= mf.trimf(x_yakit,[2,2,2])

    fiyat_ucuz=mf.trimf(x_fiyat,[35000,65000,80000])
    fiyat_orta=mf.trimf(x_fiyat,[70000,110000,140000])
    fiyat_pahali=mf.trimf(x_fiyat,[130000,170000,390000])



    input_seri=11


    fig,(ax0,ax1,ax2,ax3,ax4,ax5)=plt.subplots(nrows=6,figsize=(6,10))
    ax0.plot(x_km,km_dusuk,'r',linewidth=2,label='düşük')
    ax0.plot(x_km,km_orta,'g',linewidth=2,label='orta')
    ax0.plot(x_km,km_yuksek,'b',linewidth=2,label='yüksek')
    ax0.set_title("kilometre")
    ax0.legend()
    

    ax1.plot(x_yil,yil_eski,'r',linewidth=2,label='eski')
    ax1.plot(x_yil,yil_orta,'g',linewidth=2,label='orta')
    ax1.plot(x_yil,yil_yeni,'b',linewidth=2,label='yeni')
    ax1.set_title("yil")
    ax1.legend()
    
    ax2.plot(x_seri,seri_eski,'r',linewidth=2,label='eski')
    ax2.plot(x_seri,seri_orta,'g',linewidth=2,label='orta')
    ax2.plot(x_seri,seri_yeni,'b',linewidth=2,label='yeni')
    ax2.set_title("seri")
    ax2.legend()
    
    ax3.plot(x_vites,vites_manuel,'r',linewidth=2,label='manuel')
    ax3.plot(x_vites,vites_oto,'g',linewidth=2,label='oto')
    ax3.plot(x_vites,vites_yarioto,'b',linewidth=2,label='yarioto')
    ax3.set_title("vites")
    ax3.legend()
    
    ax4.plot(x_yakit,yakit_dizel,'r',linewidth=2,label='dizel')
    ax4.plot(x_yakit,yakit_benzin,'g',linewidth=2,label='benzin')
    ax4.plot(x_yakit,yakit_lpgbenzin,'b',linewidth=2,label='lpgbenzin')
    ax4.set_title("yakit")
    ax4.legend()
  
    ax5.plot(x_fiyat,fiyat_ucuz,'r',linewidth=2,label='ucuz')
    ax5.plot(x_fiyat,fiyat_orta,'g',linewidth=2,label='orta')
    ax5.plot(x_fiyat,fiyat_pahali,'b',linewidth=2,label='pahali')
    ax5.set_title("fiyat")
    ax5.legend()
    plt.show()
    
    



    km_fit_dusuk=fuzz.interp_membership(x_km,km_dusuk,input_km)
    km_fit_orta=fuzz.interp_membership(x_km,km_orta,input_km)
    km_fit_yuksek=fuzz.interp_membership(x_km,km_yuksek,input_km)

    yil_fit_eski=fuzz.interp_membership(x_yil,yil_eski,input_yil)
    yil_fit_orta=fuzz.interp_membership(x_yil,yil_orta,input_yil)
    yil_fit_yeni=fuzz.interp_membership(x_yil,yil_yeni,input_yil)

    seri_fit_eski=fuzz.interp_membership(x_seri,seri_eski,input_seri)
    seri_fit_orta=fuzz.interp_membership(x_seri,seri_orta,input_seri)
    seri_fit_yeni=fuzz.interp_membership(x_seri,seri_yeni,input_seri)

    vites_fit_manuel=fuzz.interp_membership(x_vites,vites_manuel,input_vites)
    vites_fit_oto=fuzz.interp_membership(x_vites,vites_oto,input_vites)
    vites_fit_yarioto=fuzz.interp_membership(x_vites,vites_yarioto,input_vites)

    yakit_fit_lpgbenzin=fuzz.interp_membership(x_yakit,yakit_lpgbenzin,input_yakit)
    yakit_fit_benzin=fuzz.interp_membership(x_yakit,yakit_benzin,input_yakit)
    yakit_fit_dizel=fuzz.interp_membership(x_yakit,yakit_dizel,input_yakit)


    rule1=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_eski, np.fmin( vites_fit_manuel,yakit_fit_benzin))),  fiyat_ucuz)
    rule2=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_eski, np.fmin(vites_fit_manuel,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule3=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_eski, np.fmin (vites_fit_manuel,yakit_fit_dizel))),  fiyat_orta)

    rule4=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_eski, np.fmin( vites_fit_oto,yakit_fit_benzin))),  fiyat_ucuz)
    rule5=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_eski, np.fmin(vites_fit_oto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule6=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_eski, np.fmin (vites_fit_oto,yakit_fit_dizel))),  fiyat_orta)


    rule7=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_eski, np.fmin( vites_fit_yarioto,yakit_fit_benzin))),  fiyat_orta)
    rule8=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_eski, np.fmin(vites_fit_yarioto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule9=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_eski, np.fmin (vites_fit_yarioto,yakit_fit_dizel))),  fiyat_orta)




    rule10=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_orta, np.fmin( vites_fit_manuel,yakit_fit_benzin))),  fiyat_orta)
    rule11=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_orta, np.fmin(vites_fit_manuel,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule12=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_orta, np.fmin (vites_fit_manuel,yakit_fit_dizel))),  fiyat_pahali)



    rule13=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_orta, np.fmin( vites_fit_yarioto,yakit_fit_benzin))),  fiyat_orta)
    rule14=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_orta, np.fmin(vites_fit_yarioto,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule15=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_orta, np.fmin (vites_fit_yarioto,yakit_fit_dizel))),  fiyat_pahali)


    rule16=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_orta, np.fmin( vites_fit_oto,yakit_fit_benzin))),  fiyat_pahali)
    rule17=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_orta, np.fmin(vites_fit_oto,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule18=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_orta, np.fmin (vites_fit_oto,yakit_fit_dizel))),  fiyat_pahali)


    rule19=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_yeni, np.fmin( vites_fit_oto,yakit_fit_benzin))),  fiyat_pahali)
    rule20=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_yeni, np.fmin(vites_fit_oto,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule21=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_yeni, np.fmin (vites_fit_oto,yakit_fit_dizel))),  fiyat_pahali)

    rule22=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_yeni, np.fmin( vites_fit_manuel,yakit_fit_benzin))),  fiyat_pahali)
    rule23=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_yeni, np.fmin(vites_fit_manuel,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule24=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_yeni, np.fmin (vites_fit_manuel,yakit_fit_dizel))),  fiyat_pahali)


    rule25=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_yeni, np.fmin( vites_fit_yarioto,yakit_fit_benzin))),  fiyat_pahali)
    rule26=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_yeni, np.fmin(vites_fit_yarioto,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule27=np.fmin(np.fmin(km_fit_dusuk,  np.fmin(yil_fit_yeni, np.fmin (vites_fit_yarioto,yakit_fit_dizel))),  fiyat_pahali)



    rule28=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_eski, np.fmin( vites_fit_manuel,yakit_fit_benzin))),  fiyat_ucuz)
    rule29=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_eski, np.fmin(vites_fit_manuel,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule30=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_eski, np.fmin (vites_fit_manuel,yakit_fit_dizel))),  fiyat_ucuz)

    rule31=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_eski, np.fmin( vites_fit_oto,yakit_fit_benzin))),  fiyat_ucuz)
    rule32=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_eski, np.fmin(vites_fit_oto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule33=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_eski, np.fmin (vites_fit_oto,yakit_fit_dizel))),  fiyat_orta)


    rule34=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_eski, np.fmin( vites_fit_yarioto,yakit_fit_benzin))),  fiyat_ucuz)
    rule35=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_eski, np.fmin(vites_fit_yarioto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule36=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_eski, np.fmin (vites_fit_yarioto,yakit_fit_dizel))),  fiyat_orta)




    rule37=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_orta, np.fmin( vites_fit_manuel,yakit_fit_benzin))),  fiyat_orta)
    rule38=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_orta, np.fmin(vites_fit_manuel,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule39=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_orta, np.fmin (vites_fit_manuel,yakit_fit_dizel))),  fiyat_pahali)



    rule40=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_orta, np.fmin( vites_fit_yarioto,yakit_fit_benzin))),  fiyat_orta)
    rule41=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_orta, np.fmin(vites_fit_yarioto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule42=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_orta, np.fmin (vites_fit_yarioto,yakit_fit_dizel))),  fiyat_orta)


    rule43=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_orta, np.fmin( vites_fit_oto,yakit_fit_benzin))),  fiyat_orta)
    rule44=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_orta, np.fmin(vites_fit_oto,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule45=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_orta, np.fmin (vites_fit_oto,yakit_fit_dizel))),  fiyat_pahali)


    rule46=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_yeni, np.fmin( vites_fit_oto,yakit_fit_benzin))),  fiyat_pahali)
    rule47=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_yeni, np.fmin(vites_fit_oto,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule48=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_yeni, np.fmin (vites_fit_oto,yakit_fit_dizel))),  fiyat_pahali)

    rule49=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_yeni, np.fmin( vites_fit_manuel,yakit_fit_benzin))),  fiyat_orta)
    rule50=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_yeni, np.fmin(vites_fit_manuel,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule51=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_yeni, np.fmin (vites_fit_manuel,yakit_fit_dizel))),  fiyat_orta)


    rule52=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_yeni, np.fmin( vites_fit_yarioto,yakit_fit_benzin))),  fiyat_pahali)
    rule53=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_yeni, np.fmin(vites_fit_yarioto,yakit_fit_lpgbenzin))),  fiyat_orta)
    rule54=np.fmin(np.fmin(km_fit_orta,  np.fmin(yil_fit_yeni, np.fmin (vites_fit_yarioto,yakit_fit_dizel))),  fiyat_pahali)



    rule55=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_eski, np.fmin( vites_fit_manuel,yakit_fit_benzin))),  fiyat_ucuz)
    rule56=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_eski, np.fmin(vites_fit_manuel,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule57=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_eski, np.fmin (vites_fit_manuel,yakit_fit_dizel))),  fiyat_ucuz)

    rule58=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_eski, np.fmin( vites_fit_oto,yakit_fit_benzin))),  fiyat_ucuz)
    rule59=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_eski, np.fmin(vites_fit_oto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule60=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_eski, np.fmin (vites_fit_oto,yakit_fit_dizel))),  fiyat_orta)


    rule61=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_eski, np.fmin( vites_fit_yarioto,yakit_fit_benzin))),  fiyat_ucuz)
    rule62=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_eski, np.fmin(vites_fit_yarioto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule63=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_eski, np.fmin (vites_fit_yarioto,yakit_fit_dizel))),  fiyat_orta)


    rule64=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_orta, np.fmin( vites_fit_manuel,yakit_fit_benzin))),  fiyat_orta)
    rule65=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_orta, np.fmin(vites_fit_manuel,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule66=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_orta, np.fmin (vites_fit_manuel,yakit_fit_dizel))),  fiyat_orta)


    rule67=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_orta, np.fmin( vites_fit_yarioto,yakit_fit_benzin))),  fiyat_orta)
    rule68=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_orta, np.fmin(vites_fit_yarioto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule69=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_orta, np.fmin (vites_fit_yarioto,yakit_fit_dizel))),  fiyat_orta)


    rule70=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_orta, np.fmin( vites_fit_oto,yakit_fit_benzin))),  fiyat_orta)
    rule71=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_orta, np.fmin(vites_fit_oto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule72=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_orta, np.fmin (vites_fit_oto,yakit_fit_dizel))),  fiyat_orta)


    rule73=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_yeni, np.fmin( vites_fit_oto,yakit_fit_benzin))),  fiyat_orta)
    rule74=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_yeni, np.fmin(vites_fit_oto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule75=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_yeni, np.fmin (vites_fit_oto,yakit_fit_dizel))),  fiyat_orta)

    rule76=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_yeni, np.fmin( vites_fit_manuel,yakit_fit_benzin))),  fiyat_orta)
    rule77=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_yeni, np.fmin(vites_fit_manuel,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule78=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_yeni, np.fmin (vites_fit_manuel,yakit_fit_dizel))),  fiyat_orta)


    rule79=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_yeni, np.fmin( vites_fit_yarioto,yakit_fit_benzin))),  fiyat_orta)
    rule80=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_yeni, np.fmin(vites_fit_yarioto,yakit_fit_lpgbenzin))),  fiyat_ucuz)
    rule81=np.fmin(np.fmin(km_fit_yuksek,  np.fmin(yil_fit_yeni, np.fmin (vites_fit_yarioto,yakit_fit_dizel))),  fiyat_orta)


    out_ucuz=np.fmax(rule1,np.fmax(rule2,np.fmax(rule4,np.fmax(rule5,np.fmax(rule8,np.fmax(rule28,np.fmax(rule29,np.fmax(rule30,np.fmax(rule31,np.fmax(rule32,np.fmax(rule34,np.fmax(rule35,np.fmax(rule38,np.fmax(rule41,np.fmax(rule55,np.fmax(rule56,np.fmax(rule57,np.fmax(rule59,np.fmax(rule61,np.fmax(rule62,np.fmax(rule64,np.fmax(rule65,np.fmax(rule68,np.fmax(rule71,np.fmax(rule74,np.fmax(rule77,rule80))))))))))))))))))))))))))
    out_orta=np.fmax(rule3,np.fmax(rule6,np.fmax(rule7,np.fmax(rule9,np.fmax(rule10,np.fmax(rule11,np.fmax(rule13,np.fmax(rule14,np.fmax(rule16,np.fmax(rule17,np.fmax(rule20,np.fmax(rule23,np.fmax(rule26,np.fmax(rule33,np.fmax(rule36,np.fmax(rule37,np.fmax(rule39,np.fmax(rule40,np.fmax(rule42,np.fmax(rule43,np.fmax(rule44,np.fmax(rule47,np.fmax(rule49,np.fmax(rule50,np.fmax(rule53,np.fmax(rule58,np.fmax(rule60,np.fmax(rule63,np.fmax(rule66,np.fmax(rule67,np.fmax(rule69,np.fmax(rule70,np.fmax(rule72,np.fmax(rule73,np.fmax(rule75,np.fmax(rule76,np.fmax(rule78,np.fmax(rule79,rule81))))))))))))))))))))))))))))))))))))))
    out_pahali=np.fmax(rule12,np.fmax(rule15,np.fmax(rule18,np.fmax(rule19,np.fmax(rule21,np.fmax(rule22,np.fmax(rule24,np.fmax(rule25,np.fmax(rule27,np.fmax(rule45,np.fmax(rule46,np.fmax(rule48,np.fmax(rule51,np.fmax(rule52,rule54))))))))))))))

    out_fiyat=np.fmax(out_ucuz,out_pahali)
    out_fiyat_2=np.fmax(out_fiyat,out_orta)
    
    def hesap():
        defuzzified=fuzz.defuzz(x_fiyat,out_fiyat_2,"centroid")
        return defuzzified

    
    return hesap()












