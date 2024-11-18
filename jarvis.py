import pyttsx3
import datetime


def parler(audio):
    ass_virtuel = pyttsx3.init()
    ass_virtuel.say(audio)
    ass_virtuel.runAndWait()


def heure():
    h = datetime.datetime.now().strftime("%H:%M")
    parler(f"Il est {h}")


def dateDuJour():
    liste_mois_annee = [
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"
    ]
    annee = datetime.datetime.now().year
    mois = datetime.datetime.now().month
    mois_en_lettres = liste_mois_annee[mois -1]
    jour = datetime.datetime.now().day
    parler(f"Aujourd'hui, nous sommes le {jour} {mois_en_lettres} {annee}")


def salutation():
    h = datetime.datetime.now().hour
    if h >= 18 or h <= 1:
        parler("Bonsoir")
    else:
        parler("Bonjour")
    dateDuJour()
    heure()
    parler("Je suis à votre service. Comment puis-je vous aider ?")


salutation()