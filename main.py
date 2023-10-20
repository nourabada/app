import sqlite3

from kivy.lang import Builder
from kivymd.app import MDApp
#from kivymd.uix.label import MDLabel
#from kivymd.uix.responsivelayout import MDResponsiveLayout
#from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
#from kivymd.uix.card import MDCard
#from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.button import MDRectangleFlatButton,MDIconButton
#from kivymd.uix.textfield import MDTextField
#from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
#from kivymd.uix.menu import MDDropdownMenu
KV = '''
ScreenManager:
    StartPage:
    LoginPage:
    MainPage:
    ControlRoom:
    ProfilePage:

        
<Content>:
    #name:Content
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    size_hint_x:0.6
    height: "120dp"
    
    MDTextField:
        id:add_text1
        hint_text_color_normal: "white"
        hint_text_color_focus: "white"
        hint_text: "Enter Button Name"
        line_color_focus: "orange"
        text_color_focus : 'white'
    

<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#c5bdd2"
    text_color: "orange"
    icon_color: "orange"
    ripple_color: "black"
    selected_color: "orange"
    focus_behavior: False
    
<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "orange"
    focus_color: "black"
    icon_color: "orange"
    focus_behavior: False
    selected_color: "orange"
    _no_ripple_effect: False

<StartPage>:
    name:"start"
    MDScreen:
        md_bg_color:'orange'
        size_hint_x: 1
        size_hint_y: 1
        RelativeLayout:
            id:"relative"
            FitImage:
                source: "start2.jpg"
                size_hint_y: 1
                size_hint_x: 1
                pos_hint: {"top": 1}
            MDCard:
                size_hint_y: 1
                size_hint_x: 1
                pos_hint: {"top": 1}
                radius: 0, 0, 0, 0
                md_bg_color:(0,0,0,0.45)
            FitImage:
                source: "start7.png"
                radius: 0, 0, 0,0
                size_hint_y: 0.5
                size_hint_x: 0.7
                pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            MDSpinner:
                size_hint: None, None
                size: '60dp', '60dp'
                #size_hint: 0.3 , 0.3
                pos_hint: {'center_x': 0.5, 'center_y': 0.15}
                active: True
                color:"orange"
            MDLabel:
                id:l5
                font_style:"H6"
                adaptive_size: True
                pos_hint: {"top": 0.03}
                #pos_hint: {"center_x": .0, "center_y": .02}
                text: "Made by : Nour Abada"
                    


<LoginPage>:
    name:"test1"
    BoxLayout:
        id : box
        orientation: 'vertical'
        halign: "center"
        MDScreen:
            name:"screen1"
            halign: "center"
            size_hint_x: 1
            size_hint_y: 1
            RelativeLayout:
                
                MDBottomNavigation:
                    id:bn1
                    panel_color: "black"
                    selected_color_background: "orange"
                    text_color_active: "orange"
                    text_color_normal : 'white'
                    
                    MDBottomNavigationItem:
                        id : bi1
                        name: 'screen 1'
                        text: 'sign in'
                        icon: 'login'
                        FitImage:
                            source: "start2.jpg"
                            size_hint_y: 1
                            size_hint_x: 1
                            pos_hint: {"top": 1}
                        MDCard:
                            size_hint_y: 1
                            size_hint_x: 1
                            pos_hint: {"top": 1}
                            radius: 0, 0, 0, 0
                            md_bg_color:(0,0,0,0.45)
                        BoxLayout:
                            orientation: 'vertical'
                            pos_hint: {"center_x": .5, "center_y": .7}
                            padding: dp(16)
                            spacing: dp(16)
                            
        
                            MDLabel:
                                font_style:"H4"
                                adaptive_size: True
                                pos_hint: {"center_x": .5, "center_y": .5}
                                text: "sign in"
                
                            
                            MDTextField:
                                id: text_field1
                                hint_text: "Enter Your Name"
                                helper_text: "There will always be a mistake"
                                helper_text_mode: "on_error"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                hint_text_color_normal: "white"
                                hint_text_color_focus: "white"
                                line_color_focus: "orange"
                                text_color_focus : 'white'
                                
                            MDTextField:
                                id: text_field2
                                password: True
                                hint_text: "Enter Your Password"
                                helper_text: "There will always be a mistake"
                                helper_text_mode: "on_error"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                hint_text_color_normal: "white"
                                hint_text_color_focus: "white"
                                line_color_focus: "orange"
                                text_color_focus : 'white'
                            
        
                            MDRectangleFlatButton:
                                size_hint_x: 0.3
                                pos_hint: {"center_x": .5, "center_y": .5}
                                text: "sign in"
                                theme_text_color: "Custom"
                                text_color: "white"
                                font_size:20
                                line_width:1.5
                                line_color:"orange"
                                on_release: app.sign_in()
                                
                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'sign up'
                        icon: 'account'
                        FitImage:
                            source: "start2.jpg"
                            size_hint_y: 1
                            size_hint_x: 1
                            pos_hint: {"top": 1}
                        MDCard:
                            size_hint_y: 1
                            size_hint_x: 1
                            pos_hint: {"top": 1}
                            radius: 0, 0, 0, 0
                            md_bg_color:(0,0,0,0.45)
                        BoxLayout:
                            orientation: 'vertical'
                            pos_hint: {"center_x": .5, "center_y": .6}
                            padding: dp(16)
                            spacing: dp(16)
                            
        
                            MDLabel:
                                font_style:"H4"
                                adaptive_size: True
                                pos_hint: {"center_x": .5, "center_y": .5}
                                text: "sign up"
                
                            
                            MDTextField:
                                id: text_field3
                                hint_text: "Enter Your Name"
                                helper_text: "There will always be a mistake"
                                helper_text_mode: "on_error"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                hint_text_color_normal: "white"
                                hint_text_color_focus: "white"
                                line_color_focus: "orange"
                                text_color_focus : 'white'
                                
                            MDTextField:
                                id: text_field4
                                password: True
                                hint_text: "Enter Your Password"
                                helper_text: "There will always be a mistake"
                                helper_text_mode: "on_error"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                hint_text_color_normal: "white"
                                hint_text_color_focus: "white"
                                line_color_focus: "orange"
                                text_color_focus : 'white'
                                
                            MDTextField:
                                id: text_field5
                                password: True
                                hint_text: "Confirm Your Password"
                                helper_text: "There will always be a mistake"
                                helper_text_mode: "on_error"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                hint_text_color_normal: "white"
                                hint_text_color_focus: "white"
                                line_color_focus: "orange"
                                text_color_focus : 'white'
                            
        
                            MDRectangleFlatButton:
                                size_hint_x: 0.3
                                pos_hint: {"center_x": .5, "center_y": .5}
                                text: "sign up"
                                theme_text_color: "Custom"
                                text_color: "white"
                                font_size:20
                                line_width:1.5
                                line_color:"orange"
                                on_release: app.sign_up()
           
            
<MainPage>:
    name:"test2"
    MDScreen:
        size_hint_x: 1
        size_hint_y: 1
        RelativeLayout:
            
            FitImage:
                source: "start2.jpg"
                size_hint_y: 1
                size_hint_x: 1
                pos_hint: {"top": 1}
            MDCard:
                size_hint_y: 1
                size_hint_x: 1
                pos_hint: {"top": 1}
                radius: 0, 0, 0, 0
                md_bg_color:(0,0,0,0.45)
            
            MDBottomAppBar:
                elevation:5
                shadow_color:"#f2960d"
                shadow_offset: 12,12
                radius: 36, 36, 0, 36
                MDTopAppBar:
                    
                    icon_color: 0, 0, 0, 1
                    md_bg_bottom_color:"black"
                    icon: "home-plus"
                    type: "bottom"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    on_action_button: app.screen_nev()
            
            
            MDCard:
                radius: 36
                pos_hint: {"center_x": .5, "center_y": .75}
                size_hint: .8, .4
                elevation:4
                shadow_softness:15
                shadow_color:"white"
    
                FitImage:
                    source: "17.jpg"
                    size_hint: 1, 1
                    pos_hint: {"top": 1}
                    radius: 36, 36, 36, 36
            MDLabel:
                id:l_main
                pos_hint: {"center_x": .5, "center_y": .32}
                text: ""
                theme_text_color: "Primary"
                padding:10
                size_hint: 0.7, 0.8
                font_size: 40  # Adjust the width to wrap text
                halign: "center"
                valign: "middle"
            
                
        
            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)
                md_bg_color:"black"
                elevation:5
                shadow_color:"white"
                MDNavigationDrawerMenu:
    
                    MDNavigationDrawerHeader:
                        title: "Home Control"
                        title_color: "white"
                        #text: "Header text"
                        spacing: "4dp"
                        padding: "12dp", 0, 0, "56dp"
    
                    MDNavigationDrawerLabel:
                        text: "System"
    
                    DrawerClickableItem:
                        icon: "home"
                        text: "Home"
                        on_release: app.on_item_select("Home","test2")
                    
                    DrawerClickableItem:
                        icon: "home-plus"
                        text: "Control"
                        on_release: app.on_item_select("Control","test3")
    
                    DrawerClickableItem:
                        icon: "account"
                        text: "Outbox"
                        on_release: app.on_item_select("Outbox","test4")
<ControlRoom>:
    name:"test3"
    MDScreen:
        md_bg_color:'black'
        size_hint_x: 1
        size_hint_y: 1
        RelativeLayout:
            id:"relative"
            
            MDCard:
                size_hint_y: 0.8
                size_hint_x: 1
                pos_hint: {"top": 1}
                radius: 0, 0, 36, 36
                elevation:4
                shadow_softness:12
                shadow_color:"white"
                FitImage:
                    source: "2.jpg"
                    radius: 0, 0, 36, 36
            MDCard:
                size_hint_y: 0.8
                size_hint_x: 1
                pos_hint: {"top": 1}
                radius: 0, 0, 36, 36
                md_bg_color:(0,0,0,0.3)
            
            MDRectangleFlatButton:
                text:"Add New Element"
                text_color:"white"
                font_size:26
                md_bg_color: (0,0,0,0.35)
                radius: 16, 16, 36, 16
                size_hint: .6, 0.1
                ripple_behavior: True
                line_width:1.5
                line_color:"orange"
                pos_hint: {"center_x": .5, "center_y": 0.1}
                on_release: app.channel_info()
            
            RelativeLayout:
                id:relative
            
            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)
                md_bg_color:"black"
                elevation:5
                shadow_color:"white"
                MDNavigationDrawerMenu:
    
                    MDNavigationDrawerHeader:
                        title: "Home Control"
                        title_color: "white"
                        #text: "Header text"
                        spacing: "4dp"
                        padding: "12dp", 0, 0, "36dp"
                    
                    MDNavigationDrawerDivider:
                        
                    MDNavigationDrawerLabel:
                        text: "System"
    
                    DrawerClickableItem:
                        icon: "home"
                        text: "Home"
                        on_release: app.on_item_select("Home","test2")
                    
                    DrawerClickableItem:
                        icon: "home-plus"
                        text: "Control"
                        on_release: app.on_item_select("Control","test3")
    
                    DrawerClickableItem:
                        icon: "account"
                        text: "Outbox"
                        on_release: app.on_item_select("Outbox","test4")
<ProfilePage>:
    name:"test4"
    MDScreen:
        size_hint_x: 1
        size_hint_y: 1
        RelativeLayout:
            
            FitImage:
                source: "start2.jpg"
                size_hint_y: 1
                size_hint_x: 1
                pos_hint: {"top": 1}
            MDCard:
                size_hint_y: 1
                size_hint_x: 1
                pos_hint: {"top": 1}
                radius: 0, 0, 0, 0
                md_bg_color:(0,0,0,0.35)
            MDLabel:
                icon: "account"
                font_style:"H1"
                adaptive_size: True
                pos_hint: {"center_x": .5, "center_y": .85}
                text: "Profile"
            MDLabel:
                id:l1
                font_style:"H2"
                adaptive_size: True
                pos_hint: {"center_x": .5, "center_y": .65}
                text: ""
            MDLabel:
                id:l2
                font_style:"H3"
                adaptive_size: True
                pos_hint: {"center_x": .5, "center_y": .55}
                text: ""
            MDLabel:
                id:l3
                font_style:"H3"
                adaptive_size: True
                pos_hint: {"center_x": .5, "center_y": .45}
                text: ""
            MDLabel:
                id:l4
                font_style:"H3"
                adaptive_size: True
                pos_hint: {"center_x": .5, "center_y": .35}
                text: ""
            MDLabel:
                id:l5
                font_style:"H6"
                adaptive_size: True
                pos_hint: {"top": 0.03}
                #pos_hint: {"center_x": .0, "center_y": .02}
                text: "Made by : Nour Abada"
            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)
                md_bg_color:"black"
                elevation:5
                shadow_color:"white"
                MDNavigationDrawerMenu:
    
                    MDNavigationDrawerHeader:
                        title: "Home Control"
                        title_color: "white"
                        #text: "Header text"
                        spacing: "4dp"
                        padding: "12dp", 0, 0, "56dp"
    
                    MDNavigationDrawerLabel:
                        text: "System"
    
                    DrawerClickableItem:
                        icon: "home"
                        text: "Home"
                        on_release: app.on_item_select("Home","test2")
                    
                    DrawerClickableItem:
                        icon: "home-plus"
                        text: "Control"
                        on_release: app.on_item_select("Control","test3")
    
                    DrawerClickableItem:
                        icon: "account"
                        text: "Outbox"
                        on_release: app.on_item_select("Outbox","test4")
'''
class StartPage(Screen):
    pass
