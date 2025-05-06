import tkinter as tk
from tkinter import ttk
from pyswip import Prolog
from tkinter import messagebox

prolog = Prolog()
prolog.consult("pcos_rules.pl")  

gejala_list = ["irregular_cycle", "high_testosterone", "ovarian_cysts"]
current_index = 0  

def get_question(gejala):
    query = f"gejala({gejala}, Y)"
    result = list(prolog.query(query))
    return result[0]["Y"] if result else ""

def next_question():
    global current_index
    if current_index < len(gejala_list):
        kotak_pertanyaan.config(state=tk.NORMAL)
        kotak_pertanyaan.delete("1.0", tk.END)
        kotak_pertanyaan.insert(tk.END, get_question(gejala_list[current_index]))
        kotak_pertanyaan.config(state=tk.DISABLED)
        yes_btn.config(state=tk.NORMAL)
        no_btn.config(state=tk.NORMAL)
    else:
        check_pcos()

def jawaban(positif):
    global current_index
    if positif:
        prolog.assertz(f"gejala_pos({gejala_list[current_index]})")
    else:
        prolog.assertz(f"gejala_neg({gejala_list[current_index]})")

    current_index += 1
    next_question()

def check_pcos():
    result = list(prolog.query("pcos(X)"))
    diagnosis = "Kemungkinan mengalami PCOS." if result else "Tidak terdeteksi PCOS."
    messagebox.showinfo("Hasil Diagnosa", diagnosis)

root = tk.Tk()
root.title("Sistem Pakar Diagnosis PCOS")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Aplikasi Diagnosa PCOS", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=4, width=40, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Diagnosa", command=next_question)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()