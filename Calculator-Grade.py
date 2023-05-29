from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD

#สร้าง Tkinter และกำหนดlogo ขนาดจอ พื้นหลัง และห้ามย่อขยาย
root = Tk()
root.title("GPA Calculator")
root.configure(bg="#fff")
root.geometry("730x740+400+20")
root.resizable(0,0)

FONT_DEFULT = ('Microsoft Yahei UI Light')

#function check file
def checkfile():
    global sub1, sub2, sub3 , sub4, sub5, sub6, sub7, sub8, sub9, sub10
    global credit1, credit2, credit3, credit4, credit5, credit6, credit7, credit8, credit9, credit10
    global grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8,grade9, grade10
    list_history_sub = []
    list_history_credit = []
    list_history_grade = []
    try:
        #หาไฟล์ และเซ็ตค่าในตัวแปรของรหัสวิชา หน่วยกิต และเกรด ที่เคยกรอกไว้ในรอบที่ล่าสุด
        fr = open("History.txt", "r", encoding="utf-8")
        for line in fr.readlines():
            sub = line[:6].strip()
            credit = line[10:17].strip()
            grade = line[18:].strip()
            if sub != "":
                list_history_sub.append(sub)
                list_history_credit.append(credit)
                list_history_grade.append(grade)
        #ใช้try except ช่วยในการกำหนด value ของwidget ที่เอามข้อมูลมาจากไฟล์ except หากเกิดerror IndexError ก็จะเซ็ตตรงนั้นเป็นdefult
        try:
            sub1 = StringVar(value=list_history_sub[0])
            credit1 = IntVar(value=list_history_credit[0])
            grade1 = StringVar(value=list_history_grade[0])
        except IndexError:
            sub1 = StringVar(value="")
            credit1 = IntVar(value=0)
            grade1 = StringVar(value="เลือกเกรด")

        try:
            sub2 = StringVar(value=list_history_sub[1])
            credit2 = IntVar(value=list_history_credit[1])
            grade2 = StringVar(value=list_history_grade[1])
        except IndexError:
            sub2 = StringVar(value="")
            credit2 = IntVar(value=0)
            grade2 = StringVar(value="เลือกเกรด")

        try:
            sub3 = StringVar(value=list_history_sub[2])
            credit3 = IntVar(value=list_history_credit[2])
            grade3 = StringVar(value=list_history_grade[2])
        except IndexError:
            sub3 = StringVar(value="")
            credit3 = IntVar(value=0)
            grade3 = StringVar(value="เลือกเกรด")

        try:
            sub4 = StringVar(value=list_history_sub[3])
            credit4 = IntVar(value=list_history_credit[3])
            grade4 = StringVar(value=list_history_grade[3])
        except IndexError:
            sub4 = StringVar(value="")
            credit4 = IntVar(value=0)
            grade4 = StringVar(value="เลือกเกรด")

        try:
            sub5 = StringVar(value=list_history_sub[4])
            credit5 = IntVar(value=list_history_credit[4])
            grade5 = StringVar(value=list_history_grade[4])
        except IndexError:
            sub5 = StringVar(value="")
            credit5 = IntVar(value=0)
            grade5 = StringVar(value="เลือกเกรด")

        try:
            sub6 = StringVar(value=list_history_sub[5])
            credit6 = IntVar(value=list_history_credit[5])
            grade6 = StringVar(value=list_history_grade[5])
        except IndexError:
            sub6 = StringVar(value="")
            credit6 = IntVar(value=0)
            grade6 = StringVar(value="เลือกเกรด")

        try:
            sub7 = StringVar(value=list_history_sub[6])
            credit7 = IntVar(value=list_history_credit[6])
            grade7 = StringVar(value=list_history_grade[6])
        except IndexError:
            sub7 = StringVar(value="")
            credit7 = IntVar(value=0)
            grade7 = StringVar(value="เลือกเกรด")

        try:
            sub8 = StringVar(value=list_history_sub[7])
            credit8 = IntVar(value=list_history_credit[7])
            grade8 = StringVar(value=list_history_grade[7])
        except IndexError:
            sub8 = StringVar(value="")
            credit8 = IntVar(value=0)
            grade8 = StringVar(value="เลือกเกรด")

        try:
            sub9 = StringVar(value=list_history_sub[8])
            credit9 = IntVar(value=list_history_credit[8])
            grade9 = StringVar(value=list_history_grade[8])
        except IndexError:
            sub9 = StringVar(value="")
            credit9 = IntVar(value=0)
            grade9 = StringVar(value="เลือกเกรด")
        try:
            sub10 = StringVar(value=list_history_sub[9])
            credit10 = IntVar(value=list_history_credit[9])
            grade10 = StringVar(value=list_history_grade[9])
        except IndexError:
            sub10 = StringVar(value="")
            credit10 = IntVar(value=0)
            grade10 = StringVar(value="เลือกเกรด")

        fr.close()
    #except error FileNotFoundError หมายถึง หาไฟล์ไม่เจอ ให้สร้างไฟล์ใหม่แล้วเซ็ตตัวแปร
    except FileNotFoundError:
        #สร้างfile
        fw = open("History.txt", "w", encoding="utf-8")
        fw.close()
        try:
            sub1 = StringVar(value=list_history_sub[0])
            credit1 = IntVar(value=list_history_credit[0])
            grade1 = StringVar(value=list_history_grade[0])
        except IndexError:
            sub1 = StringVar(value="")
            credit1 = IntVar(value=0)
            grade1 = StringVar(value="เลือกเกรด")

        try:
            sub2 = StringVar(value=list_history_sub[1])
            credit2 = IntVar(value=list_history_credit[1])
            grade2 = StringVar(value=list_history_grade[1])
        except IndexError:
            sub2 = StringVar(value="")
            credit2 = IntVar(value=0)
            grade2 = StringVar(value="เลือกเกรด")

        try:
            sub3 = StringVar(value=list_history_sub[2])
            credit3 = IntVar(value=list_history_credit[2])
            grade3 = StringVar(value=list_history_grade[2])
        except IndexError:
            sub3 = StringVar(value="")
            credit3 = IntVar(value=0)
            grade3 = StringVar(value="เลือกเกรด")

        try:
            sub4 = StringVar(value=list_history_sub[3])
            credit4 = IntVar(value=list_history_credit[3])
            grade4 = StringVar(value=list_history_grade[3])
        except IndexError:
            sub4 = StringVar(value="")
            credit4 = IntVar(value=0)
            grade4 = StringVar(value="เลือกเกรด")

        try:
            sub5 = StringVar(value=list_history_sub[4])
            credit5 = IntVar(value=list_history_credit[4])
            grade5 = StringVar(value=list_history_grade[4])
        except IndexError:
            sub5 = StringVar(value="")
            credit5 = IntVar(value=0)
            grade5 = StringVar(value="เลือกเกรด")

        try:
            sub6 = StringVar(value=list_history_sub[5])
            credit6 = IntVar(value=list_history_credit[5])
            grade6 = StringVar(value=list_history_grade[5])
        except IndexError:
            sub6 = StringVar(value="")
            credit6 = IntVar(value=0)
            grade6 = StringVar(value="เลือกเกรด")

        try:
            sub7 = StringVar(value=list_history_sub[6])
            credit7 = IntVar(value=list_history_credit[6])
            grade7 = StringVar(value=list_history_grade[6])
        except IndexError:
            sub7 = StringVar(value="")
            credit7 = IntVar(value=0)
            grade7 = StringVar(value="เลือกเกรด")

        try:
            sub8 = StringVar(value=list_history_sub[7])
            credit8 = IntVar(value=list_history_credit[7])
            grade8 = StringVar(value=list_history_grade[7])
        except IndexError:
            sub8 = StringVar(value="")
            credit8 = IntVar(value=0)
            grade8 = StringVar(value="เลือกเกรด")

        try:
            sub9 = StringVar(value=list_history_sub[8])
            credit9 = IntVar(value=list_history_credit[8])
            grade9 = StringVar(value=list_history_grade[8])
        except IndexError:
            sub9 = StringVar(value="")
            credit9 = IntVar(value=0)
            grade9 = StringVar(value="เลือกเกรด")
        try:
            sub10 = StringVar(value=list_history_sub[9])
            credit10 = IntVar(value=list_history_credit[9])
            grade10 = StringVar(value=list_history_grade[9])
        except IndexError:
            sub10 = StringVar(value="")
            credit10 = IntVar(value=0)
            grade10 = StringVar(value="เลือกเกรด")
