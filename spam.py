# Author : dexter

# Reccode : xtreshe dev

import requests, os

def logo():
  print("""
=========================================================
¦¦
¦¦   ===============================
¦¦   [ ♻ TOOLS SPAM SMS,WA,CALL ♻ ]
¦¦   ===============================
¦¦   =====================
¦¦   [ RECODE : xtreshe dev ✔ ]
¦¦   =====================
¦¦   =========================================
¦¦   [ Github : https://github.com/xtreshebot ✔ ]
¦¦   =========================================
¦¦    ======================
¦¦   [ YouTube :  ✔ ]                           
¦¦   =======================                           
¦¦                                                        
==========================================================
""")

def menu():
  os.system('clear')
  logo()
  print("\nMasukan Nomer Di Awali (8xxx)")
  nomor = input("Nomer Target : 0")
  jum = int(input("Jumlah : "))
  for i in range(jum):
      req = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
      if 'terkirim' in req:
           print("\nSpam Terkirim ✔ | By:|xtreshe dev")
      else:
           print("\nGagal! Kendala jaringan,Coba beberapa saat!")
           

menu()
