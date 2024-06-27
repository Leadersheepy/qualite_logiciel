import os
import subprocess
import anthropic
import requests

# import dotenv
# dotenv.load_dotenv()

# Fonction pour récupérer les différences des commits
def obtenir_diff_commit():
    try:
        resultat = subprocess.run(['git', 'diff', 'HEAD~1', 'HEAD', '--unified=0', 'test_script.py'], capture_output=True, text=True, check=True)
        return resultat.stdout
    except subprocess.CalledProcessError as e:
        return f"Une erreur s'est produite lors de l'exécution de git diff: {e.stderr}"

# Fonction pour analyser les différences avec l'IA
def analyser_diff_code(diff):
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("La clé API Anthropics n'est pas définie dans les variables d'environnement.")

    messages = [
        {"role": "user", "content": f"You are a helpful assistant. Analysez la différence de code suivante et fournissez des commentaires de révision, détectez les bugs et suggérez des améliorations:\n{diff}"}
    ]

    # Make the API call with the messages
    response = anthropic.Anthropic(api_key=api_key).messages.create(
        model="claude-3-haiku-20240307",
        messages=messages,
        max_tokens=1024
    )

    return response.content[0].text.strip()

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
    
    # Récupération du nom du dépôt et du numéro de la pull request à partir des variables d'environnement
    repo = os.getenv('GITHUB_REPOSITORY')
    pull_request = os.getenv('GITHUB_REF_NAME').replace("/merge", "")

    # Utilisation de poster_commentaire_revue
    code_statut = poster_commentaire_revue(repo, pull_request, commentaires_revue)
    print(f"Commentaire posté avec le code de statut: {code_statut}")

if __name__ == "__main__":
    main()