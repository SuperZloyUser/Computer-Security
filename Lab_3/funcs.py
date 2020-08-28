class encoder:
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    conformity_key_index = {0: 'Длина ключа больше "7" !', 1: 0.058, 2: 0.046, 3: 0.04,
                            4: 0.0375, 5: 0.036, 6: 0.0352, 7: 0.0345}

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def trigrams_dict(self):
        return self._trigrams_dict

    @property
    def distance_dict(self):
        return self._distance_dict

    @property
    def key_length(self):
        return self._key_length

    @key_length.setter
    def key_length(self, value):
        self._key_length = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def source_text(self):
        return self._source_text

    @source_text.setter
    def source_text(self, value):
        self._source_text = value

    @property
    def text_index(self):
        return self._text_index

    @text_index.setter
    def text_index(self, value):
        self._text_index = value

    def __init__(self):
        self._key = ''
        self._text = ''
        self._text_index = 0
        self._trigrams_dict = {}
        self._distance_dict = {}
        self._key_length = -1
        self._most_counted_letter = []
        self._source_text = ''
        pass

    def text_translator(self, input_text):
        result = []

        self.source_text = input_text

        for i in input_text:
            if i in self.alphabet:
                result.append(i)
        return ''.join(result)

    def main_func(self):

        self.find_double_and_more_trigrams()

        self.drop_excess_trigrams()

        self.gen_distance_dict()

        self.key_length = self.calculate_key_length()

        self.text_index = self.calculate_index(self.letters_count(), self.text)

        self.reset()

        return

    def text_encoder(self):

        encoded_text = ''

        for i in range(0, len(self.text)):
            encoded_text += chr((ord(self.text[i]) - ord(self.key[i % self.key_length])) % 32 + ord('А'))

        return self.return_punctuation(encoded_text)

    def return_punctuation(self, text_to_update):

        result = ''
        text_counter = 0

        for i in range(0, len(self.source_text)):
            if self.source_text[i] in self.alphabet:
                result += text_to_update[text_counter]
                text_counter += 1
            else:
                result += self.source_text[i]

        return result

    def reset(self):
        self._trigrams_dict = {}
        self._distance_dict = {}

    def encode_key(self, support_str):

        letters_counter = []
        for i in range(0, self.key_length):
            letters_counter.append({})

        for i in range(0, len(self.text)):
            if self.text[i] not in letters_counter[i % self.key_length]:
                letters_counter[i % self.key_length][self.text[i]] = 0
            letters_counter[i % self.key_length][self.text[i]] += 1

        temp_key = ''
        self.key = ''

        for i in range(0, self.key_length):
            temp_key += list(filter(lambda x: letters_counter[i][x[0]] == max(letters_counter[i].values()), letters_counter[i].items()))[0][0]

        for i in range(0, self.key_length):
            self.key += chr(abs(ord(temp_key[i]) - ord(support_str[i])) % 32 + ord('А'))

    def calculate_key_length(self):

        keys_dict = {}

        for i in self.distance_dict:
            for j in range(0, len(self.distance_dict[i]) - 1):
                self.distance_dict[i][j + 1] = self.gcd(self.distance_dict[i][j], self.distance_dict[i][j + 1])
            temp_key = min(self.distance_dict[i])
            if temp_key not in keys_dict:
                keys_dict[temp_key] = 0
            keys_dict[min(self.distance_dict[i])] += 1

        for i in list(keys_dict):
            if i < 3:
                keys_dict.pop(i)

        return list(filter(lambda x: keys_dict[x[0]] == max(keys_dict.values()), keys_dict.items()))[0][0]

    def gen_distance_dict(self):
        for i in self.trigrams_dict:
            for j in range(0, len(self.trigrams_dict[i]) - 1):
                if i not in self.distance_dict:
                    self.distance_dict[i] = []
                self.distance_dict[i].append(self.trigrams_dict[i][j + 1] - self.trigrams_dict[i][j])

    def find_double_and_more_trigrams(self):
        for i in range(0, len(self.text) - 2):
            if self.text[i + 2] not in self.alphabet or self.text[i + 1] not in self.alphabet or \
                    self.text[i] not in self.alphabet:
                continue
            pos = self.text.find(self.text[i:i + 3], i + 1)
            while pos != -1:
                if self.text[i:i + 3] not in self.trigrams_dict:
                    self.trigrams_dict[self.text[i:i + 3]] = []
                if i not in self.trigrams_dict[self.text[i:i + 3]]:
                    self.trigrams_dict[self.text[i:i + 3]].append(i)
                if pos not in self.trigrams_dict[self.text[i:i + 3]]:
                    self.trigrams_dict[self.text[i:i + 3]].append(pos)

                pos = self.text.find(self.text[i:i + 3], pos + 1)

    def drop_excess_trigrams(self):
        for i in list(self.trigrams_dict):
            if len(self.trigrams_dict[i]) < 3:
                self.trigrams_dict.pop(i)

    def letters_count(self):
        letters = {}
        for i in self.alphabet:
            for j in self.text:
                if i == j:
                    if i not in letters:
                        letters[i] = 1
                        continue
                    letters[i] += 1
        return letters

    @staticmethod
    def calculate_index(dict_with_letters: dict, text: str):
        letters_sum = 0
        for i in dict_with_letters:
            letters_sum += dict_with_letters[i] * (dict_with_letters[i] - 1)
        return letters_sum / (len(text) * (len(text) - 1))

    @staticmethod
    def gcd(a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a
