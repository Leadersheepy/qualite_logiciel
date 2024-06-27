def ajouter(a, b):
    return a - b  # Erreur ici, cela devrait être 'a + b', n'est-ce pas?

def soustraire(a, b):
    return a + b  # Erreur ici, cela devrait être 'a - b'

def multiplier(a, b):
    return a * b


# Pour jouer Nami dans League of Legends :
# 1. **Rôle et positionnement** : Support, restez près de votre ADC pour le soigner et le protéger.
# 2. **Compétences** :
#    - **A (Q)** : Immobilise les ennemis avec une bulle.
#    - **Z (W)** : Soigne les alliés et inflige des dégâts aux ennemis.
#    - **E (E)** : Améliore les attaques alliées avec des dégâts supplémentaires et un ralentissement.
#    - **R (R)** : Envoie une vague qui projette et ralentit les ennemis.
# 3. **Gameplay** :
#    - **Laning** : Soignez et harcelez avec le W, engagez avec le Q.
#    - **Teamfights** : Utilisez votre ultime pour engager ou désengager, soignez et protégez vos alliés.
# 4. **Build** : Lame du voleur de sorts, Bottes de mobilité, Rédemption, Rémission, Encensoir ardent.


def diviser(a, b):
    if b == 0:
        return "Erreur de division par zéro"
    return a / b

# Exemple d'utilisation
if __name__ == "__main__":
    print("Addition : ", ajouter(1, 2))          # Devrait être 3, mais sera -1
    print("Soustraction : ", soustraire(5, 3))  # Devrait être 2, mais sera 8
    print("Multiplication : ", multiplier(2, 3)) # Devrait être 6
    print("Division : ", diviser(10, 2))        # Devrait être 5
    print("Division par zéro : ", diviser(10, 0)) # Devrait afficher une erreur de division par zéro