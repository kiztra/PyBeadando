import math
import tkinter as tk
from tkinter import messagebox



class Haromszog:
    def __init__(self, master):
        self.master = master
        self.master.title("Háromszög adatai - Torma Rudolf - JRGT5V")
        self.master.geometry("600x400")
        self.cim_cimke = tk.Label(self.master, text="Az oldalak hossza:", font=("Ariel", 16))
        self.cim_cimke.grid(row=0, column=1, pady=20, padx=60)
        self.c_cimke = tk.Label(self.master, text="A oldal:", font=("Ariel", 16))
        self.c_cimke.grid(row=1, column=0)
        self.a_meret = tk.StringVar(value="3")
        self.c_oldal = tk.Entry(self.master, textvariable=self.a_meret, width=10)
        self.c_oldal.grid(row=2, column=0, pady=10, padx=50)
        self.b_cimke = tk.Label(self.master, text="B oldal:", font=("Ariel", 16))
        self.b_cimke.grid(row=1, column=1)
        self.b_meret = tk.StringVar(value="4")
        self.b_oldal = tk.Entry(self.master, textvariable=self.b_meret, width=10)
        self.b_oldal.grid(row=2, column=1, pady=10, padx=50)
        self.c_cimke = tk.Label(self.master, text="C oldal:", font=("Ariel", 16))
        self.c_cimke.grid(row=1, column=2)
        self.c_meret = tk.StringVar(value="5")
        self.c_oldal = tk.Entry(self.master, textvariable=self.c_meret, width=10)
        self.c_oldal.grid(row=2, column=2, pady=10, padx=50)
        self.eredmeny_kcimke_szoveg = tk.StringVar(value="")
        self.kerulet_eredmeny = tk.Label(self.master, textvariable=self.eredmeny_kcimke_szoveg, font=("Ariel", 16))
        self.kerulet_eredmeny.grid(row=4, column=1, pady=20)
        self.k_gomb = tk.Button(self.master, text="Kerület", command=self.h_kerulet)
        self.k_gomb.grid(row=4, column=0, pady=20)
        self.eredmeny_tcimke_szoveg = tk.StringVar(value="")
        self.terulet_eredmeny = tk.Label(self.master, textvariable=self.eredmeny_tcimke_szoveg, font=("Ariel", 16))
        self.terulet_eredmeny.grid(row=5, column=1, pady=20)
        self.t_gomb = tk.Button(self.master, text="Terület", command=self.h_terulet)
        self.t_gomb.grid(row=5, column=0, pady=20)
        self.eredmeny_dcimke_szoveg = tk.StringVar(value="")
        self.derekszog_eredmeny = tk.Label(self.master, textvariable=self.eredmeny_dcimke_szoveg, font=("Ariel", 16))
        self.derekszog_eredmeny.grid(row=6, column=1, pady=20)
        self.d_gomb = tk.Button(self.master, text="Derékszögű", command=self.h_derekszog)
        self.d_gomb.grid(row=6, column=0, pady=20)
        self.kilepes = tk.Button(self.master, text="Kilépés", command=self.master.destroy, bg="red")
        self.kilepes.grid(row=8, column=2)

    def h_terulet(self):
        try:
            self.a_oldal = int(self.a_meret.get())
            self.b_oldal = int(self.b_meret.get())
            self.c_oldal = int(self.c_meret.get())

            if (self.a_oldal + self.b_oldal <= self.c_oldal) or (self.a_oldal + self.c_oldal <= self.b_oldal) or (
                    self.b_oldal + self.c_oldal <= self.a_oldal):
                self.eredmeny_tcimke_szoveg.set("")
                return messagebox.showerror(title="Hiba", message="A megadott oldalak nem alkotnak háromszöget!")
            S = (self.a_oldal + self.b_oldal + self.c_oldal)/2
            terulet = math.sqrt(S * (S - self.a_oldal) * (S - self.b_oldal) * (S - self.c_oldal))

            self.eredmeny_tcimke_szoveg.set(f"{terulet} cm²")

        except:
            messagebox.showerror(title="Hiba", message="Nem jó értéket adott meg!")

    def h_kerulet(self):
        try:
            self.a_oldal = int(self.a_meret.get())
            self.b_oldal = int(self.b_meret.get())
            self.c_oldal = int(self.c_meret.get())

            if (self.a_oldal + self.b_oldal <= self.c_oldal) or (self.a_oldal + self.c_oldal <= self.b_oldal) or (self.b_oldal + self.c_oldal <= self.a_oldal):
                self.eredmeny_kcimke_szoveg.set("")
                return messagebox.showerror(title="Hiba", message="A megadott oldalak nem alkotnak háromszöget!")

            kerulet = self.a_oldal + self.b_oldal + self.c_oldal
            self.eredmeny_kcimke_szoveg.set(f"{kerulet} cm")

        except:
            messagebox.showerror(title="Hiba", message="Nem jó értéket adott meg!")

    def h_derekszog(self):
        try:
            self.a_oldal = int(self.a_meret.get())
            self.b_oldal = int(self.b_meret.get())
            self.c_oldal = int(self.c_meret.get())

            if (self.a_oldal + self.b_oldal <= self.c_oldal) or (self.a_oldal + self.c_oldal <= self.b_oldal) or (self.b_oldal + self.c_oldal <= self.a_oldal):
                self.eredmeny_kcimke_szoveg.set("")
                return messagebox.showerror(title="Hiba", message="A megadott oldalak nem alkotnak háromszöget!")

            oldalak = sorted([self.a_oldal, self.b_oldal, self.c_oldal])
            if math.isclose(oldalak[0] ** 2 + oldalak[1] ** 2, oldalak[2]** 2):
                self.eredmeny_dcimke_szoveg.set("IGEN, derékszögű!")
            else:
                self.eredmeny_dcimke_szoveg.set("NEM derékszögű!")


        except:
            messagebox.showerror(title="Hiba", message="Nem jó értéket adott meg!")

