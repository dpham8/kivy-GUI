# Author: Dat Pham
# Date Modifed: 10/17/21
#
import kivy
from kivy.app import App
kivy.require('1.9.1')
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup
# text-to-speech
from gtts import gTTS 
import time
import vlc
import os
# speech-to-text
import speech_recognition as sr
#pdf
import PyPDF2
import pyttsx3

from kivy.core.window import Window
#Window.size = (700, 500)

#windows
class WindowManager(ScreenManager):
	pass
	
class Menu(Screen):
	pass

from speech_test import *
#from kivy.logger import Logger

class Option1(Screen):
	speech_output = ObjectProperty(None)

	def spinner_clicked(self, value):
		self.ids.module.text = f'Selected library: {value}'
		
		#if value == 'Healthcare':
			#print("yesssssssss")
			
	def start(self):
		
		r = sr.Recognizer()
		with sr.Microphone() as source:
			#r.adjust_for_ambient_noise(source, duration=0.1)
			print('Speak: ')
			audio = r.listen(source)
			try:
				text = r.recognize_google(audio)
				print('you said: {}'.format(text))
				self.speech_output.text = text
			except:
				print('Sorry could not recognize your voice')
		
	def stop(self):
		print("hi")
					#translate(0)
		
class Option1ADHD(Screen):
	pass

class Option1CS(Screen):
	pass
	
class Option1HC(Screen):
	pass
	
class Option1F(Screen):
	pass

class Option2(Screen):
	def spinner_clicked(self, value):
		pass
	pass
	
class Option2ADHD(Screen):
	pass

class Option2CS(Screen):
	pass
	
class Option2HC(Screen):
	pass
	
class Option2F(Screen):
	pass

class LoadDialog(FloatLayout):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)

class Option3(Screen):
	loadfile = ObjectProperty(None)
	#savefile = ObjectProperty(None)
	text_input = ObjectProperty(None)
	#file = ""
	
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Load file", content=content, size_hint=(0.5, 0.8))
		self._popup.open()

	def load(self, path, filename):
		#file = filename[0]
		#if filename[0].endswith('.txt'):
		#	print("hii")
			#print(file)
		
		if filename[0].endswith('.txt'):
			with open(os.path.join(path, filename[0])) as stream:	
				myText = stream.read().replace("\n", " ")
				self.text_input.text = myText
				self.dismiss_popup() #change 
			
				language = 'en'
			
				output = gTTS(text=myText, lang=language, slow=False)
				output.save("output.mp3")
			
				instance = vlc.Instance()
				speech = instance.media_player_new()
				media = instance.media_new('output.mp3')
				speech.set_media(media)
				speech.play()
			
		if filename[0].endswith('.pdf'):
			path = open(filename[0], 'rb')
			pdfReader = PyPDF2.PdfFileReader(path)
			
			#start read at page
			from_page = pdfReader.getPage(7)
			text = from_page.extractText()
			self.text_input.text = text
			self.dismiss_popup()
			
			speak = pyttsx3.init()
			speak.say(text)
			speak.runAndWait()

class Option4(Screen):
	pass

class Option5(Screen):
	pass

class Option6(Screen):
	pass
		
kv = Builder.load_file('pages.kv')

class TranslatorApp(App):
	def build(self):
		return kv

Factory.register('Option3', cls=Option3)
Factory.register('LoadDialog', cls=LoadDialog)
#Factory.register('SaveDialog', cls=SaveDialog

if __name__ == '__main__':
	TranslatorApp().run()

