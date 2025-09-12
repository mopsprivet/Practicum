import random

class MarsURLEncoder:

    def __init__(self): 
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.links_storage = {} 

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        while True:
            hash_part = ""  
            for i in range(6):  
                random_char = random.choice(self.chars)
                hash_part += random_char

            if hash_part not in self.links_storage:
                break  

        self.links_storage[hash_part] = long_url

        short_url = "https://ma.rs/" + hash_part
        return short_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""

        hash_part = short_url.split("/")[-1]

        if hash_part in self.links_storage:
            return self.links_storage[hash_part]
        else:
            return None