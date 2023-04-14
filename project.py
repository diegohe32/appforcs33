
Conversations
2.28 GB of 15 GB used
Terms · Privacy · Program Policies
Last account activity: 2 minutes ago
Details
from tkinter import *
from tkinter import ttk
import sqlite3 
height = 500
width = 500

'''
How I created the sqlite table uncomment this if your gonna run it for the first time and then recooment it out so the table isnt brand new everytime

cursor.execute("""CREATE TABLE userInfo(
    first_name text,
    last_name text,
    pronoun text,
   
    
)""")
'''

    
def main():
    
    
    root = Tk()
    app = Window1(root)
    root.mainloop()
#initial page
class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Page")
        self.master.geometry(f"{height}x{width}")
        self.master.config( bg = "white")
        self.frame = Frame(self.master)
        self.frame.config(bg = "white", )
        self.frame.pack()
        
        
        

        
        Label( self.frame, bg = "white",text = "" , height = 3, width = 20).grid(row = 0, column= 0)
        btnReg = Button(self.frame , height = 3 , width=15,bg="white", text="Register", command=self.register)
        btnReg.grid(row = 2, column = 0)
        Button(self.frame, height=3, width=15,bg="white", text="Login",command=self.login ).grid(row=1,column=0)
        
        
    def register(self):
        newWindow = Toplevel(self.master)
        app = Register(newWindow)
    def login(self):
        newWindow = Toplevel(self.master)
        app = Login(newWindow)
        

class Confirm:
    def __init__(self, master, first_name, lastName, pronoun,age,monthly_income,subscription, ):
        
        self.master = master
        self.master.config(bg = "white")
        self.master.title("Confirm")
        self.master.geometry("250x200+0+0")
        
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0)
        self.frame.pack()
        self.user_fields_frame = LabelFrame(self.frame, )
        
        self.user_fields_frame.grid(row=1,column=0)
        
        self.title = Label(self.frame, text ="Conformation Page", width = 30)
        Label(self.user_fields_frame, text = f"Name: {first_name} {lastName}").grid(row=0,column=0)
        Label(self.user_fields_frame, text = f"Pronouns: {pronoun}").grid(row=1,column=0)
        Label(self.user_fields_frame, text = f"Age: {age}").grid(row=2,column=0)
        Label(self.user_fields_frame, text = f"Monthly Income: {monthly_income}").grid(row=3,column=0)
        Label(self.user_fields_frame, text= f"Subscriptions").grid(row=0,column=1)
        for i,v in enumerate(subscription,1):
            Label(self.user_fields_frame, text = v, ).grid(row  = i, column=1)
        
        
        Button(self.frame, text="Confirm", command=lambda:[self.homepage(), self.addDataToTable(first_name, lastName, pronoun)]).grid(row=4,column=0)
        Button(self.frame, text= "Decline", command=self.reset()).grid(row=5, column=0)
        
        
        self.title.grid(row = 0, column=0)
        
    def homepage(self):
        new_window = Toplevel(self.master)
        self.HOME = HomePage(new_window)
        
    def addDataToTable(self,first_name, lastName, pronoun):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO userInfo VALUES (:first_name, :last_name,:pronoun )",
                       {
                           "first_name":first_name,
                           "last_name":lastName,
                           'pronoun':pronoun,
                           
                       })
        connection.commit()
        connection.close()
        
    def reset(self):

        app = Toplevel(self.master)
        setted = Register(app)
        
        
        

        
