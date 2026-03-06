import math
import tkinter as tk
from tkinter import ttk

# ----------------------------
# CONVERSIONES
# ----------------------------

def conv_long(v,u):
    if u=="m": return v
    if u=="cm": return v/100
    if u=="in": return v*0.0254

def conv_mom(v,u):
    if u=="N.m": return v
    if u=="lbf.in": return v*0.113

def conv_stress(v,u):
    if u=="Pa": return v
    if u=="MPa": return v*1e6
    if u=="psi": return v*6894.76
    if u=="kpsi": return v*6.89476e6

def mostrar_esfuerzo(pa):

    if unidad_result.get()=="Pa":
        return f"{pa:.2e} Pa"

    if unidad_result.get()=="MPa":
        return f"{pa/1e6:.3f} MPa"

    if unidad_result.get()=="psi":
        return f"{pa/6894.76:.2f} psi"

    if unidad_result.get()=="kpsi":
        return f"{pa/6.89476e6:.3f} kpsi"

# ----------------------------
# CALCULO
# ----------------------------

def calcular():

    D = conv_long(float(eD.get()),u_long.get())
    d = conv_long(float(ed.get()),u_long.get())
    r = conv_long(float(er.get()),u_long.get())

    Ma = conv_mom(float(eMa.get()),u_mom.get())
    Mm = conv_mom(float(eMm.get()),u_mom.get())
    Ta = conv_mom(float(eTa.get()),u_mom.get())
    Tm = conv_mom(float(eTm.get()),u_mom.get())

    Sut = conv_stress(float(eSut.get()),u_esf.get())
    Sy = conv_stress(float(eSy.get()),u_esf.get())
    Se = conv_stress(float(eSe.get()),u_esf.get())

# ----------------------------
# RELACIONES GEOMETRICAS
# ----------------------------

    Dd = D/d
    rd = r/d

# ----------------------------
# Kt AUTOMATICO
# ----------------------------

    if modoKt.get()=="Automatico":

        Kt = 1 + 2.7*((Dd-1)**0.5)*(rd**-0.25)
        Kts = 1 + 2.2*((Dd-1)**0.5)*(rd**-0.30)

    else:

        Kt=float(eKt.get())
        Kts=float(eKts.get())

# ----------------------------
# SENSIBILIDAD MUESCA
# ----------------------------

    if modoq.get()=="Automatico":

        SutMPa = Sut/1e6

        a = 0.246*(SutMPa**-0.107)
        a_s = 0.190*(SutMPa**-0.097)

        q = 1/(1+(a/math.sqrt(r)))
        qs = 1/(1+(a_s/math.sqrt(r)))

    else:

        q=float(eq.get())
        qs=float(eqs.get())

# ----------------------------
# FACTORES FATIGA
# ----------------------------

    if modoKf.get()=="Automatico":

        Kf = 1 + q*(Kt-1)
        Kfs = 1 + qs*(Kts-1)

    else:

        Kf=float(eKf.get())
        Kfs=float(eKfs.get())

# ----------------------------
# ESFUERZOS
# ----------------------------

    sigma_a = (32*Ma)/(math.pi*d**3)*Kf
    sigma_m = (32*Mm)/(math.pi*d**3)*Kf

    tau_a = (16*Ta)/(math.pi*d**3)*Kfs
    tau_m = (16*Tm)/(math.pi*d**3)*Kfs

# ----------------------------
# VON MISES
# ----------------------------

    sigma_a_vm = math.sqrt(sigma_a**2+3*tau_a**2)
    sigma_m_vm = math.sqrt(sigma_m**2+3*tau_m**2)

    sigma_max = math.sqrt((sigma_m+sigma_a)**2+3*(tau_m+tau_a)**2)

    n_vm = Sy/sigma_max

# ----------------------------
# PARAMETROS A B
# ----------------------------

    A = math.sqrt(4*(Kf*Ma)**2+3*(Kfs*Ta)**2)
    B = math.sqrt(4*(Kf*Mm)**2+3*(Kfs*Tm)**2)

# ----------------------------
# GOODMAN
# ----------------------------

    inv = (16/(math.pi*d**3))*((A/Se)+(B/Sut))
    n_good = 1/inv

# ----------------------------
# SODERBERG
# ----------------------------

    inv = (16/(math.pi*d**3))*((A/Se)+(B/Sy))
    n_sod = 1/inv

# ----------------------------
# GERBER
# ----------------------------

    inv = (8*A)/(math.pi*d**3*Se)*(1+math.sqrt(1+(2*B*Se/(A*Sut))**2))
    n_ger = 1/inv