class LoginPage(Screen):
    pass
class MainPage(Screen):
    pass
class ControlRoom(Screen):
    pass
class ProfilePage(Screen):
    pass
class Content(BoxLayout):
    pass
class Example(MDApp):
    m=0
    n=0
    fl=""
    name=""
    password=""
    button=None
    channel=0
    counter=0
    c=1
    i_x=i_y=0
    dialog = None
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.root = Builder.load_string(KV)
        connection, cursor = self.connect_to_database()
        self.create_table(cursor)
        connection.close()
        Clock.schedule_once(self.switch_to_login, 12)  # Schedule a delay of 3 seconds

    def switch_to_login(self, dt):
        self.root.current = 'test1'
        
    def connect_to_database(self):
        try:
            # Connect to the SQLite database (replace "your_database.db" with your database file)
            connection = sqlite3.connect("App.db")
            
            # Create a cursor object for executing SQL commands
            cursor = connection.cursor()
            
            # Return both the connection and cursor
            return connection, cursor
        except sqlite3.Error as e:
            # Handle any SQLite errors that may occur during connection
            print("SQLite error:", e)
            return None, None
    def create_table(self,cursor):
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS App (
                                name TEXT,
                                password TEXT,
                                confirm_pass TEXT,
                                button_name TEXT,
                                channel INTEGER,                    
                                x INTEGER,
                                y INTEGER,
                                fl TEXT,
                                char TEXT
                            )''')
        except sqlite3.Error as e:
            print("SQLite error:", e)

    def insert_data(self, cursor, name, password, confirm_pass):
        try:
            #self.name=name
            #self.password=password
            cursor.execute("INSERT INTO App (name, password, confirm_pass) VALUES (?, ?, ?)", (name, password, confirm_pass))
            cursor.connection.commit()  # Commit changes to the database
            message=f"Welcome {name} ,Enjoy using it :)"
            self.screen_nev(message,True)
        except sqlite3.Error as e:
            print("SQLite error:", e)
    def insert_button(self, cursor,name,password, button_name, channel,x,y,fl):
        try:
            cursor.execute("INSERT INTO App (name,password,button_name, channel,x,y,fl) VALUES (?, ?, ?,?,?,?,?)", (self.name,self.password,button_name, channel,x,y,fl))
            cursor.connection.commit()  # Commit changes to the database
            message=f"Button {button_name} is added ,Enjoy using it :)"
            self.screen_nev(message,False)
        except sqlite3.Error as e:
            print("SQLite error:", e)
    def select_data(self, cursor, search_name,search_pass):
        try:
            # Execute a SELECT query125
            cursor.execute(f"SELECT name,password,channel FROM App WHERE name = ? AND password = ?", (search_name,search_pass))
    
            # Fetch all rows from the result set
            rows = cursor.fetchall()
    
            # Process the retrieved data
            if rows:
                for row in rows:
                    name,password,channel = row
                message=f"Welcome back {search_name} ,We missed you :)"
                self.screen_nev(message,True)
                self.name=search_name
                self.password=search_pass
                self.channel=channel
                print(name,password,channel)
            else:
                message="No data found ,Please enter right name and password"
                self.screen_nev(message,False)
        except sqlite3.Error as e:
            print("SQLite error:", e)
    def check_exsist(self,cursor, search_name,search_pass):
        try:
            # Execute a SELECT query125
            cursor.execute(f"SELECT name,password FROM App WHERE name = ? AND password = ?", (search_name,search_pass))
    
            # Fetch all rows from the result set
            rows = cursor.fetchall()
    
            # Process the retrieved data
            if rows: 
                return 1
        except sqlite3.Error as e:
            print("SQLite error:", e)
    def select_button(self, cursor, search_name,search_pass):
        try:
            # Execute a SELECT query125
            cursor.execute("SELECT button_name, channel, x, y,fl FROM App WHERE name = ? AND password = ?", (search_name, search_pass))
    
            # Fetch all rows from the result set
            rows = cursor.fetchall()
    
            # Process the retrieved data
            if rows:
                #message=f"Welcome back {search_name} ,We missed you :)"
                for row in rows:
                    button_name, channel, x, y ,self.fl = row
                    if button_name == None:
                        continue
                    else:
                        self.i_y=1-y
                        self.channel=channel
                        self.c+=1
                        self.read_button(button_name, channel, x, y)
            
            else:
                message="No data found ,Please enter right name and password"
        except sqlite3.Error as e:
            print("SQLite error:", e)
    
    def sign_in(self):
        
        text_field1 = self.root.get_screen('test1').ids.text_field1
        text1 = text_field1.text
        text_field1.text=""
        print("Text entered in text_field1:", text1)
        text_field2 = self.root.get_screen('test1').ids.text_field2
        text2 = text_field2.text
        text_field2.text=""
        print("Text entered in text_field1:", text2)
        if text1 == "" or text2 == "" :
            message="Please fill all the fields :)"
            self.screen_nev(message,False)
        else :
            self.name=text1
            self.password = text2
            self.root.get_screen('test2').ids.l_main.text = f"Welcome {self.name}\nWe missed you :)\nEnjoy control everything from here\n^^"
            connection, cursor = self.connect_to_database()
            if connection and cursor:
                self.select_data(cursor,text1,text2)
                connection.close()
            
        
        
        
    def sign_up(self):
        text_field3 = self.root.get_screen('test1').ids.text_field3
        text3 = text_field3.text
        
        print("Text entered in text_field3:", text3)
        text_field4 = self.root.get_screen('test1').ids.text_field4
        text4 = text_field4.text
        text_field4.text=""
        print("Text entered in text_field4:", text4)
        text_field5 = self.root.get_screen('test1').ids.text_field5
        text5 = text_field5.text
        text_field5.text=""
        print("Text entered in text_field5:", text5)
        if text3 == "" or text4 == "" or text5 == "" :
            message="Please fill all the fields :)"
            self.screen_nev(message,False)
        elif text4 != text5:
            message="Please fill all the fields right ,The password field don't match the confirm field :)"
            self.screen_nev(message,False)
        else:
            connection, cursor = self.connect_to_database()
            if connection and cursor:
                s=self.check_exsist(cursor, text3, text4)
            connection.close()
            if s:
                message="Please choose valid name)"
                self.screen_nev(message,False)
            else:
                self.name=text3
                self.password=text4
                self.root.get_screen('test2').ids.l_main.text = f"Welcome {self.name}\nWe missed you :)\nEnjoy control everything from here\n^^"
                connection, cursor = self.connect_to_database()
                if connection and cursor:
                    self.insert_data(cursor, text3, text4, text5)
                    connection.close()
                text_field3.text=""
    def Menu(self):
        #self.root.current = "test1"
        print("hi")
    def message_main(self,message):
        self.dialog = MDDialog(
            text=message,
            elevation=4,
            shadow_softness=15,
            md_bg_color=(0, 0, 0, 1),
            shadow_color="white",
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                ),
            ],
        )
        self.dialog.open()
    def screen_nev(self,message,flag):
        self.dialog = MDDialog(
            text= message,
            elevation=4,
            shadow_softness=15,
            shadow_color="white",
            md_bg_color=(0, 0, 0, 1),
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color="orange",
                    on_release=lambda *args: self.navigate_to_screen("test2",flag)
                ),
            ],
        )
        
        self.dialog.text = message
        self.dialog.open()
    def navigate_to_screen(self, target_screen,flag):
        self.dialog.dismiss()
        if flag == True:
            self.root.current = target_screen
    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()
    
    def channel_info(self):
        if self.fl!="end":
            self.dialog = MDDialog(
                title="Channels:",
                text="Plaese Choose numbers of Channel",
                type="custom",
                elevation=4,
                shadow_softness=15,
                shadow_color="white",
                md_bg_color=(0, 0, 0, 1),
                buttons=[
                    MDFlatButton(
                        text="4 Channel",
                        theme_text_color="Custom",
                        text_color="orange",
                        font_size=14,
                        on_release=lambda *args:self.add_info(4)
                    ),
                    MDFlatButton(
                        text="8 Channel",
                        theme_text_color="Custom",
                        text_color="orange",
                        font_size=14,
                        on_release=lambda *args:self.add_info(8)
                        
                    ),
                    MDFlatButton(
                        text="10 Channel",
                        theme_text_color="Custom",
                        text_color="orange",
                        font_size=14,
                        on_release=lambda *args:self.add_info(10)
                        
                    ),
                ],
            )
            self.dialog.open()
        else:
            if self.c>=self.channel+1:
                message="You have reach your limit"
                self.screen_nev(message,False)
            else:
                self.add_info()
        
    def add_info(self,*args):
        for i in args:
            self.channel=i
        if self.dialog:
            self.dialog.dismiss()
        self.dialog = MDDialog(
            text="Enter the Name of button to be added",
            type="custom",
            content_cls=Content(),
            elevation=4,
            shadow_softness=15,
            shadow_color="white",
            md_bg_color=(0, 0, 0, 1),
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color = "orange",
                    on_release = self.close_dialog
                ),
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color="orange",
                    on_release = lambda *args: self.item_selected(self.dialog.content_cls.ids.add_text1.text,self.channel)
                ),
            ],
        
        )
        self.dialog.open()
        
    def on_item_select(self, item_name, page_name):
        # Close the navigation drawer
        self.root.get_screen('test2').ids.nav_drawer.set_state("close")
        self.root.get_screen('test3').ids.nav_drawer.set_state("close")
        self.root.get_screen('test4').ids.nav_drawer.set_state("close")
        # Now you can perform any actions based on the selected item, if needed
        if item_name == "Home":
            # Handle the "Home" item selection
            self.root.current = page_name
        elif item_name == "Control":
            # Handle the "Control" item selection
            self.root.current = page_name
            connection, cursor = self.connect_to_database()
            if connection and cursor:
                print(self.name,self.password)
                self.select_button(cursor,self.name,self.password)
                connection.close()
        elif item_name == "Outbox":
            self.root.get_screen('test4').ids.l1.text = f"hi {self.name}"
            self.root.get_screen('test4').ids.l2.text = f"Name : {self.name}"
            self.root.get_screen('test4').ids.l3.text = f"Password : {self.password}"
            self.root.get_screen('test4').ids.l4.text = f"Channels : {self.channel}"
            # Handle the "Outbox" item selection
            self.root.current = page_name
        
    def item_selected(self, add_text1,channel):
        self.dialog.dismiss()
        self.add_item(add_text1,channel)
    
    def page_selected(self):
        self.root.current = "test3"
        connection, cursor = self.connect_to_database()
        if connection and cursor:
            print(self.name,self.password)
            self.select_button(cursor,self.name,self.password)
            connection.close()
        
    def read_button(self,button_name,channel,d_x,d_y):
        if channel==4:
            w_y=0.2
        elif channel==8:
            w_y=0.1
        elif channel==10:
            w_y=0.05
        new_card = MDRectangleFlatButton(
            md_bg_color= (0,0,0,0.25),
            font_size=28 ,
            text= button_name,
            text_color="white",
            size_hint= (0.4, w_y),
            ripple_behavior= True,
            line_width=1.5,
            line_color="orange",
            pos_hint= {"center_x": d_x, "center_y": d_y},
            #on_release= lambda *args: self.channel_info()
            )
        rel = RelativeLayout(
            
            )
        button = MDIconButton(
            id="menu_button",
            text_color="white",
            icon= "dots-vertical",
            icon_color="white",
            pos_hint= {"center_x": 1, "center_y": 0.9},
            #on_release= lambda *args: self.menu.open()
            )
        self.button = button
        button.id= f"button_{self.c}"
        #button_id = button.id
        #print(self.i_x,self.i_y,self.c,button_id)
        relative_layout = self.root.get_screen('test3').ids.relative
        new_card.add_widget(rel)
        rel.add_widget(button)
        relative_layout.add_widget(new_card)
    def add_item(self,add_text1,channel):
        if channel==4:
            w_y=0.2
            x=0.25
            y=0.2
            if self.c%2==0:
                self.i_x=x*3
                self.i_y=self.i_y
            elif self.c%2==1 and self.c!=1:
                self.i_x=x
                self.i_y+=0.4
            elif self.c==1:
                self.i_x=x
                self.i_y=y
            self.c+=1
        elif channel==8:
            w_y=0.1
            x=0.25
            y=0.15
            if self.c%2==0:
                self.i_x=x*3
                self.i_y=self.i_y
            elif self.c%2==1 and self.c!=1:
                self.i_x=x
                self.i_y+=0.15
            elif self.c==1:
                self.i_x=x
                self.i_y=y
            self.c+=1
        elif channel==10:
            w_y=0.05
            x=0.25
            y=0.1
            if self.c%2==0:
                self.i_x=x*3
                self.i_y=self.i_y
            elif self.c%2==1 and self.c!=1:
                self.i_x=x
                self.i_y+=0.15
            elif self.c==1:
                self.i_x=x
                self.i_y=y
            self.c+=1
            
        if self.c<=channel+1:
            new_card = MDRectangleFlatButton(
                md_bg_color= (0,0,0,0.25),
                font_size=28 ,
                text= add_text1,
                text_color="white",
                size_hint= (0.4, w_y),
                ripple_behavior= True,
                line_width=1.5,
                line_color="orange",
                pos_hint= {"center_x": self.i_x, "center_y": 1-self.i_y},
                #on_release= lambda *args: self.channel_info()
                )
            rel = RelativeLayout(
                
                )
            button = MDIconButton(
                id="menu_button",
                text_color="white",
                icon= "dots-vertical",
                icon_color="white",
                pos_hint= {"center_x": 1, "center_y": 0.9},
                #on_release= lambda *args: self.menu.open()
                )
            self.fl="end"
            self.button = button
            button.id= f"button_{self.c}"
            button_id = button.id
            print(self.i_x,self.i_y,self.c,button_id)
            relative_layout = self.root.get_screen('test3').ids.relative
            new_card.add_widget(rel)
            rel.add_widget(button)
            relative_layout.add_widget(new_card)
            connection, cursor = self.connect_to_database()
            if connection and cursor:
                self.insert_button(cursor, self.name, self.password, add_text1, channel, self.i_x, 1 - self.i_y,self.fl)
                connection.close()
            
        
Example().run()