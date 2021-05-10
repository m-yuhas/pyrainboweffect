# pyrainboweffect
## Introduction
Prenez une image comme ceci:

![téléchargement en cours...](../images/demo0_in.png)

Et la transformez:

![téléchargement en cours...](../images/demo0_out.gif)

## Lancement Rapide
* Installez le paquet:

```
pip install pyrainboweffect
```

### Python IPA
Dans une console Python, importez le paquet:

```python
>>> import pyrainboweffect
```

Appliquez l'effet à une fichier d'image et enregistrez le résultat comme GIF:

```python
>>> pyrainboweffect.psychedelic_gif('input.png', 'output.gif')
```

Appliquez l'effet à une fichier d'image et enregistrez le résultat comme mp4:

```python
>>> pyrainboweffect.psychedelic_mp4('input.png', 'output.gif')
```

### ILC
Pour utiliser l'interface en ligne de commande:

```bash
$ python -m pyrainboweffect input.png output.gif
```

## Documentation de l'IPA
Pour la documentation complète, [cliquez ici](api_documentation.md).
Actuellement la documentation est seulement disponible en anglais.

## Théorie d'Operation
Il semble que cet effet peut être généré avec les etapes suivantes:
1. Convertir l'image en niveaux de gris.
2. Partitionner l'espace d'intensité en le même nombre de partitions comme
  couleurs dans la schéma de couleur.
3. Mettre les régions d'intensité à leurs couleurs correspondantes.
4. Majorer l'intensité des tous les pixels dans l'image originale (recommencer
  à 0 si se produit le dépassement).
5. Revenir à l'étape 2 et répéter jusqu'à ce qu'il y a cadres suffisantes pour
  faire une animation.

## Dépendances
Ce paquet seulement supporte Python version 3.5 et plus.  Ce paquet devrait
pouvoir être exécuté dans toute système POSIX aussi bien que Windows 7 et plus.

Les suivants paquets Pypi sont requis:
* moviepy
* numpy
* opencv-python

## Comment Contribuer
Suggestions et «pull requests» sont bienvenus.  Si trouvez un bug et vous
n'avez pas le temps à le régler vous-même, s'il vous plaît ouvrez un problème.

## Tâches Futures
- Appliquer l'effet psychédélique à une image animée ou vidéo.
