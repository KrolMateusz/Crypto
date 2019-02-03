import affine_cipher
import pyperclip
import detect_english
import cryptomath


def main():
    cipher = ("\"S IAKVWBYL MAWPD DYGYLRY BA NY ISPPYD EFBYPPEOYFB ET EB IAWPD"
        " DYIYERY S JWKSF EFBA NYPEYREFO BJSB EB MSG JWKSF.\" -SPSF BWLEFO")
    hacked_message = hack_affine(cipher)
    if hacked_message:
        print(hacked_message)
        pyperclip.copy(hacked_message)
    else:
        print('Hacking failed.')


def hack_affine(message):
    message = message.upper()
    for key in range(len(affine_cipher.SYMBOLS) ** 2):
        key_a = affine_cipher.get_key_parts(key)[0]
        if cryptomath.gcd(key_a, len(affine_cipher.SYMBOLS)) != 1:
            continue
        decrypted_text = affine_cipher.decrypt_message(message, key)
        if detect_english.is_english(decrypted_text):
            return decrypted_text, str(key)
    return '', ''


if __name__ == '__main__':
    main()
