import sympy
import random


def pqse_gen(self):
    e = -1

    while e < 0:
        i = sympy.randprime(40000000000000, 90000000000000)
        self.lineEdit_p.setText(str(i))

        i = sympy.randprime(40000000000000, 90000000000000)
        self.lineEdit_q.setText(str(i))

        self.lineEdit_pq.setText(str(int(self.lineEdit_p.text()) * int(self.lineEdit_q.text())))
        self.lineEdit_d.setText(str((int(self.lineEdit_p.text()) - 1) * (int(self.lineEdit_q.text()) - 1)))

        self.open_number_s = sympy.randprime(40000000000000, int(self.lineEdit_d.text()))
        self.lineEdit_s.setText(str(self.open_number_s))

        e = ex_gcd_recursive(int(self.lineEdit_s.text()), int(self.lineEdit_d.text()))[0]

        self.lineEdit_e.setPlaceholderText(str(e))

    self.const_flag = 1


def prepare_encryption(self):
    self.lineEdit_s_A.setText(self.lineEdit_s.text())
    self.lineEdit_pq_A.setText(self.lineEdit_pq.text())
    self.lineEdit_e_B.setPlaceholderText(self.lineEdit_e.placeholderText())
    self.lineEdit_pq_B.setText(self.lineEdit_pq.text())

    self.lineEdit_p.setText("")
    self.lineEdit_q.setText("")
    self.lineEdit_s.setText("")
    self.lineEdit_d.setText("")
    self.lineEdit_e.setPlaceholderText("")
    self.lineEdit_pq.setText("")

    self.const_flag = 0
    self.const_flag_2 = 1


def encryption_decryption(self):
    # Зашифровывание текста открытым ключом
    encoded_ascii_message = ""
    for char in self.textForRSA.toPlainText().encode("unicode-escape"):
        encoded_ascii_message += str(char)

    print("Сообщение в ascii-формате: {0}".format(encoded_ascii_message))

    encoded_message = []

    while len(encoded_ascii_message) > 0:

        if len(encoded_ascii_message) > 20:
            block_size = random.randint(5, 20)
        else:
            block_size = len(encoded_ascii_message)

        temp_str = encoded_ascii_message[0:block_size]
        encoded_ascii_message = encoded_ascii_message[block_size:len(encoded_ascii_message)]

        i = 0
        while len(encoded_ascii_message) - i:
            if encoded_ascii_message[i] != '0':
                break
            else:
                temp_str = temp_str + encoded_ascii_message[i]
                i += 1

        encoded_message.append(pow(int(temp_str), int(self.lineEdit_s_A.text()), int(self.lineEdit_pq_A.text())))

    self.textEdit.setText(str(encoded_message).replace("[", "").replace("]", "").replace(",", "").replace(" ", ""))
    print("Зашифрованное ascii-сообщение(Шифр RSA): {0}; len - {1}".format(encoded_message, len(self.textEdit.toPlainText())))

    # Расшифровывание текста закрытым ключом
    decoded_ascii_message = ""

    for i in range(0, len(encoded_message)):
        decoded_ascii_message += str(pow(encoded_message[i], int(self.lineEdit_e_B.placeholderText()),
                                         int(self.lineEdit_pq_B.text())))

    print("Расшифрованное ascii-сообщение(Шифр RSA): {0}; len - {1}".format(decoded_ascii_message, len(decoded_ascii_message)))

    decoded_message = ascii_to_string(decoded_ascii_message)
    self.textEdit_2.setText(decoded_message)
    print(decoded_message.encode().decode("unicode-escape") + "\n\n")

    self.const_flag = 0


def ex_gcd_recursive(a, b):
    if not b:
        return 1, 0, a
    y, x, g = ex_gcd_recursive(b, a % b)
    return x, y - (a // b) * x, g


def ascii_to_string(ascii_text):
    text = u""

    i = 0
    while i < len(ascii_text):
        if ascii_text[i] == '1':
            chars = ascii_text[i:i+3]
            text += chr(int(chars))
            i += 3
        else:
            chars = ascii_text[i:i+2]
            text += chr(int(chars))
            i += 2

    return text
