import os
from kivy.loader import Loader

from kivymd import images_path
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from login_class.login import Login
from register_class.register import Register
from main_navigation.mainNavigation import mainNavigation


class MainWid(ScreenManager):
    def __init__(self, **kwargs):
        super(MainWid, self).__init__()
        self.Login = Login(self)
        self.Register = Register(self)
        self.mainNavigation = mainNavigation()

        wid = Screen(name='loginScreen')
        wid.add_widget(self.Login)
        self.add_widget(wid)

        wid = Screen(name='RegisterScreen')
        wid.add_widget(self.Register)
        self.add_widget(wid)

        wid = Screen(name='mainNavigationScreen')
        wid.add_widget(self.mainNavigation)
        self.add_widget(wid)

        self.goto_login()

    def goto_login(self):
        self.current = 'loginScreen'

    def goto_register(self):
        self.current = 'RegisterScreen'

    def goto_mainNavigation(self, **kwargs):
        self.current = 'mainNavigationScreen'
        self.mainNavigation.create_list_tks(**kwargs)
        #self.mainNavigation.load_drawer()


class MainApp(MDApp):
    def build(self):
        Loader.loading_image = f"{images_path}transparent.png"
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/register_class/register.kv")
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/login_class/login.kv")
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/kivy_file/mainNavigation.kv")
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/kivy_file/messageFrame.kv")
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/kivy_file/cardSubscription.kv")
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/contact_class/screen_contact.kv")



        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        self.theme_cls.theme_style = "Light"  # "Light"
        self.theme_cls.primary_hue = "700"  # "500"
        return MainWid()

    def on_start(self):
        #self.fps_monitor_start()
        return True

    def on_stop(self):
        return True

    def on_pause(self):
        return True

    def on_resume(self):
        return True


if __name__ == "__main__":
    MainApp().run()
