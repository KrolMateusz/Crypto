import string
import sys
import time

import matplotlib.pyplot as plt
from kivy.app import App
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager

sys.path.insert(0, 'c:/Users/Mateusz/PythonProjects/Aplikacja_szyfrowanie/Alghoritms')
import affine_cipher
import affine_hacker
import cesar_cipher
import cesar_hacker
import frequency_analysis
import simple_substition_cipher
import simple_substition_hacker
import transposition_cipher
import transposition_hacker
import vigenere_cipher
import vigenere_hacker


class ScreenManagement(ScreenManager):
    pass


class EncryptionScreen(Screen):
    user_message_text_input = ObjectProperty()
    user_key_text_input = ObjectProperty()
    hidden_message_text = ObjectProperty()
    user_cipher_text = ObjectProperty()

    def clear_message(self):
        self.user_message_text_input.text = ''
    
    def clear_key(self):
        self.user_key_text_input.text = ''

    def hide_message(self, message, key):
        start_time = time.time()
        if self.user_cipher_text.text == 'Szyfr afiniczny':
            if affine_cipher.check_keys(*affine_cipher.get_key_parts(int(key.text)), 'encrypt'):
                self.hidden_message_text.text = affine_cipher.encrypt_message(message.text, int(key.text))
            else:
                key.text = str(affine_cipher.get_random_key())
                self.hidden_message_text.text = affine_cipher.encrypt_message(message.text, int(key.text))
        if self.user_cipher_text.text == 'Szyfr Cezara':
            self.hidden_message_text.text = cesar_cipher.encrypt_message(message.text, int(key.text))
        if self.user_cipher_text.text == 'Szyfr podstawieniowy':
            if not simple_substition_cipher.check_key(key.text):
                key.text = simple_substition_cipher.get_random_key()
            self.hidden_message_text.text = simple_substition_cipher.encrypt_message(message.text, key.text)
        if self.user_cipher_text.text == 'Szyfr kolumnowy':
            self.hidden_message_text.text = transposition_cipher.encrypt_message(message.text, int(key.text))
        if self.user_cipher_text.text == 'Szyfr Vigenere':
            self.hidden_message_text.text = vigenere_cipher.encrypt_message(message.text, key.text)
        print(self.hidden_message_text.text)
        print(len(self.hidden_message_text.text))
        print(round(time.time() - start_time, 2))


class DecryptionScreen(Screen):
    user_message_text_input = ObjectProperty()
    ser_key_text_input = ObjectProperty()
    hidden_message_text = ObjectProperty()
    user_cipher_text = ObjectProperty()

    def clear_message(self):
        self.user_message_text_input.text = ''
    
    def clear_key(self):
        self.user_key_text_input.text = ''

    def hide_message(self, message, key):
        if self.user_cipher_text.text == 'Szyfr afiniczny':
            if affine_cipher.check_keys(*affine_cipher.get_key_parts(int(key.text)), 'encrypt'):
                self.hidden_message_text.text = affine_cipher.decrypt_message(message.text, int(key.text))
            else:
                key.text = str(affine_cipher.get_random_key())
                self.hidden_message_text.text = affine_cipher.decrypt_message(message.text, int(key.text))
        if self.user_cipher_text.text == 'Szyfr Cezara':
            self.hidden_message_text.text = cesar_cipher.decrypt_message(message.text, int(key.text))
        if self.user_cipher_text.text == 'Szyfr podstawieniowy':
            if not simple_substition_cipher.check_key(key.text):
                key.text = simple_substition_cipher.get_random_key()
            self.hidden_message_text.text = simple_substition_cipher.decrypt_message(message.text, key.text)
        if self.user_cipher_text.text == 'Szyfr kolumnowy':
            self.hidden_message_text.text = transposition_cipher.decrypt_message(message.text, int(key.text))
        if self.user_cipher_text.text == 'Szyfr Vigenere':
            self.hidden_message_text.text = vigenere_cipher.decrypt_message(message.text, key.text)
        print(self.hidden_message_text.text)


class CryptanalysisScreen(Screen):
    user_ciphertext_text = ObjectProperty()
    user_encryption_method = ObjectProperty()
    translated_message_text = ObjectProperty()
    translated_message_key = ObjectProperty()

    def clear_message(self):
        self.user_ciphertext_text.text = ''

    def break_cipher(self, message):
        if self.user_encryption_method.text == 'Szyfr afiniczny':
            self.translated_message_text.text, self.translated_message_key.text = affine_hacker.hack_affine(message.text)
        if self.user_encryption_method.text == 'Szyfr Cezara':
            self.translated_message_text.text, self.translated_message_key.text = cesar_hacker.hack_cipher(message.text)
        if self.user_encryption_method.text == 'Szyfr podstawieniowy':
            self.translated_message_text.text, self.translated_message_key.text = simple_substition_hacker.decrypt_with_cipher_letter_mappings(message.text, simple_substition_hacker.hack_cipher(message.text))
        if self.user_encryption_method.text == 'Szyfr kolumnowy':
            self.translated_message_text.text, self.translated_message_key.text = transposition_hacker.hack_transposition_cipher(message.text)
        if self.user_encryption_method.text == 'Szyfr Vigenere':
            self.translated_message_text.text, self.translated_message_key.text = vigenere_hacker.hack_vigenere(message.text)
        print(self.translated_message_text.text)


class BarScreen(Screen):
    bar = ObjectProperty(None)
    user_message_graph = ObjectProperty()
    
    def generate_graph(self, message):
        letters = list(string.ascii_uppercase)
        english_frequency = frequency_analysis.ENGLISH_LETTER_FREQUENCY_SORTED.values()
        message_frequency = frequency_analysis.get_percentage_frequency(message.text).values()

        plt.clf()
        plt.subplot(2, 1, 1)
        plt.title('Frequency graph')
        plt.ylabel('Liczebnosc [%]')
        plt.bar(letters, english_frequency, label='Jezyk angielski', color='blue')
        plt.legend()
        plt.subplot(2, 1, 2)
        plt.ylabel('Liczebnosc [%]')
        plt.bar(letters, message_frequency, label='Wiadomosc', color='red')
        plt.legend()

        self.bar.clear_widgets()
        self.bar.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class HelpScreen(Screen):
    text = ObjectProperty()

    def on_pre_enter(self, *args):
        with open('C:\\Users\\Mateusz\\PythonProjects\\Aplikacja_szyfrowanie\\Kivy\\help.txt') as file:
            message = file.read()
        self.text.text = message


class InputApp(App):

    def build(self):
        return Builder.load_file('main.kv')

if __name__ == "__main__":
    InputApp().run()
