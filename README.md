# Spotify Checker and Closer Tool

## Description
Ce script Python est un outil simple qui vérifie si Spotify est installé sur l'ordinateur. S'il est installé, l'outil ferme Spotify s'il est en cours d'exécution et affiche une boîte de dialogue indiquant "Réussi". Si Spotify n'est pas installé, une boîte de dialogue informe l'utilisateur.

## Fonctionnalités
- **Détection de Spotify** : Vérifie si Spotify est installé en recherchant son dossier d'installation par défaut.
- **Fermeture de Spotify** : Si Spotify est en cours d'exécution, il est automatiquement fermé.
- **Messages visuels** : Toutes les informations (réussi, échec ou non installé) sont affichées dans des boîtes de dialogue Windows, sans utiliser le terminal (CMD).

## Prérequis
- **Système d'exploitation** : Windows
- **Python** : Version 3.x installée sur le PC
- **Modules nécessaires** : Aucun module externe n'est requis. Les modules utilisés (`os`, `ctypes`) sont intégrés à Python.

## Utilisation
1. Téléchargez ou copiez le script Python sur votre ordinateur.
2. Exécutez le script en double-cliquant dessus ou via un éditeur Python (comme IDLE).
3. Une boîte de dialogue s'affichera pour vous informer :
   - Si Spotify est installé et a été fermé avec succès : `Réussi`
   - Si Spotify n'est pas installé : `Spotify n'est pas installé sur ce PC.`
   - Si une erreur s'est produite lors de la fermeture : `Échec de la fermeture de Spotify`

## Exemple de résultat
- **Spotify installé et en cours d'exécution** :  
  ![Image](https://via.placeholder.com/200x100?text=Spotify+fermé+avec+succès)

- **Spotify non installé** :  
  ![Image](https://via.placeholder.com/200x100?text=Spotify+non+installé)

## Limitations
- Ce script ne détecte que l'installation par défaut de Spotify (dans `%AppData%\Spotify`).
- Si Spotify est installé ailleurs, il ne sera pas détecté.

## Auteur
- Script développé pour un projet de démonstration Python.
