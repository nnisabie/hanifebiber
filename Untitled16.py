#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# ---------- Bulanık Mantık Modeli ----------
nem = ctrl.Antecedent(np.arange(0, 101, 1), 'Toprak Nemi')
sicaklik = ctrl.Antecedent(np.arange(0, 51, 1), 'Hava Sicakligi')
ruzgar = ctrl.Antecedent(np.arange(0, 31, 1), 'Ruzgar Hiz')
yagmur = ctrl.Antecedent(np.arange(0, 101, 1), 'Yagmur Olasiligi')
bitki = ctrl.Antecedent(np.arange(0, 3, 1), 'Bitki Turu')

sure = ctrl.Consequent(np.arange(0, 61, 1), 'Sulama Süresi')
siklik = ctrl.Consequent(np.arange(1, 4, 1), 'Sulama Sıklığı')

nem.automf(names=['dusuk', 'orta', 'yuksek'])
sicaklik.automf(names=['soguk', 'ilik', 'sicak'])
ruzgar.automf(names=['dusuk', 'orta', 'yuksek'])
yagmur.automf(names=['dusuk', 'orta', 'yuksek'])

bitki['sebze'] = fuzz.trimf(bitki.universe, [0, 0, 0.5])
bitki['meyve'] = fuzz.trimf(bitki.universe, [0.5, 1, 1.5])
bitki['tahil'] = fuzz.trimf(bitki.universe, [1.5, 2, 2])

sure['kisa'] = fuzz.trimf(sure.universe, [0, 10, 20])
sure['orta'] = fuzz.trimf(sure.universe, [15, 30, 45])
sure['uzun'] = fuzz.trimf(sure.universe, [40, 60, 60])

siklik['az'] = fuzz.trimf(siklik.universe, [1, 1, 1.5])
siklik['orta'] = fuzz.trimf(siklik.universe, [1.5, 2, 2.5])
siklik['sik'] = fuzz.trimf(siklik.universe, [2.5, 3, 3])

rule1 = ctrl.Rule(nem['dusuk'] & sicaklik['sicak'] & yagmur['dusuk'], (sure['uzun'], siklik['sik']))
rule2 = ctrl.Rule(nem['orta'] & sicaklik['ilik'] & yagmur['orta'] & bitki['meyve'], (sure['orta'], siklik['orta']))
rule3 = ctrl.Rule(nem['yuksek'] & yagmur['yuksek'] & ruzgar['yuksek'], (sure['kisa'], siklik['az']))
rule4 = ctrl.Rule(bitki['sebze'] & sicaklik['sicak'] & nem['dusuk'], (sure['uzun'], siklik['sik']))
rule5 = ctrl.Rule(ruzgar['yuksek'] & yagmur['dusuk'] & sicaklik['soguk'], (sure['orta'], siklik['az']))

sulama_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
sulama_sim = ctrl.ControlSystemSimulation(sulama_ctrl)

# ---------- GUI Başlangıcı ----------
root = tk.Tk()
root.title("Akıllı Sulama Sistemi")
root.geometry("900x650")
root.configure(bg="#ecf0f1")

style = ttk.Style()
style.theme_use("clam")
style.configure('TNotebook', background="#ecf0f1", borderwidth=0)
style.configure('TNotebook.Tab', background="#bdc3c7", foreground="black", font=('Segoe UI', 11, 'bold'), padding=[12, 6])
style.map('TNotebook.Tab', background=[("selected", "#3498db")], foreground=[("selected", "white")])

# Sekmeler
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Veri Girişi')
tabControl.add(tab2, text='Girdi Grafikler')
tabControl.add(tab3, text='Çıktı Grafikler')
tabControl.pack(expand=1, fill="both")

# Yardımcı Fonksiyonlar
def create_labeled_entry(frame, label_text):
    container = tk.Frame(frame, bg="white", bd=1, relief="groove")
    container.pack(pady=6, padx=20, fill="x")
    tk.Label(container, text=label_text, bg="white", fg="#2c3e50", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=8, pady=(5, 0))
    entry = tk.Entry(container, font=("Segoe UI", 11), bg="#fdfefe", relief="flat")
    entry.pack(padx=8, pady=(0, 6), fill="x")
    return entry

def create_combobox(frame, label_text, values):
    container = tk.Frame(frame, bg="white", bd=1, relief="groove")
    container.pack(pady=6, padx=20, fill="x")
    tk.Label(container, text=label_text, bg="white", fg="#2c3e50", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=8, pady=(5, 0))
    combo = ttk.Combobox(container, values=values, font=("Segoe UI", 11))
    combo.current(0)
    combo.pack(padx=8, pady=(0, 6), fill="x")
    return combo

