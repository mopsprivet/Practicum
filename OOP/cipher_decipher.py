class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift. 
        
        result = [] 
        for letter in original_text.lower(): 
            if letter in self.alphabet: 
                cipher_letter_index = self.alphabet.find(letter.lower())  # здесь ваш код 
                list.append(result, self.alphabet[(cipher_letter_index + shift) % 33]) 
            else:
                result.append(letter)
        return ''.join(result) 
    
    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        for letter in cipher_text.lower(): 
            if letter in self.alphabet.lower(): 
                cipher_letter_index = self.alphabet.find(letter.lower())  # здесь ваш код 
                list.append(result, self.alphabet[(cipher_letter_index - shift) % 33]) 
            else:
                result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Пришло ревью в шифрованном виде. Кажется, нас расскрыли!',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
)) 