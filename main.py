from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.clock import Clock
import time
from kivy.config import Config


Config.set('kivy', 'window_icon', 'icon.ico')
Config.set('graphics', 'resizable', True)


class ReadDefiningApp(App):
	def build(self):
		self.title = 'Read-Defining'
		return


class WindowManager(ScreenManager):
	TEXT_GLOBAL = StringProperty('')
	SPEED_GLOBAL = NumericProperty(10)
	WORD_GLOBAL = StringProperty('')
	START_GLOBAL = StringProperty('')
	lst = ListProperty([])
	x = 0
	timesPressed = 0

	def __init__(self, **kwargs):
		super(WindowManager, self).__init__(**kwargs)
		self.event = None

	def word_by_word(self):
		self.cancel()
		self.timesPressed = 0
		self.x = 0
		t = 60/int(self.SPEED_GLOBAL)
		self.lst = self.TEXT_GLOBAL.split()
		self.WORD_GLOBAL = self.lst[0]
		self.event = Clock.schedule_interval(self.update, t)
		self.event()

	def cont(self):
		Clock.unschedule(self.event)
		t = 60/int(self.SPEED_GLOBAL)
		self.event = Clock.schedule_interval(self.update, t)
		self.event()

	def update(self):
		try:
			self.WORD_GLOBAL = self.lst[self.x]
			self.x += 1
		except IndexError:
			self.START_GLOBAL = "Start Again?"
			self.WORD_GLOBAL = ""

	def cancel(self):
		Clock.unschedule(self.event)


class EntryLayout(Screen):
	def submit(self):
		pass


class ResultLayout(Screen):
	pass


def word_by_word():
	text = input("Enter the text you want to read.")
	s = int(input("How fast do you want to read the text (wpm)?"))
	t = 60/s
	lst = text.split()
	for i in lst:
		if i != "":
			print(i)
			time.sleep(t)
		else:
			continue


if __name__ == '__main__':
	ReadDefiningApp().run()