# Giriş Sekmesi
entry_nem = create_labeled_entry(tab1, "Toprak Nemi (%)")
entry_sicaklik = create_labeled_entry(tab1, "Hava Sıcaklığı (°C)")
entry_ruzgar = create_labeled_entry(tab1, "Rüzgar Hızı (km/h)")
entry_yagmur = create_labeled_entry(tab1, "Yağmur Olasılığı (%)")
bitki_combo = create_combobox(tab1, "Bitki Türü", ["Sebze", "Meyve", "Tahil"])

result_frame = tk.Frame(tab1, bg="#ecf0f1")
result_frame.pack(pady=10)

lbl_sure = tk.Label(result_frame, text="Sulama Süresi: ---", font=("Segoe UI", 12, "bold"), bg="#ecf0f1", fg="#2980b9")
lbl_sure.pack(pady=5)

lbl_siklik = tk.Label(result_frame, text="Sulama Sıklığı: ---", font=("Segoe UI", 12, "bold"), bg="#ecf0f1", fg="#27ae60")
lbl_siklik.pack(pady=5)

tk.Button(tab1, text="HESAPLA", command=lambda: hesapla(), font=("Segoe UI", 12, "bold"), bg="#3498db", fg="white", relief="flat", padx=20, pady=10).pack(pady=20)

# Hesaplama
bitki_map = {'Sebze': 0, 'Meyve': 1, 'Tahil': 2}

def hesapla():
    try:
        sulama_sim.input['Toprak Nemi'] = float(entry_nem.get())
        sulama_sim.input['Hava Sicakligi'] = float(entry_sicaklik.get())
        sulama_sim.input['Ruzgar Hiz'] = float(entry_ruzgar.get())
        sulama_sim.input['Yagmur Olasiligi'] = float(entry_yagmur.get())
        sulama_sim.input['Bitki Turu'] = bitki_map[bitki_combo.get()]

        sulama_sim.compute()

        lbl_sure.config(text=f"Sulama Süresi: {sulama_sim.output['Sulama Süresi']:.1f} dk")
        lbl_siklik.config(text=f"Sulama Sıklığı: {sulama_sim.output['Sulama Sıklığı']:.1f} kez/gün")

        girdi_grafigi_ciz()
        cikti_grafigi_ciz()

    except Exception as e:
        messagebox.showerror("Hata", str(e))

# Grafik Fonksiyonları
def girdi_grafigi_ciz():
    for widget in tab2.winfo_children():
        widget.destroy()

    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    fig.suptitle("Girdi Üyelik Fonksiyonları", fontsize=16, fontweight='bold', color='darkblue')
    renkler = ['#1f77b4', '#2ca02c', '#d62728']

    for var, ax, title in zip([nem, sicaklik, ruzgar, yagmur], axs.flat, ['Toprak Nemi (%)', 'Hava Sıcaklığı (°C)', 'Rüzgar Hızı (km/h)', 'Yağmur Olasılığı (%)']):
        for i, label in enumerate(var.terms):
            ax.plot(var.universe, var[label].mf, label=label.capitalize(), linewidth=2.5, color=renkler[i % len(renkler)])
            ax.fill_between(var.universe, var[label].mf, alpha=0.15, color=renkler[i % len(renkler)])
            max_idx = np.argmax(var[label].mf)
            ax.plot(var.universe[max_idx], var[label].mf[max_idx], 'ro')
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("Girdi Değeri")
        ax.set_ylabel("Üyelik")
        ax.grid(True)
        ax.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    canvas = FigureCanvasTkAgg(fig, master=tab2)
    canvas.draw()
    canvas.get_tk_widget().pack()
    plt.close(fig)

def cikti_grafigi_ciz():
    for widget in tab3.winfo_children():
        widget.destroy()

    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    fig.suptitle("Çıktı Üyelik Fonksiyonları", fontsize=16, fontweight='bold', color='darkgreen')
    renkler = ['#ff7f0e', '#9467bd', '#17becf']

    for var, ax, output_name, title in zip([sure, siklik], axs, ['Sulama Süresi', 'Sulama Sıklığı'], ['Sulama Süresi (dk)', 'Sulama Sıklığı (kez/gün)']):
        for i, label in enumerate(var.terms):
            ax.plot(var.universe, var[label].mf, label=label.capitalize(), linewidth=2.5, color=renkler[i % len(renkler)])
            ax.fill_between(var.universe, var[label].mf, alpha=0.15, color=renkler[i % len(renkler)])
        try:
            x = sulama_sim.output[output_name]
            for i, label in enumerate(var.terms):
                y = fuzz.interp_membership(var.universe, var[label].mf, x)
                ax.plot(x, y, 'ro')
        except:
            pass
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("Çıktı Değeri")
        ax.set_ylabel("Üyelik")
        ax.grid(True)
        ax.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    canvas = FigureCanvasTkAgg(fig, master=tab3)
    canvas.draw()
    canvas.get_tk_widget().pack()
    plt.close(fig)

# ---------- Başlat ----------
root.mainloop()


# In[ ]:




