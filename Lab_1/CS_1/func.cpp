#include "ssc.h"

void SSC::Encryption(){

    QString str;
    QString key;
    QString newKey;
    QString newStr;

    // Получение исходного текста и ключа из формы
    str = SSC::getTextFromLine1();
    key = SSC::getTextFromLine2();

    int flag = 0;

    // Создание первой части матрицы шифрования из ключа
    for (int i = 0; i < key.length(); i++)
    {

        flag = 0;

        for (int j = 0; j < newKey.length(); j++)
            if (newKey[j] == key[i]) flag++;

        if (flag == 0)
            newKey = newKey + key[i];

    }


    int pos = 0;
    int shift = SSC::getShiftFromRB();

    // Создание второй части матрицы шифрования из букв, которые не вошли в ключ
    for (int i = 0; i < alfabet.length() - 1; i++)
        if (newKey.indexOf(alfabet[i], 0, Qt::CaseInsensitive) == -1) newKey = newKey + alfabet[i];


    // Шифрование исходного текста
    for (int i = 0; i < str.length(); i++){

        if (str[i] == ' ') {
            newStr += str[i];
            continue;
        }

        pos = newKey.indexOf(str[i], 0, Qt::CaseInsensitive) + shift * SHIFT_FOR_STR;

        if (pos > 25 && pos < 30) pos += SHIFT_FOR_STR;
        if (pos >= 30) pos %= 30;

        newStr = newStr + newKey[pos];

    }

    QString out;

    // Подготовка матрицы шифрования(пеобразование из строки в таблицу)
    for (int i = 0; i < newKey.length(); i++){

        if (i % SHIFT_FOR_STR == 0 && i != 0) out = out + "\n";
        out = out + newKey[i] + "    ";

    }

    out = out + "*    *    *    *";

    // Вывод зашифрованного текста и матрицы
    SSC::setTextToTB2(out);
    SSC::setTextToTB1(newStr);

}
