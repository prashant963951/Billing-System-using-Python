from tkinter import*
import random
import os
from tkinter import messagebox

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#badc57"
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#badc57", fg="Black", relief=GROOVE)
        title.pack(fill=X)
    # ================variables=======================
        self.Player_Adition = IntVar()
        self.Pro = IntVar()
        self.Stream_cxl = IntVar()
        self.Super_Gold = IntVar()
        self.Club = IntVar()
        self.Pro_700 = IntVar()

    # ============Bats==============================
        self.English_Willow = IntVar()
        self.Kasmiri_Willow = IntVar()
        self.Sibrian_Willow = IntVar()
        
        #=============Ball=============================
        self.Red_First = IntVar()
        self.Red_Second = IntVar()
        self.Red_Third = IntVar()
        self.White_First = IntVar()
        self.White_Second = IntVar()
        self.White_Third = IntVar()

    # ==============Total product price================
        self.Batting_Gloves_price = StringVar()
        self.Bats_price = StringVar()
        self.Ball_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.Batting_Gloves_tax = StringVar()
        self.Bats_tax = StringVar()
        self.Ball_tax = StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#badc57", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#badc57", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    # ===================Batting_Gloves====================================
        F2 = LabelFrame(self.root, text="Batting Gloves", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F2.place(x=5, y=180, width=325, height=380)

        Player_Adition_lbl = Label(F2, text="Player_Adition", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Player_Adition_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        Player_Adition_txt = Entry(F2, width=10, textvariable=self.Player_Adition, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Player_Adition_txt.grid(row=0, column=1, padx=10, pady=10)

        Pro_lbl = Label(F2, text="Pro", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Pro_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Pro_txt = Entry(F2, width=10, textvariable=self.Pro, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Pro_txt.grid(row=1, column=1, padx=10, pady=10)

        Stream_cxl_lbl = Label(F2, text="Stream_cxl", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Stream_cxl_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Stream_cxl_txt = Entry(F2, width=10, textvariable=self.Stream_cxl, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        Stream_cxl_txt.grid(row=2, column=1, padx=10, pady=10)

        Super_Gold_lbl = Label(F2, text="Super_Gold", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Super_Gold_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        Super_Gold_txt = Entry(F2, width=10, textvariable=self.Super_Gold, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Super_Gold_txt.grid(row=3, column=1, padx=10, pady=10)

        Club_lbl = Label(F2, text="Club", font =('times new roman', 16, 'bold'), bg = "#badc57", fg = "black")
        Club_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        Club_txt = Entry(F2, width=10, textvariable=self.Club, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Club_txt.grid(row=4, column=1, padx=10, pady=10)

        Pro_700_lbl = Label(F2, text="Thermal Gun", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Pro_700_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        Pro_700_txt = Entry(F2, width=10, textvariable=self.Pro_700, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Pro_700_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========BatsItems=========================
        F3 = LabelFrame(self.root, text="Bats Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F3.place(x=340, y=180, width=325, height=380)

        English_Willow_lbl = Label(F3, text="English_Willow", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        English_Willow_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        English_Willow_txt = Entry(F3, width=10, textvariable=self.English_Willow, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        English_Willow_txt.grid(row=0, column=1, padx=10, pady=10)

        Kasmiri_Willow_lbl = Label(F3, text="Kasmiri_Willow", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Kasmiri_Willow_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Kasmiri_Willow_txt = Entry(F3, width=10, textvariable=self.Kasmiri_Willow, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Kasmiri_Willow_txt.grid(row=1, column=1, padx=10, pady=10)

        Sibrian_willow_lbl = Label(F3, text="Sibrian_Willow", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Sibrian_willow_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Sibrian_willow_txt = Entry(F3, width=10, textvariable=self.Sibrian_Willow, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Sibrian_willow_txt.grid(row=2, column=1, padx=10, pady=10)


    # ===========Ball================================
        F4 = LabelFrame(self.root, text="Ball", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F4.place(x=670, y=180, width=325, height=380)

        Red_First_lbl = Label(F4, text="Red_First", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Red_First_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        Red_First_txt = Entry(F4, width=10, textvariable=self.Red_First, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Red_First_txt.grid(row=0, column=1, padx=10, pady=10)

        Red_Second_lbl = Label(F4, text="Red_Second", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Red_Second_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Red_Second_txt = Entry(F4, width=10, textvariable=self.Red_Second, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Red_Second_txt.grid(row=1, column=1, padx=10, pady=10)

        Red_Third_lbl = Label(F4, text="Red_Third", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        Red_Third_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Red_Third_txt = Entry(F4, width=10, textvariable=self.Red_Third, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Red_Third_txt.grid(row=2, column=1, padx=10, pady=10)

        White_First_lbl = Label(F4, text="White_First", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        White_First_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        White_First_txt = Entry(F4, width=10, textvariable=self.White_First, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        White_First_txt.grid(row=3, column=1, padx=10, pady=10)

        White_Second_lbl = Label(F4, text="White_Second", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        White_Second_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        White_Second_txt = Entry(F4, width=10, textvariable=self.White_Second, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        White_Second_txt.grid(row=4, column=1, padx=10, pady=10)

        White_Third_lbl = Label(F4, text="White_Third", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        White_Third_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        White_Third_txt = Entry(F4, width=10, textvariable=self.White_Third, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        White_Third_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Tax Invoice", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="#badc57")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Batting_Gloves Price", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.Batting_Gloves_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Bats Price", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.Bats_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Ball Price", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.Ball_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Batting_Gloves Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.Batting_Gloves_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Bats Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.Bats_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Ball Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.Ball_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

#================totalBill==========================
    def total(self):
        self.m_h_g_p = self.Stream_cxl.get()*900
        self.m_s_p = self.Player_Adition.get()*1300
        self.m_m_p = self.Pro.get()*1300
        self.m_d_p = self.Super_Gold.get()*750
        self.m_n_p = self.Club.get()*500
        self.m_t_g_p = self.Pro_700.get()*350
        self.total_Batting_Gloves_price = float(self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)

        self.Batting_Gloves_price.set("Rs. "+str(self.total_Batting_Gloves_price))
        self.b_g_tax = round((self.total_Batting_Gloves_price*0.12), 2)
        self.Batting_Gloves_tax.set("Rs. "+str(self.b_g_tax))

        self.g_r_p = self.English_Willow.get()*5000
        self.g_f_o_p = self.Kasmiri_Willow.get()*1500
        self.g_w_p = self.Sibrian_Willow.get()*2000
        self.total_Bats_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p)

        self.Bats_price.set("Rs. " + str(self.total_Bats_price))
        self.b_t_tax = round((self.total_Bats_price*0.12), 2)
        self.Bats_tax.set("Rs. " + str(self.b_t_tax))

        self.b_l_s_p = self.Red_First.get()*300
        self.b_l_l_p = self.Red_Second.get()*270
        self.b_l_m_p = self.Red_Third.get()*230
        self.b_l_c_p = self.White_First.get()*320
        self.b_l_f_p = self.White_Second.get()*290
        self.c_m_d = self.White_Third.get()*260
        self.total_Ball_price = float(self.b_l_s_p+self.b_l_l_p+self.b_l_m_p+self.b_l_c_p+self.b_l_f_p+self.c_m_d)

        self.Ball_price.set("Rs. "+str(self.total_Ball_price))
        self.b_l_tax = round((self.total_Ball_price * 0.12), 2)
        self.Ball_tax.set("Rs. "+str(self.b_l_tax))

        self.total_bill = float(self.total_Batting_Gloves_price+self.total_Bats_price+self.total_Ball_price+self.b_g_tax+self.b_t_tax+self.b_l_tax)

#==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome To S.K.sports")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

#=========billArea=================================================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.Batting_Gloves_price.get() == "Rs. 0.0" and self.Bats_price.get() == "Rs. 0.0" and self.Ball_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============Batting_Gloves===========================
        if self.Player_Adition.get() != 0:
            self.txtarea.insert(END, f"\n Player_Adition\t\t{self.Player_Adition.get()}\t\t{self.m_s_p}")
        if self.Pro.get() != 0:
            self.txtarea.insert(END, f"\n Player_Adition\t\t{self.Pro.get()}\t\t{self.m_m_p}")
        if self.Stream_cxl.get() != 0:
            self.txtarea.insert(END, f"\n Stream_cxl\t\t{self.Stream_cxl.get()}\t\t{self.m_h_g_p}")
        if self.Super_Gold.get() != 0:
            self.Super_Goldtxtarea.insert(END, f"\n Super_Gold\t\t{self.Super_Gold.get()}\t\t{self.m_d_p}")
        if self.Club.get() != 0:
            self.txtarea.insert(END, f"\n Club\t\t{self.Club.get()}\t\t{self.m_n_p}")
        if self.Pro_700.get() != 0:
            self.txtarea.insert(END , f"\n Thermal Gun\t\t{self.Player_Adition.get()}\t\t{self.m_t_g_p}")
    # ==============Bats============================
        if self.English_Willow.get() != 0:
            self.txtarea.insert(END, f"\n English_Willow\t\t{self.English_Willow.get()}\t\t{self.g_r_p}")
        if self.Kasmiri_Willow.get() != 0:
            self.txtarea.insert(END, f"\n Kasmiri_Willow\t\t{self.Kasmiri_Willow.get()}\t\t{self.g_f_o_p}")
        if self.Sibrian_Willow.get() != 0:
            self.txtarea.insert(END, f"\n Sibrian_Willow\t\t{self.Sibrian_Willow.get()}\t\t{self.g_w_p}")

        #================Ball==========================
        if self.Red_First.get() != 0:
            self.txtarea.insert(END, f"\n Red_First\t\t{self.Red_First.get()}\t\t{self.b_l_s_p}")
        if self.Red_Second.get() != 0:
            self.txtarea.insert(END, f"\n Player_Adition\t\t{self.Red_Second.get()}\t\t{self.b_l_l_p}")
        if self.Red_Third.get() != 0:
            self.txtarea.insert(END, f"\n Red_Third\t\t{self.Red_Third.get()}\t\t{self.b_l_m_p}")
        if self.White_First.get() != 0:
            self.txtarea.insert(END, f"\n Super_Gold\t\t{self.White_First.get()}\t\t{self.b_l_c_p}")
        if self.White_Second.get() != 0:
            self.txtarea.insert(END, f"\n White_Second\t\t{self.Club.get()}\t\t{self.b_l_f_p}")
        if self.White_Third.get() != 0:
            self.txtarea.insert(END, f"\n White_Third\t\t{self.Player_Adition.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n-------------------------------------")
        # ===============taxes==============================
        if self.Batting_Gloves_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Batting_Gloves Tax\t\t\t{self.Batting_Gloves_tax.get()}")
        if self.Bats_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Bats Tax\t\t\t{self.Bats_tax.get()}")
        if self.Ball_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Ball Tax\t\t\t{self.Ball_tax.get()}")
        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------------")
        self.save_bill()

    #=========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.Player_Adition.set(0)
            self.Pro.set(0)
            self.Stream_cxl.set(0)
            self.Super_Gold.set(0)
            self.Club.set(0)
            self.Pro_700.set(0)
    # ============Bats==============================
            self.English_Willow.set(0)
            self.Kasmiri_Willow.set(0)
            self.Sibrian_Willow.set(0)
            
    # =============Ball=============================
            self.Red_First.set(0)
            self.Red_Second.set(0)
            self.Red_Third.set(0)
            self.White_First.set(0)
            self.White_Second.set(0)
            self.White_Third.set(0)
    # ====================taxes================================
            self.Batting_Gloves_price.set("")
            self.Bats_price.set("")
            self.Ball_price.set("")

            self.Batting_Gloves_tax.set("")
            self.Bats_tax.set("")
            self.Ball_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()