# ----------------------------
# ASME
# ----------------------------

    inv = (16/(math.pi*d**3))*math.sqrt(
        4*(Kf*Ma/Se)**2+
        3*(Kfs*Ta/Se)**2+
        4*(Kf*Mm/Sy)**2+
        3*(Kfs*Tm/Sy)**2)

    n_asme = 1/inv

# ----------------------------
# RESULTADOS
# ----------------------------

    txt=f"""

RELACIONES GEOMETRICAS

D/d = {Dd:.3f}
r/d = {rd:.4f}

-------------------------

FACTORES

Kt = {Kt:.3f}
Kts = {Kts:.3f}

q = {q:.3f}
qs = {qs:.3f}

Kf = {Kf:.3f}
Kfs = {Kfs:.3f}

-------------------------

ESFUERZOS

σa = {mostrar_esfuerzo(sigma_a)}
σm = {mostrar_esfuerzo(sigma_m)}

τa = {mostrar_esfuerzo(tau_a)}
τm = {mostrar_esfuerzo(tau_m)}

-------------------------

VON MISES

σa' = {mostrar_esfuerzo(sigma_a_vm)}
σm' = {mostrar_esfuerzo(sigma_m_vm)}

σmax = {mostrar_esfuerzo(sigma_max)}

Factor Von Mises

n = {n_vm:.2f}

-------------------------

GOODMAN

n = {n_good:.2f}

SODERBERG

n = {n_sod:.2f}

GERBER

n = {n_ger:.2f}

ASME ELIPTICO

n = {n_asme:.2f}

"""

    salida.delete("1.0",tk.END)
    salida.insert(tk.END,txt)

# ----------------------------
# INTERFAZ
# ----------------------------

root=tk.Tk()
root.title("Calculadora de Fatiga de Ejes")
root.geometry("900x700")

tabs=ttk.Notebook(root)
tabs.pack(fill="both",expand=True)

tab1=tk.Frame(tabs)
tab2=tk.Frame(tabs)

tabs.add(tab1,text="DATOS")
tabs.add(tab2,text="RESULTADOS")

frame=tk.Frame(tab1)
frame.pack(pady=20)

def campo(txt,row,val):

    tk.Label(frame,text=txt).grid(row=row,column=0)

    e=tk.Entry(frame,width=10)
    e.insert(0,val)
    e.grid(row=row,column=1)

    return e

eD=campo("Diametro mayor D",0,0.04)
ed=campo("Diametro menor d",1,0.03)
er=campo("Radio r",2,0.002)

eMa=campo("Momento alternante",3,50)
eMm=campo("Momento medio",4,40)

eTa=campo("Torque alternante",5,20)
eTm=campo("Torque medio",6,30)

eSut=campo("Sut",7,700)
eSy=campo("Sy",8,560)
eSe=campo("Se",9,210)

# unidades

u_long=ttk.Combobox(frame,values=["m","cm","in"])
u_long.set("m")
u_long.grid(row=0,column=2)

u_mom=ttk.Combobox(frame,values=["N.m","lbf.in"])
u_mom.set("N.m")
u_mom.grid(row=3,column=2)

u_esf=ttk.Combobox(frame,values=["Pa","MPa","psi","kpsi"])
u_esf.set("MPa")
u_esf.grid(row=7,column=2)

# modos

modoKt=ttk.Combobox(frame,values=["Automatico","Manual"])
modoKt.set("Automatico")
modoKt.grid(row=10,column=1)

eKt=campo("Kt",11,2)
eKts=campo("Kts",12,1.5)

modoq=ttk.Combobox(frame,values=["Automatico","Manual"])
modoq.set("Automatico")
modoq.grid(row=13,column=1)

eq=campo("q",14,0.8)
eqs=campo("qs",15,0.8)

modoKf=ttk.Combobox(frame,values=["Automatico","Manual"])
modoKf.set("Automatico")
modoKf.grid(row=16,column=1)

eKf=campo("Kf",17,2)
eKfs=campo("Kfs",18,1.5)

tk.Button(frame,text="CALCULAR",command=calcular,width=20).grid(row=19,column=1,pady=10)

# RESULTADOS

unidad_result=ttk.Combobox(tab2,values=["Pa","MPa","psi","kpsi"])
unidad_result.set("MPa")
unidad_result.pack()

salida=tk.Text(tab2,width=100,height=35)
salida.pack()

root.mainloop()