#set font stype and color
FONT_COLOR = "black"
BG_COLOR = "#fff"
RED_ORANGE = "#fff"
WHITE = "black"

#dict grade
grade_dict = {"A": "4", "B+": "3.5", "B": "3", "C+": "2.5", "C": "2", "D+": "1.5", "D": "1", "F": "0"}
#ฟังก์ชันคำนวณเกรด
def calculate_gpa():
    global sum_credit
    global result_gpa
    global list_grade
    #เก็บตัวค่าที่รับจากwidget เข้าตัวแปร
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = credit1.get(), credit2.get(), credit3.get(), credit4.get(), credit5.get(), credit6.get(), credit7.get(), credit8.get(), credit9.get(), credit10.get()
    g1 , g2, g3, g4, g5, g6, g7, g8, g9, g10 = grade1.get(), grade2.get(), grade3.get(), grade4.get(), grade5.get(), grade6.get(), grade7.get(), grade8.get(), grade9.get(), grade10.get()
    sum_point = 0
    sum_credit = 0
    #ถ้าข้อไหนว่างให้แทนด้วย0
    if g1 == "เลือกเกรด" or g1 == " ":
        g1 = "F"
        c1 = 0
    if g2 == "เลือกเกรด" or g2 == " ":
        g2 = "F"
        c2 = 0
    if g3 == "เลือกเกรด" or g3 == " ":
        g3 = "F"
        c3 = 0
    if g4 == "เลือกเกรด" or g4 == " ":
        g4 = "F"
        c4 = 0
    if g5 == "เลือกเกรด" or g5 == " ":
        g5 = "F"
        c5 = 0
    if g6 == "เลือกเกรด" or g6 == " ":
        g6 = "F"
        c6 = 0
    if g7 == "เลือกเกรด" or g7 == " ":
        g7 = "F"
        c7 = 0
    if g8 == "เลือกเกรด" or g8 == " ":
        g8 = "F"
        c8 = 0
    if g9 == "เลือกเกรด" or g9 == " ":
        g9 = "F"
        c9 = 0
    if g10 == "เลือกเกรด" or g10 == " ":
        g10 = "F"
        c10 = 0
    #บวกgrade ทั้งหมด แล้วลูปเพื่อแปลงจากABCD เป็น 4321
    sum_g = g1+g2+g3+g4+g5+g6+g7+g8+g9+g10
    for gradeABCD,grade1234  in grade_dict.items():
         sum_g = sum_g.replace(gradeABCD, f' {grade1234} ')

    #ลูปเกรดเข้าlist เพื่อเอาไปใช้สะดวก
    list_grade = []
    for p in sum_g.split():
        list_grade.append(p)

    #รวมคะแนนทั้งหมด จากค่า หน่วยกิต * เกรด
    sum_point = sum_point + (float(c1) * float(list_grade[0]))
    sum_point = sum_point + (float(c2) * float(list_grade[1]))
    sum_point = sum_point + (float(c3) * float(list_grade[2]))
    sum_point = sum_point + (float(c4) * float(list_grade[3]))
    sum_point = sum_point + (float(c5) * float(list_grade[4]))
    sum_point = sum_point + (float(c6) * float(list_grade[5]))
    sum_point = sum_point + (float(c7) * float(list_grade[6]))
    sum_point = sum_point + (float(c8) * float(list_grade[7]))
    sum_point = sum_point + (float(c9) * float(list_grade[8]))
    sum_point = sum_point + (float(c10) * float(list_grade[9]))

    #รวมหน่วยกิต
    sum_credit = float(c1) + float(c2) + float(c3) + float(c4) + float(c5) + float(c6) + float(c7) + float(c8) + float(c9) + float(c10)

    #ใช้try except กันerror ในการหาGPA
    try:
        result_gpa = sum_point / sum_credit
    except ZeroDivisionError:
        result_gpa = 0

    
    #เกรด คูณ หน่วยกิต ได้คะแนนออกมา 4*3 = 12, 0*3 = 0
    #เกรดเฉลี่ยคือ คะแนนรวม หาร เครดิตรวม

