# How to Add More Languages 

This document explains the process of adding new languages . Currently, the project uses a JSON language file to store text translations. Here’s how you can easily add more languages.

## Project Structure

The project file structure includes a directory named `assets/lang`, where language files in JSON format are stored. Each file should follow a specific schema containing the necessary translations for each component of the application.

## Steps to Add a New Language

1. **Create a New JSON File**:
   - Inside the `assets/lang` directory, create a new JSON file. Name the file with the language code (for example, `fr.json` for French or `en.json` for English).

2. **Define the Translations**:
   - Copy the contents of an existing language file (like `es.json`) and paste it into the new file.
   - Translate all text strings into your new language. Ensure that you maintain the same structure as the original file.

   ### Example File for French (`fr.json`):
   ```json
   {
       "name": "Français",
       "createPsw": {
           "title": "Créer un Mot de Passe",
           "saveAs": "Sélectionnez un dossier pour enregistrer le mot de passe",
           "passwordsDoNotMatch": "Les mots de passe ne correspondent pas",
           "passwordCannotBeEmpty": "Le mot de passe ne peut pas être vide",
           "passwordSavedSuccessfully": "Mot de passe enregistré avec succès",
           "save": "Enregistrer"
       },
       "Login": {
           "psw": "Entrez votre mot de passe",
           "submit": "Se Connecter",
           "pswList": {
               "columns": ["Source", "Utilisateur/Email", "Mot de Passe", "caché"],
               "add": "Ajouter",
               "reload": "Recharger",
               "passwordMng": {
                   "back": "Retour",
                   "copy": "Copier",
                   "delete": "Supprimer",
                   "passwordCannotBeEmpty": "Le mot de passe ne peut pas être vide",
                   "verifyTitle": "Écrivez le mot de passe de l'utilisateur",
                   "cancel": "Annuler",
                   "submit": "Accepter"
               }
           }
       }
   }
