from elements import Button, Input, Text, Picture
from page import Page

btn = Button('button')
inpt = Input('input')
txt = Text('ноября')
pic = Picture('img')

btn.exist(Page.url())
inpt.exist(Page.url())
txt.exist(Page.url())
pic.exist(Page.url())
