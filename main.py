import pyautogui # screenshot özelliği bu modülden geliyor
import tkinter as tk #buarada tk adını tkinter yerine kullanabilirz.

from tkinter.filedialog import *## Burada ki modülü ekleme tarzını anlamadım. Sadece o modülün bütün fonksiyonlarını çalıştırmak istiyorsak
# * işareti hepsini kullanmamızı sağlar

root= tk.Tk()

canvas1 = tk.Canvas(root, width= 300, height=300)

canvas1.pack()

def takeScreenShot(): #fonksiyon yarattık

    myScreenshot = pyautogui.screenshot()
    
    # kayıt ederken isimini sormasını ve nereye kayıt edeceğimizi sağlıyor.
    save_path= asksaveasfilename()
    myScreenshot.save(save_path+"_screenshot.png")



# button yarattık
myButton= tk.Button(text="Take ScreenShot",command= takeScreenShot,font=10)


canvas1.create_window(150,150,window=myButton)

root.mainloop()