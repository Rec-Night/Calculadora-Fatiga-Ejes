import tkinter as tk
import math

def calcular():

    try:
        Sut = float(entry_sut.get())
        d = float(entry_d.get())

        Kt = float(entry_kt.get())
        Kts = float(entry_kts.get())

        q = float(entry_q.get())
        qs = float(entry_qs.get())

        confiabilidad = float(entry_conf.get())

        # tabla confiabilidad en decimal
        tabla_ke = {
            0.50:1.000,
            0.90:0.897,
            0.95:0.868,
            0.99:0.814,
            0.999:0.753,
            0.9999:0.702,
            0.99999:0.659
        }

        if confiabilidad in tabla_ke:
            ke = tabla_ke[confiabilidad]
        else:
            resultado.set("Confiabilidad no válida")
            return

        # Se prima
        Se_prima = 0.5 * Sut

        # factores Marin
        ka = 2.70 * (Sut ** -0.265)
        kb = (d/0.30) ** -0.107
        kc = 1
        kd = 1
        kf_marin = 1

        # Se corregido
        Se = ka * kb * kc * kd * kf_marin * ke * Se_prima

        # Factores de fatiga
        Kf = 1 + q * (Kt - 1)
        Kfs = 1 + qs * (Kts - 1)

        resultado.set(
            f"Se' = {round(Se_prima,2)} kpsi\n"
            f"ka = {round(ka,3)}\n"
            f"kb = {round(kb,3)}\n"
            f"ke = {ke}\n\n"
            f"Se = {round(Se,2)} kpsi\n\n"
            f"Kf = {round(Kf,3)}\n"
            f"Kfs = {round(Kfs,3)}"
        )

    except:
        resultado.set("Error en los datos")

ventana = tk.Tk()
ventana.title("Calculadora de Fatiga")
ventana.geometry("320x480")

tk.Label(ventana, text="Sut (kpsi)").pack()
entry_sut = tk.Entry(ventana)
entry_sut.pack()

tk.Label(ventana, text="Diámetro d (in)").pack()
entry_d = tk.Entry(ventana)
entry_d.pack()

tk.Label(ventana, text="Confiabilidad (decimal)").pack()
entry_conf = tk.Entry(ventana)
entry_conf.pack()

tk.Label(ventana, text="Kt").pack()
entry_kt = tk.Entry(ventana)
entry_kt.pack()

tk.Label(ventana, text="Kts").pack()
entry_kts = tk.Entry(ventana)
entry_kts.pack()

tk.Label(ventana, text="q").pack()
entry_q = tk.Entry(ventana)
entry_q.pack()

tk.Label(ventana, text="qs (cortante)").pack()
entry_qs = tk.Entry(ventana)
entry_qs.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack()

ventana.mainloop()