#------------------------------------------------------------------------------------------------------------
#หน้าประวัติ
def result_his_page():
    calculate_gpa()
    #ไว้เคลียร์หน้าให้ว่าง สำหรับจะเปลี่ยนหน้า
    def clear_his_page():
        frame_title.destroy()
        frame_text.destroy()
        frame_result.destroy()
        frame_button.destroy()
    #เรียกclear แล้วเรียกหน้าmainpage เพื่อไปหน้าmainpage
    def backto_mainpage():
        clear_his_page()
        mainpage()
    #ลบข้อมูลในไฟล์และเซ็ตค่าoutput เป็นdefult
    def deleate_data():
        fw = open("History.txt","w",encoding="utf-8")
        fw.close()
        label_col1.config(text=(f""))
        label_col2.config(text=(f""))
        label_col3.config(text=(f""))
        
    show_sub = ""
    show_credit = ""
    show_grade = ""
    #อ่านไฟล์เพื่อลูปเก็บเข้าตัวแปร แล้วนำมาแสดงในwidget output
    fr = open("History.txt", "r", encoding="utf-8")
    for line in fr.readlines():
        subs = line[:6].strip()
        credits = line[10:17].strip()
        grades = line[18:].strip()
        if subs != "":
            show_sub = str(show_sub) + str(subs) + "\n"
            show_credit = str(show_credit) + str(credits) + "\n"
            show_grade = str(show_grade) + str(grades) + "\n"
                
    fr.close()
    #สร้างFrame การทำงาน
    frame_title = Frame(root,width=450, height=50, bg=BG_COLOR)
    frame_title.place(x=200,y=10)
    frame_text = Frame(root,width=660,height=435,bg=BG_COLOR)
    frame_text.place(x=25,y=80)
    
    frame_head_col1 = Frame(frame_text,width=280,height=40,bg=BG_COLOR)
    frame_head_col1.place(x=70,y=0)
    frame_head_col2 = Frame(frame_text,width=100,height=40,bg=BG_COLOR)
    frame_head_col2.place(x=320,y=0)
    frame_head_col3 = Frame(frame_text,width=120,height=40,bg=BG_COLOR)
    frame_head_col3.place(x=430,y=0)
    frame_col1 = Frame(frame_text,width=325,height=320,bg=BG_COLOR)
    frame_col1.place(x=60,y=40)
    frame_col2 = Frame(frame_text,width=120,height=320,bg=BG_COLOR)
    frame_col2.place(x=365,y=40)
    frame_col3 = Frame(frame_text,width=150,height=320,bg=BG_COLOR)
    frame_col3.place(x=475,y=40)

    title = Label(frame_title,text="ประวัติล่าสุดที่คำนวณ",font=(FONT_DEFULT,26),bg=BG_COLOR)
    title.pack(anchor=CENTER)
    head_col1 = Label(frame_head_col1,text="รหัสวิชา",font=(FONT_DEFULT,18),bg=BG_COLOR)
    head_col1.place(x=70)
    head_col2 = Label(frame_head_col2,text="หน่วยกิต",font=(FONT_DEFULT,18),bg=BG_COLOR)
    head_col2.place(x=5)
    head_col3 = Label(frame_head_col3,text="เกรด",font=(FONT_DEFULT,18),bg=BG_COLOR)
    head_col3.place(x=50)
    label_col1 = Label(frame_col1,text=show_sub,font=(FONT_DEFULT,18),bg=BG_COLOR)
    label_col1.place(x=80)
    label_col2 = Label(frame_col2,text=show_credit,font=(FONT_DEFULT,18),bg=BG_COLOR)
    label_col2.place(x=0)
    label_col3 = Label(frame_col3,text=show_grade,font=(FONT_DEFULT,18),bg=BG_COLOR,justify=LEFT)
    label_col3.place(x=20)
    Frame(frame_text,width=550,height=2,bg='black').place(x=70,y=360)
    
    
    frame_result = Frame(root,width=550, height=100, bg=BG_COLOR)
    frame_result.place(x=100,y=450)
    label_result1 = Label(frame_result,text="เกรดเฉลี่ยที่ได้คือ: 4.00   |",font=(FONT_DEFULT,18),bg=BG_COLOR,justify=LEFT)
    label_result1.grid(row=0,columnspan=2)
    label_result2 = Label(frame_result,text=" จำนวนหน่วยกิตทั้งหมด: 40",font=(FONT_DEFULT,18),bg=BG_COLOR,justify=LEFT)
    label_result2.grid(row=0,column=2)

    label_result1.config(text=(f"จำนวนหน่วยกิตทั้งหมด: {sum_credit}   |"))
    label_result2.config(text=(f" เกรดเฉลี่ยที่ได้คือ: {result_gpa:.2f}"))
    
    #ปุ่ม
    frame_button = Frame(root,width=550, height=120, bg=BG_COLOR)
    frame_button.place(x=100,y=520)
    button_backto_mainpage = Button(frame_button,width=32,pady=10,text='กลับหน้าหลัก',bg='#57a1f8',fg='white',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=backto_mainpage)
    button_backto_mainpage.place(x=130,y=0)
    button_clear_his = Button(frame_button,width=32,pady=10,text='ลบประวัติ',bg='#B0C4DE',fg='white',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=deleate_data)
    button_clear_his.place(x=130,y=60)
