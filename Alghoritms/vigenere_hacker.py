import detect_english
import frequency_analysis
import itertools
import pyperclip
import re
import vigenere_cipher
import string

LETTERS = string.ascii_uppercase
SILENT_MODE = True
NUM_MOST_FREQ_LETTERS = 3
MAX_KEY_LEN = 12
NON_LETTER_PATTERNS = re.compile('[^A-Z]')


def main():
    ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf,
kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce
vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm 
ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. 
Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr 
vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce 
Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a 
ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab 
mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf 
lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq 
pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw 
Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl 
Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a 
kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e 
Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts 
yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn 
eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at 
hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce 
Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. 
Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz 
vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev 
bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw 
ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id 
tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc 
wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa 
mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, 
Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv 
nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." 
Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva 
ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""
    hacked_message = hack_vigenere(ciphertext)
    if hacked_message:
        print('Copying hacked message to clipboard')
        pyperclip.copy(hacked_message)
        print(hacked_message)
    else:
        print('Hacking failed.')


def find_repeat_sequences_spacings(message):
    message = NON_LETTER_PATTERNS.sub('', message.upper())
    seq_spacings = {}
    for seq_len in range(2, 3):
        for seq_start in range(len(message) - seq_len):
            seq = message[seq_start: seq_start + seq_len]
            for i in range(seq_start + seq_len, len(message) - seq_len):
                if message[i: i + seq_len] == seq:
                    if seq not in seq_spacings:
                        seq_spacings[seq] = []
                    seq_spacings[seq].append(i - seq_start)
    return seq_spacings


def get_useful_factors(number):
    if number < 2:
        return []
    factors = []
    for i in range(2, MAX_KEY_LEN + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(int(number / i))
    if 1 in factors:
        factors.remove(1)
    return list(set(factors))


def get_item_at_index_one(x):
    return x[1]


def get_most_common_factors(seq_factors):
    factor_counts = {}
    for seq in seq_factors:
        factor_list = seq_factors[seq]
        for factor in factor_list:
            if factor not in factor_counts:
                factor_counts[factor] = 0
            else:
                factor_counts[factor] += 1
    factors_by_count = []
    for factor in factor_counts:
        if factor <= MAX_KEY_LEN:
            factors_by_count.append((factor, factor_counts[factor]))
    factors_by_count.sort(key=get_item_at_index_one, reverse=True)
    return factors_by_count


def kasiski_examination(ciphertext):
    repeated_seq_spacings = find_repeat_sequences_spacings(ciphertext)
    seq_factors = {}
    for seq in repeated_seq_spacings:
        seq_factors[seq] = []
        for spacing in repeated_seq_spacings[seq]:
            seq_factors[seq].extend(get_useful_factors(spacing))
    factors_by_count = get_most_common_factors(seq_factors)
    all_likely_key_lengths = []
    for two_int_tuple in factors_by_count:
        all_likely_key_lengths.append(two_int_tuple[0])
    return all_likely_key_lengths


def get_nth_subkeys_letters(n, key_len, message):
    message = NON_LETTER_PATTERNS.sub('', message.upper())
    i = n - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += key_len
    return ''.join(letters)


def attempt_hack_with_key_length(ciphertext, most_likely_key_length):
    ciphertext_up = ciphertext.upper()
    all_freq_scores = []
    for nth in range(1, most_likely_key_length + 1):
        nth_letters = get_nth_subkeys_letters(nth, most_likely_key_length,
                                              ciphertext_up)
        freq_scores = []
        for possible_key in LETTERS:
            decrypted_text = vigenere_cipher.decrypt_message(nth_letters,
                                                             possible_key)
            key_and_freq_match_tuple = (possible_key, frequency_analysis.
                                        english_frequency_match_score
                                        (decrypted_text))
            freq_scores.append(key_and_freq_match_tuple)
        freq_scores.sort(key=get_item_at_index_one, reverse=True)
        all_freq_scores.append(freq_scores[:NUM_MOST_FREQ_LETTERS])
    if not SILENT_MODE:
        for i in range(len(all_freq_scores)):
            print('Possible letters for letter %s of the key: '
                  % (i + 1), end='')
            for freq_score in all_freq_scores[i]:
                print(freq_score[0], end=' ')
            print()
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS),
                                     repeat=most_likely_key_length):
        possible_key = ''
        for i in range(most_likely_key_length):
            possible_key += all_freq_scores[i][indexes[i]][0]
        if not SILENT_MODE:
            print('Attempting with key: %s' % possible_key)
        decrypted_text = vigenere_cipher.decrypt_message(ciphertext_up,
                                                         possible_key)
        if detect_english.is_english(decrypted_text):
            orig_case = []
            for i in range(len(ciphertext)):
                if ciphertext[i].isupper():
                    orig_case.append(decrypted_text[i].upper())
                else:
                    orig_case.append(decrypted_text[i].lower())
            decrypted_text = ''.join(orig_case)
            # print('Possible decryption with key %s:' % possible_key)
            # print(decrypted_text[:200])
            # print('\nEnter d for done or press ENTER to continue hacking.')
            # key_pressed = input('> ')
            # if key_pressed.lower().strip().startswith('d'):
            return decrypted_text, possible_key
    return None, None


def hack_vigenere(ciphertext):
    all_likely_key_lengths = kasiski_examination(ciphertext)
    if not SILENT_MODE:
        key_length_str = ''
        for key_len in all_likely_key_lengths:
            key_length_str += '%s ' % key_len
        print('Kasiski Examination results say the most likely key '
              'lengths are: ' + key_length_str + '\n')
    for key_len in all_likely_key_lengths:
        if not SILENT_MODE:
            print('Attempting hack with key length %s (%s possible keys)...'
                  % (key_len, NUM_MOST_FREQ_LETTERS ** key_len))
        hacked_message, key = attempt_hack_with_key_length(ciphertext, key_len)
        if hacked_message:
            break
    if hacked_message is None:
        if not SILENT_MODE:
            print('Unable to hack message with likely key length(s). '
                  'Brute forcing key length...')
        for key_len in range(1, MAX_KEY_LEN + 1):
            if key_len not in all_likely_key_lengths:
                if not SILENT_MODE:
                    print('Attempting hack with key length %s '
                          '(%s possible keys)...'
                          % (key_len, NUM_MOST_FREQ_LETTERS ** key_len))
                hacked_message, key = attempt_hack_with_key_length(ciphertext,
                                                                  key_len)
                if hacked_message is not None:
                    break
    return hacked_message, str(key)


if __name__ == '__main__':
    main()
