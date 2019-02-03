import pyperclip
import detect_english
import transposition_cipher


def main():
    # file = open('test.txt')
    # secret_message = file.read()
    # file.close()
    secret_message = """CsaR b98b7sn
maihnrminroahcfoaorsdao tBerd thshluhel rpe.sioehsopnL cen,rytge ecufa'gp  leiehhuhcffeidd ga  w.  ,Seup r g nrdenh gSDe1 e1 gmanlev ecg rtee gbm.i tfcea e iieta tanytels  smda nl oSeu  f i
re ocrbsilBtese e ree idni Becwho yl c mltiBede ingaBe er Or)alat,oreacaiwie
parlp dah orbidwnn  ncett o eiPo p na atnc m1aefodenwntob nauor vi cy stn ecta'hoarNeatiM ehna edtfcira,(c -c  niti s,nnhlnhgdct aeuCe etm"bsiivgfmior
ul cxgafulmirdyhdiM.9 cuningasemaoani
aaan1e,sshie
ahbsiuvkiatheuctetbhs hfenlb 2e1 t1w shcpo tda eoi o pm tor"rhp,a tte iecm eaemo nr neesei eoeu 9ptnifcistd grlsltncb 9n u esnitab nleenreensoe ebaifee
eebF6m71o8aEheihpio nee ntnormcenef eu
gcehntrcaptvldomdsthctcm
si nnsI1elcnfen r Bei .tochlttttco hgnetamed desr
cemdpradgo re."""
    hacked_message = hack_transposition_cipher(secret_message)
    if not hacked_message:
        print('Hacking failed.')
    else:
        print(hacked_message)
        pyperclip.copy(hacked_message)


def hack_transposition_cipher(message):
    for key in range(1, len(message)):
        decrypted_message = transposition_cipher.decrypt_message(message, key)
        if detect_english.is_english(decrypted_message, word_percentage=70):
            return decrypted_message, str(key)
    return '', ''


if __name__ == '__main__':
    main()