#------------------------------------------------------------------------------------------------------------
#หน้าหลัก
def mainpage():
    global result_gpa
    #run checkfile
    checkfile()
    #set f-string เพื่อเอาไปแสดงในwidget หรือoutput
    def update_label_gpa():
        result_display1.config(text=f"เกรดเฉลี่ยที่ได้คือ ")
        result_display2.config(text=f"{result_gpa:.2f}")
    def calculate():
        calculate_gpa()
        update_label_gpa()
        s1, s2, s3, s4,s5, s6, s7, s8,s9, s10 = sub1.get() ,sub2.get() ,sub3.get() ,sub4.get() ,sub5.get() ,sub6.get() ,sub7.get() ,sub8.get() ,sub9.get() ,sub10.get()
        c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = credit1.get(), credit2.get(), credit3.get(), credit4.get(), credit5.get(), credit6.get(), credit7.get(), credit8.get(), credit9.get(), credit10.get()
        g1 , g2, g3, g4, g5, g6, g7, g8, g9, g10 = grade1.get(), grade2.get(), grade3.get(), grade4.get(), grade5.get(), grade6.get(), grade7.get(), grade8.get(), grade9.get(), grade10.get()
        if g1 == "เลือกเกรด" or g1 == " ":
            s1 = "     "
            c1 = 0
            sub1.set(value="")
            credit1.set(value=0)
            grade1.set(value="เลือกเกรด")
        if g2 == "เลือกเกรด" or g2 == " ":
            s2 = "     "
            c2 = 0
            sub2.set(value="")
            credit2.set(value=0)
            grade2.set(value="เลือกเกรด")
        if g3 == "เลือกเกรด" or g3 == " ":
            s3 = "     "
            c3 = 0
            sub3.set(value="")
            credit3.set(value=0)
            grade3.set(value="เลือกเกรด")
        if g4 == "เลือกเกรด" or g4 == " ":
            s4 = "     "
            c4 = 0
            sub4.set(value="")
            credit4.set(value=0)
            grade4.set(value="เลือกเกรด")
        if g5 == "เลือกเกรด" or g5 == " ":
            s5 = "     "
            c5 = 0
            sub5.set(value="")
            credit5.set(value=0)
            grade5.set(value="เลือกเกรด")
        if g6 == "เลือกเกรด" or g6 == " ":
            s6 = "     "
            c6 = 0
            sub6.set(value="")
            credit6.set(value=0)
            grade6.set(value="เลือกเกรด")
        if g7 == "เลือกเกรด" or g7 == " ":
            s7 = "     "
            c7 = 0
            sub7.set(value="")
            credit7.set(value=0)
            grade7.set(value="เลือกเกรด")
        if g8 == "เลือกเกรด" or g8 == " ":
            s8 = "     "
            c8 = 0
            sub8.set(value="")
            credit8.set(value=0)
            grade8.set(value="เลือกเกรด")
        if g9 == "เลือกเกรด" or g9 == " ":
            s9 = "     "
            c9 = 0
            sub9.set(value="")
            credit9.set(value=0)
            grade9.set(value="เลือกเกรด")
        if g10 == "เลือกเกรด" or g10 == " ":
            s10 = "     "
            c10 = 0
            sub10.set(value="")
            credit10.set(value=0)
            grade10.set(value="เลือกเกรด")
        fw = open("History.txt", "w", encoding="utf-8")
        #การจัดการด้วยF-string จะทำให้เก็บเข้าไฟล์และนำของมาใช้ง่าย
        fw.writelines(str(f"{s1} {c1:10}      {g1}\n")) #จะเว้นช่องหลังจากรหัสวิชา 10ตัว และจะใส่ช่องว่างต่อจากรหัสวิชา 5ช่อง เพื่อให้สะดวกต่อการเอามาใช้ 
        fw.writelines(str(f"{s2} {c2:10}      {g2}\n"))
        fw.writelines(str(f"{s3} {c3:10}      {g3}\n"))
        fw.writelines(str(f"{s4} {c4:10}      {g4}\n"))
        fw.writelines(str(f"{s5} {c5:10}      {g5}\n"))
        fw.writelines(str(f"{s6} {c6:10}      {g6}\n"))
        fw.writelines(str(f"{s7} {c7:10}      {g7}\n"))
        fw.writelines(str(f"{s8} {c8:10}      {g8}\n"))
        fw.writelines(str(f"{s9} {c9:10}      {g9}\n"))
        fw.writelines(str(f"{s10} {c10:10}      {g10}\n"))

        fw.close()

    #clear หน้าหลักเพื่อไปหน้าอื่น
    def clear_mainpage():
        frame_title.destroy()
        frame_text.destroy()
        frame_button.destroy()
        frame_bg.destroy()
    #ล้างข้อมูลที่กรอกให้เป็นdefult แต่ไม่ใช่การล้างข้อมูลในไฟล์
    def clear_data():
        sub1.set(value="")
        sub2.set(value="")
        sub3.set(value="")
        sub4.set(value="")
        sub5.set(value="")
        sub6.set(value="")
        sub7.set(value="")
        sub8.set(value="")
        sub9.set(value="")
        sub10.set(value="")

        credit1.set(value=0)
        credit2.set(value=0)
        credit3.set(value=0)
        credit4.set(value=0)
        credit5.set(value=0)
        credit6.set(value=0)
        credit7.set(value=0)
        credit8.set(value=0)
        credit9.set(value=0)
        credit10.set(value=0)

        grade1.set(value="เลือกเกรด")
        grade2.set(value="เลือกเกรด")
        grade3.set(value="เลือกเกรด")
        grade4.set(value="เลือกเกรด")
        grade5.set(value="เลือกเกรด")
        grade6.set(value="เลือกเกรด")
        grade7.set(value="เลือกเกรด")
        grade8.set(value="เลือกเกรด")
        grade9.set(value="เลือกเกรด")
        grade10.set(value="เลือกเกรด")

        result_display1.config(text="")
        result_display2.config(text="")

    #ไปหน้าดูประวัติ
    def goto_history():
        clear_mainpage()
        result_his_page()

    #สร้างFrame สำหรับwidget
    frame_title = Frame(root,width=450, height=50, bg=BG_COLOR)
    frame_title.place(x=160,y=10)
    frame_text = Frame(root,width=660,height=435,bg=BG_COLOR)
    frame_text.place(x=45,y=80)
    frame_bg = Frame(frame_text,width=590,height=435,bg=RED_ORANGE)
    frame_bg.place(x=17,y=0)

    
    frame_head_col1 = Frame(frame_text,width=310,height=40,bg=RED_ORANGE)
    frame_head_col1.place(x=60,y=0)
    frame_head_col2 = Frame(frame_text,width=105,height=40,bg=RED_ORANGE)
    frame_head_col2.place(x=370,y=0)
    frame_head_col3 = Frame(frame_text,width=128,height=40,bg=RED_ORANGE)
    frame_head_col3.place(x=475,y=0)
    frame_num = Frame(frame_text,width=50,height=500,bg=RED_ORANGE)
    frame_num.place(x=23,y=45)
    frame_col1 = Frame(frame_text,width=325,height=500,bg=RED_ORANGE)
    frame_col1.place(x=60,y=40)
    frame_col2 = Frame(frame_text,width=120,height=500,bg=RED_ORANGE)
    frame_col2.place(x=365,y=40)
    frame_col3 = Frame(frame_text,width=150,height=500,bg=RED_ORANGE)
    frame_col3.place(x=475,y=40)

    #result
    frame_result = Frame(root,width=380,height=60, bg= BG_COLOR)
    frame_result.place(x=180,y=525)
    result_display1 = Label(frame_result,text=("เกรดเฉลี่ยที่ได้คือ :"),font=(FONT_DEFULT,26),bg=BG_COLOR)
    result_display1.place(x=10,y=2)
    result_display2 = Label(frame_result,text="",font=(FONT_DEFULT,28,BOLD),bg=BG_COLOR)
    result_display2.place(x=270,y=2)

    frame_button = Frame(root,width=400,height=120, bg= BG_COLOR)
    frame_button.place(x=160,y=590)

    title = Label(frame_title,text="โปรแกรมคำนวณเกรดเฉลี่ย",font=(FONT_DEFULT,26),bg=BG_COLOR,fg=FONT_COLOR)
    title.pack(anchor=CENTER)
    #หัวตาราง
    head_col1 = Label(frame_head_col1,text="รหัสวิชา",font=(FONT_DEFULT,18),bg=RED_ORANGE,fg=FONT_COLOR)
    head_col1.place(x=100)
    head_col2 = Label(frame_head_col2,text="หน่วยกิต",font=(FONT_DEFULT,18),bg=RED_ORANGE,fg=FONT_COLOR)
    head_col2.place(x=5)
    head_col3 = Label(frame_head_col3,text="เกรด",font=(FONT_DEFULT,18),bg=RED_ORANGE,fg=FONT_COLOR)
    head_col3.place(x=30)
    #ลำดับวิชา
    num = Label(frame_num,text="1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n10.",font=(FONT_DEFULT,22),bg=RED_ORANGE,fg=FONT_COLOR)
    num.pack(anchor=N)
    
    #รหัสวิชา
    subject = Entry(frame_col1,textvariable=sub1,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)
    subject = Entry(frame_col1,textvariable=sub2,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)
    subject = Entry(frame_col1,textvariable=sub3,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)
    subject = Entry(frame_col1,textvariable=sub4,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)
    subject = Entry(frame_col1,textvariable=sub5,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)
    subject = Entry(frame_col1,textvariable=sub6,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)
    subject = Entry(frame_col1,textvariable=sub7,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)
    subject = Entry(frame_col1,textvariable=sub8,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)
    subject = Entry(frame_col1,textvariable=sub9,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)
    subject = Entry(frame_col1,textvariable=sub10,font=(FONT_DEFULT,20),justify=LEFT)
    subject.pack(anchor=E)

    #หน่วยกิต
    credit = Entry(frame_col2,textvariable=credit1,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    credit = Entry(frame_col2,textvariable=credit2,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    credit = Entry(frame_col2,textvariable=credit3,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    credit = Entry(frame_col2,textvariable=credit4,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    credit = Entry(frame_col2,textvariable=credit5,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    credit = Entry(frame_col2,textvariable=credit6,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    credit = Entry(frame_col2,textvariable=credit7,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    credit = Entry(frame_col2,textvariable=credit8,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    credit = Entry(frame_col2,textvariable=credit9,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    credit = Entry(frame_col2,textvariable=credit10,font=(FONT_DEFULT,20),justify=RIGHT,width=7)
    credit.pack(anchor=E)
    
    #เกรด
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade1,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack(pady=2)
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade2,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack()
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade3,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack(pady=2)
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade4,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack()
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade5,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack(pady=2)
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade6,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack()
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade7,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack(pady=2)
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade8,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack()
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade9,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack(pady=2)
    grade = ttk.Combobox(frame_col3,width=8,font=(FONT_DEFULT,18),textvariable=grade10,justify=RIGHT)
    grade["values"]=(" ","A","B+","B","C+","C","D+","D","F")
    grade.pack(pady=2)
    

    #ปุ่มหน้าแรก คำนวณ ดูประวัติ และออกจากโปรแกรม
    button_cal = Button(frame_button,width=32,pady=10,text='คำนวณ',bg='#57a1f8',fg='white',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=calculate)
    button_cal.place(x=50,y=0)
    button_clear = Button(frame_button,width=19,pady=4,text='ล้างข้อมูล',bg='#B0C4DE',fg="white",border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=clear_data)
    button_clear.place(x=5,y=65)
    button_history = Button(frame_button,width=19,pady=4,text='ประวัติ',bg='#B0C4DE',fg="white",border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=goto_history)
    button_history.place(x=205,y=65)

#function ไว้รันmainโปรแกรม
def main():
    mainpage()
main()
root.mainloop()