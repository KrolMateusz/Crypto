from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.properties import ObjectProperty
import sys

sys.path.insert(0, 'c:/Users/Mateusz/PythonProjects/Aplikacja_szyfrowanie/Alghoritms')
import cesar_cipher
import transposition_cipher
import simple_substition_cipher
import vigenere_cipher
import affine_cipher
import rsa_cipher

class ScreenManagement(ScreenManager):
    pass

class EncryptionScreen(Screen):
    pass

class DecryptionScreen(Screen):
    pass

class InputDB(BoxLayout):
    user_message_text_input = ObjectProperty()
    ser_key_text_input = ObjectProperty()
    hidden_message_text = ObjectProperty()
    user_cipher_text = ObjectProperty()

    def hide_message(self, message, key):
        if self.user_cipher_text.text == 'Affine cipher':
            if affine_cipher.check_keys(*affine_cipher.get_key_parts(int(key.text)), 'encrypt'):
                self.hidden_message_text.text = affine_cipher.encrypt_message(message.text, int(key.text))
            else:
                key.text = str(affine_cipher.get_random_key())
                self.hidden_message_text.text = affine_cipher.encrypt_message(message.text, int(key.text))
        if self.user_cipher_text.text == 'Cesar cipher':
            self.hidden_message_text.text = cesar_cipher.encrypt_message(message.text, int(key.text))
        if self.user_cipher_text.text == 'Substition cipher':
            if not simple_substition_cipher.check_key(key.text):
                key.text = simple_substition_cipher.get_random_key()
            self.hidden_message_text.text = simple_substition_cipher.encrypt_message(message.text, key.text)
        if self.user_cipher_text.text == 'Transposition cipher':
            self.hidden_message_text.text = transposition_cipher.encrypt_message(message.text, int(key.text))
        if self.user_cipher_text.text == 'Vigenere cipher':
            self.hidden_message_text.text = vigenere_cipher.encrypt_message(message.text, key.text)
        print(self.hidden_message_text.text)


class InputApp(App):

    def build(self):
        return Builder.load_file('input.kv')

if __name__ == "__main__":
    InputApp().run()
