import os
import subprocess
import anthropic
import requests

# Fonction pour récupérer les différences des commits
def obtenir_diff_commit():
    try:
        resultat = subprocess.run(['git', 'diff', 'HEAD~1', 'HEAD', '--unified=0'], capture_output=True, text=True, check=True)
        return resultat.stdout
    except subprocess.CalledProcessError as e:
        return f"Une erreur s'est produite lors de l'exécution de git diff: {e.stderr}"

# Fonction pour analyser les différences avec l'IA
def analyser_diff_code(diff):
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("La clé API Anthropics n'est pas définie dans les variables d'environnement.")
    
    reponse = anthropic.Anthropic(api_key=api_key).completions.create(
        max_tokens_to_sample=1000,
        model="claude-3-haiku-20240307",
        prompt=f"\n\nHuman: Analysez la différence de code suivante et fournissez des commentaires de révision, détectez les bugs et suggérez des améliorations:\n{diff}\n\nAssistant:"
    )
    return reponse['choices'][0]['text'].strip() if 'choices' in reponse and reponse['choices'] else "Pas de réponse de l'API."

# Fonction pour poster un commentaire sur une pull request
def poster_commentaire_revue(repo, numero_pr, commentaire):
    url = f"https://api.github.com/repos/{repo}/issues/{numero_pr}/comments"
    headers = {'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'}
    if not headers['Authorization']:
        raise ValueError("Le token GitHub n'est pas défini dans les variables d'environnement.")
    
    donnees = {'body': commentaire}
    reponse = requests.post(url, headers=headers, json=donnees)
    return reponse.status_code

def main():
    diff_commit = obtenir_diff_commit()
    if "Une erreur s'est produite" in diff_commit:
        print(diff_commit)
        return
    
    commentaires_revue = analyser_diff_code(diff_commit)
    print(f"Commentaires de révision:\n{commentaires_revue}")
    
    # Exemple d'utilisation de poster_commentaire_revue (décommentez et modifiez avec le repo et le numéro de PR réels)
    # code_statut = poster_commentaire_revue('votre-repo', 1, commentaires_revue)
    # print(f"Commentaire posté avec le code de statut: {code_statut}")

if __name__ == "__main__":
    main()