import pyttsx3
import datetime
import speech_recognition as sr


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


def commande():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Donner une commande.")
        r.pause_threshold = 1 #1 seconde
        audio = r.listen(source)
        try:
            print("En cours...")
            req = r.recognize_google(audio, language="fr-FR")
            print(req)
        except Exception as e:
            print(e)
            parler(f"Il n'y a {e} pas dans la commande.")
            return "None"
        return req


commande()
#salutation()