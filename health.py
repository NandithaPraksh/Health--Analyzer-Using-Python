import pandas as pd 
import numpy as np
import tkinter as tk
from tkinter import  messagebox
file_name =  'health.xlsx'
try:
    data = pd.read_excel(file_name)
except FileNotFoundError:
    data = pd.DataFrame(columns=['Name','Age','Gender','Height(cm)','BMI','BMI Category','Health Tips'])
data.drop(columns=["BMI Category"],inplace = True,errors='ignore')
data.drop(columns=['Health Tips'],inplace =True,errors ='ignore')
data.to_excel(file_name,index = False)
def bmi_category(bmi):
    if bmi<=18.5:
        return 'UnderWeight'
    elif 18.5<= bmi <24.9:
        return 'Normal Weight'
    elif 25 <=bmi <=29.9:
        return 'Over Weight'
    else:
        return 'Obese'
def health_tips(category):
    tips = {
        'UnderWeight':'Eat protein-rich food & maintain calories ',
        'Normal Weight':'Keep it up! Stay active & hydrated ',
        'Over Weight': 'Try light workouts & balanced diet',
        'Obese':'Consult a nutritionist & focus on small lifestyle changes'
    }
    return tips.get(category,'')
def calculate_bmi():
    global data
    try:
        name =entry_name.get()
        age = int(entry_age.get())
        gender = entry_gender.get()
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        height_m = height/100
        bmi = round(weight/(height_m**2),2)
        category =bmi_category(bmi)
        tip =health_tips(category)

        new_data =pd.DataFrame([{
            'Name': name,
            'Age':age,
            'Gender':gender,
            'Height(cm)':height,
            'Weight(kg)':weight,
            'Height(m)':height_m,
            'BMI':bmi,
            'Category':category,
            'tips':tip

            }])
        data = pd.concat([data,new_data],ignore_index = True)
        data.to_excel(file_name,index =False)
        result = f"BMI:{bmi}\nCategory:{category}\n\n{tip}"
        messagebox.showinfo("BMI Result",result)
        entry_name.delete(0,tk.END)
        entry_age.delete(0,tk.END)
        entry_gender.delete(0,tk.END)
        entry_height.delete(0,tk.END)
        entry_weight.delete(0,tk.END)
    except ValueError:
        messagebox.showerror("Please fill all the fiels correctly")
window =tk.Tk()
window.title("BMI Health Analyzer")
window.geometry("600x600")
window.config(bg ="#ffe6f2")
title = tk.Label(window,text ="BMI Health Analyzer",font=("Comic Sans MS", 16, "bold"), bg="#ffe6f2", fg="#d63384")
title.pack(pady =10)
labels= ["Name","Age","Gender","Height(cm)","Weight(kg)"]
entries = []
for label_text in labels:

    frame = tk.Frame(window, bg ="#ffe6f2")
    frame.pack(pady = 3)
    label = tk.Label(frame,text = label_text,font=("Areal",11,"bold"),bg="#ffe6f2", fg="#ff1493")
    label.pack(side = tk.LEFT,padx =10)
    entry =tk.Entry(frame)
    entry.pack(side = tk.RIGHT)
    entries.append(entry)
entry_name,entry_age,entry_gender,entry_height,entry_weight = entries
btn =tk.Button(window,text = "Calculate BMI",font=("Arial", 12, "bold"), bg="#ff80bf", fg="white",command = calculate_bmi)
btn.pack(pady =15)
window.mainloop()





