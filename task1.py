class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    self.table[key_hash].remove([pair[0],pair[1]])
                    return True
        return False

    def delete_ver2(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            new_pairs = [pair for pair in self.table[key_hash] if pair[0] != key]
            if self.table[key_hash] != new_pairs:
                self.table[key_hash] = new_pairs
                return True
        return False

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)

H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
# H.insert("pineapple", 1)
# H.insert("plum", 2)
# H.insert("peach", 3)
# H.insert("pear", 0)

print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

print(H.delete("apple")) # Виведе: True
print(H.get("apple"))    # Виведе: None
print(H.delete("apple")) # Виведе: False

print(H.delete_ver2("orange")) # Виведе: True
print(H.get("orange"))    # Виведе: None
print(H.delete_ver2("orange")) # Виведе: False