class HomePage:
    def __init__(self,master):
        self.master = master
        self.master.config(bg = "white")
        self.master.title("HomePage")
        self.master.geometry(f"{height}x{width}")
        Label(self.master,text ="",height=1,bg="white" ).pack()
        
        self.notebook = ttk.Notebook(self.master)
       
        self.welcome_tab = Frame(self.notebook, bg = "white")
        Label(self.welcome_tab,bg = "white", text="Hello and welcome").pack()
        Button(self.welcome_tab, text= "Show records", command=self.show() ).pack()
        
        self.graphs_tab = Frame(self.notebook, bg = "white")
        Label(self.graphs_tab, text="This is gonna be a graph of your spending ").pack()
        
        
        self.welcome_tab.pack(fill= "both", expand=1)
        
        self.notebook.add(self.welcome_tab, text= "Welcome")
        self.notebook.add(self.graphs_tab, text="Graphs")
        self.notebook.pack()
    def show(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        records = cursor.execute("SELECT * FROM userInfo")
        stringrecords = ""
        for record in records:
            stringrecords+= str(record) + "\n"
        Label(self.welcome_tab, text = f"{stringrecords}").pack()
        
        connection.commit()
        connection.close()
        
        
class Register:
    def __init__(self, master):
        self.user_subscription_and_price = {}
        self.providers = []
        
        self.master = master
        self.master.config(bg = "white")
        self.master.title("Session")
        self.master.geometry(f"{height}x{width}")
        #creating master frame that other frames live inside
        self.frame = Frame(self.master)
        self.frame.pack()
    
        self.user_info_frame = LabelFrame(self.frame)
        self.user_info_frame.grid(row = 0 , column= 0, padx=20,pady=10 )
       
        

        #widgets for first frame
        first_name_label = Label(self.user_info_frame, text = "First Name")
        last_name_label = Label(self.user_info_frame,text = "Last Name")
        pronouns_label = Label(self.user_info_frame, text = "Pronouns")
        self.pronouns = ttk.Combobox(self.user_info_frame, values =["He", "Her", "They"])
        self.first_name_entry = Entry(self.user_info_frame)
        self.last_name_entry = Entry (self.user_info_frame)
        age_label = Label(self.user_info_frame, text = "Age")
        self.age = Spinbox(self.user_info_frame, from_= 18 , to=100)
        
        
        first_name_label.grid(row = 0, column=0)
        last_name_label.grid(row =0, column=1)
        pronouns_label.grid(row = 0, column=2)
        self.first_name_entry.grid(row = 1, column=0)
        self.last_name_entry.grid(row = 1, column=1)
        self.pronouns.grid(row= 1, column=2)
        age_label.grid(row = 2, column=0,)
        self.age.grid(row = 3, column=0)
        #adding a padding to all widgets to look cleaner
        for wid in self.user_info_frame.winfo_children():
            wid.grid_configure(padx=1,pady=5)
            
        #creating 2nd frame
        self.user_finance_info = LabelFrame(self.frame)
        self.user_finance_info.grid(row=1, column=0 , sticky="news", padx=20,pady=20)
        #Label frame to display users subscriptions as they sign up
        self.display_sub = LabelFrame(self.user_finance_info )
        #widgets for 2nd frame
        subscription_label = Label(self.user_finance_info,text = "Enter your Subscription")
        self.current_subscription = Entry(self.user_finance_info)
        price = Label(self.user_finance_info, text = "Price of Subscription per month")
        self.sub_price = Entry(self.user_finance_info,)
        self.add_sub = Button( self.user_finance_info, text = "Add Subscription", command= self.add_subscription)
        Subscription = Label(self.user_finance_info, text = "Current Subscriptions")
        monthly_income_label = Label(self.user_finance_info, text="Enter your monthly income" )
        self.monthly_income = Entry(self.user_finance_info)
        
        subscription_label.grid(row = 0, column=0)
        self.current_subscription.grid(row=1, column=0)
        self.add_sub.grid(row=2,column=0)
        self.sub_price.grid(row = 1, column=1)
        price.grid(row = 0 , column=1)
        Subscription.grid(row =0, column=2) 
        self.display_sub.grid(row = 1, column = 2 , sticky = "news")
        monthly_income_label.grid(row =3 , column=0 )
        self.monthly_income.grid(row=4,column=0)
        
        for wid in self.user_finance_info.winfo_children():
            wid.grid_configure(padx=3,pady=5)
            
        #3rd frame for users to confirm and register
        self.confirm_frame = LabelFrame(self.frame)
        self.confirm_frame.grid(row=2,column=0)
        
        confirm_btn = Button(self.confirm_frame, text="Register", command=self.confirm)
        confirm_btn.grid(row= 0 ,column=0)
        
        #for when users register 
    def add_subscription(self):
        self.user_subscription_and_price[self.current_subscription.get()] = self.sub_price.get()
        self.providers.append(self.current_subscription.get())
        for i in range(len(self.providers)):
            Label(self.display_sub,text = f"{self.providers[i]}").grid(row = i, column=0)
        #clear text boxes
        self.sub_price.delete(0,END)
        self.current_subscription.delete(0,END)
    
    def confirm(self):
        new_window = Toplevel(self.master )
        self.confirm_window = Confirm(new_window, self.first_name_entry.get(), self.last_name_entry.get(), self.pronouns.get(), self.age.get(), self.monthly_income.get(), self.providers)
        
class Login():
    def __init__(self, master) :
        self.master = master
        self.master.config(bg = "white")
        self.master.title("Login")
        self.master.geometry(f"{height}x{width}")
        
        self.frame = Frame(self.master)
        self.frame.config(bg= "white")
        self.frame.pack()
        
        Label(self.frame, text ="",bg= "white", height = 3, width = 20 ).grid(column=0,row=0)
        Label(self.frame, text ="Username:"  ,bg="white").grid(column=0,row=1)
        Entry(self.frame, ).grid(row=1,column=1)
        Label(self.frame, text ="Password:"  ,bg="white").grid(column=0,row=2)
        Entry(self.frame, ).grid(row=2,column=1)
        Button(self.frame, text= "Login", command=self.homepage).grid(column = 1, row = 3)
        
    def homepage(self):
        new_window = Toplevel(self.master)
        self.HOME = HomePage(new_window)
        
        
        
        
        
        
            
        
        
        
        
        
   
        
        
       
        
        
        
    
    
if __name__ == '__main__':
    main()
