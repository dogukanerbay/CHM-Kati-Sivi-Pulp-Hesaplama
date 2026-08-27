from tkinter import *

window = Tk()
window.title("Katı Sıvı İşlemleri")
window.minsize(300,300)
window.config(bg="white")

#Katı
katı_label = Label(text="Katı Miktarı (Kg)")
katı_label.pack()
katı_entry = Entry(width=20)
katı_entry.pack()

#Sıvı
sıvı_label = Label(text="Sıvı Miktarı (Kg)")
sıvı_label.pack()
sıvı_entry = Entry(width=20)
sıvı_entry.pack()

def hesap():
    try:

        katı  = float(katı_entry.get())
        sıvı = float(sıvı_entry.get())
        pulp= katı+sıvı

        if sıvı == 0 or katı==0:
            result_text_label.config(text="Katı ve sıvı miktarı 0 olamaz.")
            return

        pko = (katı/pulp)*100
        pso = (sıvı/pulp)*100
        katı_sıvı_oranı = (katı / sıvı)*100
        result_text_label.config(text=f"Toplam ağırlık:{pulp:.2f} kg\nPülpte katı oranı %{pko:.2f}\nPülpte sıvı oranı %{pso:.2f}"
                                      f"\nKatı sıvı oranı %{katı_sıvı_oranı:.2f}")
    except (ValueError):
        result_text_label.config(text="Değerlerinizi kontrol edin")

button = Button(text="Hesapla", command=hesap)
button.config(padx=10, pady=10)
button.pack()

#Result
result_label = Label(text="Sonuç")
result_label.pack()

result_text_label = Label(text="")
result_text_label.pack()

window.mainloop()

