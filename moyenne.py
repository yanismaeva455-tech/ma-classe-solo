"""Fonction Calcul de la moyenne pondérée d'un élève."""
import csv


def moyenne_ponderee(notes):
    """Retourne la moyenne sur 20, arrondie à 2 décimales.

    notes : liste de tuples (note, coefficient).
    """
    if not notes:
        raise ValueError("La liste de notes est vide")
    total = sum(note * coef for note, coef in notes)
    somme_coefs = sum(coef for _, coef in notes)
    return round(total / len(notes), 2)


def lire_notes(chemin):
    """Lit un fichier CSV (matiere,note,coefficient) et retourne la liste des tuples."""
    with open(chemin, newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)
        return [(float(l["note"]), float(l["coefficient"])) for l in lecteur]


if __name__ == "__main__":
    notes = lire_notes("donnees/notes.csv")
    """"print("Moyenne :", moyenne_ponderee(notes))"""
    print("Afficher la mention")
