def add(a, b):
    return a - b  # Erreur ici, cela devrait être 'a + b'

def subtract(a, b):
    return a + b  # Erreur ici, cela devrait être 'a - b'

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero error"
    return a / b

# Exemple d'utilisation
if __name__ == "__main__":
    print("Addition: ", add(1, 2))          # Devrait être 3, mais sera -1
    print("Subtraction: ", subtract(5, 3))  # Devrait être 2, mais sera 8
    print("Multiplication: ", multiply(2, 3)) # Devrait être 6
    print("Division: ", divide(10, 2))        # Devrait être 5
    print("Division by zero: ", divide(10, 0)) # Devrait afficher une erreur de division par zéro
