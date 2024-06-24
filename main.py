import json
import discord
from discord.ext import commands
import colorama
from colorama import Fore, Style
import os
import asyncio

banner = """
   _____ _      ______          _   _ ______ _____  
  / ____| |    |  ____|   /\   | \ | |  ____|  __ \ 
 | |    | |    | |__     /  \  |  \| | |__  | |  | |
 | |    | |    |  __|   / /\ \ | . ` |  __| | |  | |
 | |____| |____| |____ / ____ \| |\  | |____| |__| |
  \_____|______|______/_/    \_\_| \_|______|_____/ 
"""

def add_owner(owner_id):
    os.system('cls')
    with open('owners.txt', 'a') as f:
        f.write(f"\n{owner_id}")
    print(f'L\'owner "{owner_id}" à été ajouté dans la liste des owners.')

def remove_owner(owner_id):
    os.system('cls')
    owners = []
    with open('owners.txt', 'r') as f:
        owners = [line.strip() for line in f.readlines()]
    if owner_id in owners:
        owners.remove(owner_id)
        with open('owners.txt', 'w') as f:
            for owner in owners:
                f.write(f"{owner}\n")
    print("L'owner à été supprimer de la liste des owners.")

def list_owners():
    os.system('cls')
    owners = []
    with open('owners.txt', 'r') as f:
        owners = [line.strip() for line in f.readlines()]
    for owner in owners:
        print(f"Owner ID : {owner}")

def register_bot():
    bot_id = input("Identifiant du bot : ")
    bot_name = input("Donner un nom au bot : ")
    bot_token = input("Token du bot : ")

    bots = {}
    if os.path.exists('bots.json'):
        with open('bots.json', 'r') as f:
            bots = json.load(f)

    if bot_name not in bots:
        bots[bot_name] = {"id": bot_id, "token": bot_token}
        with open('bots.json', 'w') as f:
            json.dump(bots, f, indent=4)
        print("Bot enregistré")
    else:
        print("Bot déjà enregistré")

def delete_bot():
    os.system('cls')
    bot_name = input("Nom du bot à supprimer : ")
    bots = json.loads(open('bots.json', 'r').read())
    if bot_name in bots:
        del bots[bot_name]
        with open('bots.json', 'w') as f:
            json.dump(bots, f)
        print("Bot supprimé")
    else:
        print("Bot non trouvé")

def list_bots():
    os.system('cls')
    bots = json.loads(open('bots.json', 'r').read())
    print(f"Il y a {len(bots)} bots dans la liste")
    for bot_name, bot_data in bots.items():
        print(f"Nom : {Fore.RED}{bot_name}{Fore.LIGHTCYAN_EX}, Token : {Fore.RED}{bot_data['token'][:5]}{Fore.LIGHTCYAN_EX}..., ID du bot : {Fore.RED}{bot_data['id']}{Fore.LIGHTCYAN_EX}")

def connect_bot():
    os.system('cls')
    bot_name = input("Nom du bot à connecter: ")
    bots = json.loads(open('bots.json', 'r').read())
    if bot_name in bots:
        bot_token = bots[bot_name]["token"]
        bot_id = bots[bot_name]["id"]
        print(f"\nVous êtes connecté au bot {bot_name}!")
        print(f"\nVoici le lien OAuth2 pour inviter le bot : https://discord.com/oauth2/authorize?client_id={bot_id}&permissions=8&scope=bot")
        print(f"\n{Fore.RED}+purge{Fore.LIGHTCYAN_EX} <nombres> <noms> (Supprime tout les salons et en créer un certain nombres avec un nom spécifié.)\n{Fore.RED}+clean{Fore.LIGHTCYAN_EX} (Supprime tout les salons)\n{Fore.RED}+spam{Fore.LIGHTCYAN_EX} <nombre> <message> (Spam un message un certain nombre de fois dans tout les salons du serveur.)\n{Fore.RED}+dmall{Fore.LIGHTCYAN_EX} <message> (Envois un message à tout les utilisateurs présent dans le serveur.)\n")
        print(Fore.LIGHTCYAN_EX)
        with open('sourcecode.py', 'r') as f:
            source_code = f.read()
        with open('bot.py', 'w') as f:
            f.write(source_code)
        with open('bot.py', 'r') as f:
            code = f.read()
        code = code.replace("TOKEN_HERE", bot_token)
        with open('bot.py', 'w') as f:
            f.write(code)
        exec(open('bot.py').read())
    else:
        print("Bot non trouvé")

def command_list():
    os.system('cls')
    print(f"\n{Fore.RED}+purge{Fore.LIGHTCYAN_EX} <nombres> <noms> (Supprime tout les salons et en créer un certain nombres avec un nom spécifié.)\n{Fore.RED}+clean{Fore.LIGHTCYAN_EX} (Supprime tout les salons)\n{Fore.RED}+spam{Fore.LIGHTCYAN_EX} <nombre> <message> (Spam un message un certain nombre de fois dans tout les salons du serveur.)\n{Fore.RED}+dmall{Fore.LIGHTCYAN_EX} <message> (Envois un message à tout les utilisateurs présent dans le serveur.)\n")

def display_menu():
    print(Fore.RED + f"{banner}\n")
    print(Fore.LIGHTCYAN_EX +"Menu principal :\n")
    print(f"{Fore.RED}1.{Fore.LIGHTCYAN_EX} Enregistrer un nouveau bot\t\t{Fore.RED}4.{Fore.LIGHTCYAN_EX} Ajouter un owner à un bot\t\t{Fore.RED}7.{Fore.LIGHTCYAN_EX} Lister les bots")
    print(f"{Fore.RED}2.{Fore.LIGHTCYAN_EX} Supprimer un bot existant\t\t{Fore.RED}5.{Fore.LIGHTCYAN_EX} Supprimer un owner d'un bot\t\t{Fore.RED}8.{Fore.LIGHTCYAN_EX} Afficher les commandes")
    print(f"{Fore.RED}3.{Fore.LIGHTCYAN_EX} Se connecter à un bot existant\t{Fore.RED}6.{Fore.LIGHTCYAN_EX} Lister les owners d'un bot\n")

def main():
    os.system('cls')
    display_menu()
    while True:
        option = input(f"Choisissez une option ({Fore.RED}home{Fore.LIGHTCYAN_EX} pour retourner au menu): ")
        if option == "1":
            register_bot()
        elif option == "2":
            delete_bot()
        elif option == "3":
            connect_bot()
        elif option == "4":
            owner_id = input("Identifiant de l'owner que vous souhaitez ajouter:")
            add_owner(owner_id)
        elif option == "5":
            owner_id = input("Identifiant de l'owner que vous souhaitez supprimer:")
            remove_owner(owner_id)
        elif option == "6":
            list_owners()
        elif option == "7":
            list_bots()
        elif option == "home":
            os.system('cls')
            display_menu()
        elif option == "8":
            command_list()

if __name__ == "__main__":
    main()