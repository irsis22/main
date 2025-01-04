from kivy.app import app 
from kivy.uix.widget import widget
from kivy.uix.screenmanager import screen
from kivy.ulx.button import Button
from kivy.ulx.lable import Lable
from kivy.ulx.boxlayout import BoxLayout


class MyApp(App):
 def build(self):
    txt = Lable (text ='Choose to die')
    btn = Button(text='Dont click')
    btn.on_press = tst

    layout = BoxLayout()
    layout.add_widget(txt)
    layout.add_widget(box)
    return layout
  
object_name = widget_name(parameters)
    widget creation code
  
def build()
   return widget
  widget1.add_widget(widget2)


  box = Boxlayout(orientatio = 'vertical' padding = 8, spacing = 8)
  hl = BoxLayout()
  txt = Lable (text = 'Choose a sceen')

  hl.add_widget(txt)
  hl.add_widget(box)

Class MyScreen(screen):
  def __init__ (`self,**Kwargs)
    super.__init__(**Kwargs)


class MyApp(App):
  sm = ScreenManager()
  
  sm.add_widget(screen1(name = 'scr1'))
  sm.add_widget(screen2(name = 'scr2'))
    sm.add_widget(screen3(name = 'scr3'))
  sm.add_Widget(MainScr(name = 'main'))
  return sm
 
 selfmanager.current = screen_name

Class scrButton(Button):
  def __init__(self, screen, direction = 'right', goal = main)
    super().__init__()
    self.screen = screen
    self.direction = direction
    self.goal
  def on_press(self):
    self.screen.manager.transition = self.direction
    self.screen.manager.current = self.goal

ScrButton(self, directions = 'right', goal ='main', textb ='Back')
size_hint = (6,2), pos_hint = {'right': 1}
btn = Buttontext (text = 'here!', size_hint=(5,5))
post_hint = {swich_widget_part>:<where_on_screen_located}



Class MainScr (screen):
  def __init__(self, name = 'main')
    super(.__init__(name = name))



MyApp().run()
app = MyApp()
app.run()
Lable(text = 'Lable on the screen', color = (1, 0.6, 0.2, 1))