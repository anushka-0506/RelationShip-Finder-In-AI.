import pyglet
from pyglet import window
import window1

window = pyglet.window.Window(1300, 450, "This project is copyrighted to Mr. S.venkat .", resizable=True, style=window.Window.WINDOW_STYLE_DIALOG)
window.set_minimum_size(400,300)
icon = pyglet.image.load('delete1.png')
window.set_icon(icon)
label = pyglet.text.Label("FAMILY RELATIONSHIP FINDER.",
                          font_name='Times New Roman',color=(0, 0, 0, 255),
                          font_size=25,bold=True,
                          x=window.width/1.8 , y = window.height/1.1)
labe = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">It is a basic assumsion based software The size of the family is assumed </font>',
                x=window.width//1.8, y=window.height//1.3 )  
lab1 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">to be costant with two parents A &B .They have three children C(Boy), </font>',
                x=window.width//1.8, y=window.height//1.4 )    
lab = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">D(Boy) and E(girl): </font>',
                x=window.width//1.8, y=window.height//1.5 ) 
lab8 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">Now the following notations are made: - </font>',
                x=window.width//1.8, y=window.height//1.8 )                  
lab2 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">1).      F is the wife of G, G is the wife of D and H is the husband of E </font>',
                x=window.width//1.8, y=window.height//2 ) 
lab3 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">2).         C and F have children I and J . I is a boy and J is a girl </font>',
                x=window.width//1.8, y=window.height//2.2 ) 
lab4 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">3).       D and G have children K and L . K is a girl and L is a girl </font>',
                x=window.width//1.8, y=window.height//2.4 ) 
lab5 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">4).    E and H have children M and N . M is a boy and N is a boy </font>',
                x=window.width//1.8, y=window.height//2.7 )   
lab6 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">These are the over all assumptions that are made. Changes can be easily </font>',
                x=window.width//1.8, y=window.height//3.5 )  
lab7 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">made using the<b> "UPDATE"</b> and <b>"DELETE"</b> buttons .  </font>',
                x=window.width//1.8, y=window.height//4 ) 

lab9 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">After reading all the Assumtions and Notations Please close the window by </font>',
                x=window.width//1.8, y=window.height//9 ) 
labe9 = pyglet.text.HTMLLabel(
        '<font face="Times New Roman" size="4">clicking on the<b> "X" </b> button located on the Top most right.</font>',
                x=window.width//1.8, y=window.height//14 )                                                                   
animation = pyglet.image.load_animation('ooj.gif')
animSprite = pyglet.sprite.Sprite(animation)                          
r,g,b,alpha = 0.5,0.5,0.8,0.5

 
 
pyglet.gl.glClearColor(r,g,b,alpha)
 
@window.event
def on_draw():
    window.clear()
    label.draw()
    labe.draw()
    lab1.draw()
    lab.draw()
    lab2.draw()
    lab3.draw()
    lab4.draw()
    lab5.draw()
    lab6.draw()
    lab7.draw()
    lab8.draw()
    lab9.draw()
    labe9.draw()
    animSprite.draw()
 
from playsound import playsound 
playsound('voice2.mp3') 
pyglet.app.run()
