# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import os
import getpass
import MrHolmes as holmes
from Core.Support import Font
from Core.Support import Banner_Selector as banner
from configparser import ConfigParser
from Core.Support import Clear
from Core.Support import Language

dest = "Configuration"
nomefile = "Configuration.ini"
filename = "../" + Language.Translation.Get_Language()
filename


class Config:

    @staticmethod
    def Banner():
        Clear.Screen.Clear()
        Folder = "Banners/Configuration"
        banner.Random.Get_Banner(Folder)

    @staticmethod
    def modify_recipient():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Email","Choice") + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                recipient = str(input(
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Email","Modify") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while recipient == "":
                    recipient = str(input(
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Email","Modify") + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if recipient == "None":
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Email","NotChanged"))
                    os.chdir("../")
                else:
                    Parser.set("Smtp", "email", recipient)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print(Language.Translation.Translate_Language(filename,"Configuration","Email","Changed"))
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def modify_password():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Password","Choice") + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                passw = getpass.getpass(Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Password","Modify") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                while passw == "":
                    passw = getpass.getpass(
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Password","Modify") + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                if passw == "None":
                    out = input(
                        Language.Translation.Translate_Language(filename,"Configuration","Password","NotChanged"))
                    os.chdir("../")
                else:
                    Parser.set("Smtp", "password", passw)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print(Language.Translation.Translate_Language(filename,"Configuration","Password","Changed"))
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def modify_destination():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Email","Choice2") + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                destination = str(input(
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Email","Modify2") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while destination == "":
                    destination = str(input(
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Email","Modify2") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if destination == "None":
                    out = input(
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Email","NotChanged2") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                    os.chdir("../")
                else:
                    Parser.set("Smtp", "destination", destination)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print(Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Email","Modify2") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                    out = input( Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def modify_port():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE +  Language.Translation.Translate_Language(filename,"Configuration","Smtp","Choice2") + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                port = str(input(
                    Font.Color.WHITE +  Language.Translation.Translate_Language(filename,"Configuration","Smtp","Modify2") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while port == "":
                    port = str(input(
                        Font.Color.WHITE +  Language.Translation.Translate_Language(filename,"Configuration","Smtp","Modify2") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if port == "None":
                    out = input(
                         Language.Translation.Translate_Language(filename,"Configuration","Smtp","NotChanged2"))
                    os.chdir("../")
                else:
                    Parser.set("Smtp", "port", port)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print( Language.Translation.Translate_Language(filename,"Configuration","Smtp","Changed2"))
                    out = input( Language.Translation.Translate_Language(filename,"Configuration","Modify","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE +  Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def modify_server():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE +  Language.Translation.Translate_Language(filename,"Configuration","Email","Choice") + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                server = str(input(
                    Font.Color.WHITE +  Language.Translation.Translate_Language(filename,"Configuration","Email","Modify") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while server == "":
                    server = str(input(
                        Font.Color.WHITE +  Language.Translation.Translate_Language(filename,"Configuration","Email","Modify") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if server == "None":
                    out = input(
                         Language.Translation.Translate_Language(filename,"Configuration","Email","NotChanged"))
                    os.chdir("../")
                else:
                    Parser.set("Smtp", "server", server)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print( Language.Translation.Translate_Language(filename,"Configuration","Email","Changed"))
                    out = input( Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def modify_path():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE +  Language.Translation.Translate_Language(filename,"Configuration","Update-Path","Choice") + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile:
                Parser = ConfigParser()
                Parser.read(nomefile)
                path = str(input(
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Update-Path","Modify")  + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while path == "":
                    path = str(input(
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Update-Path","Modify") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if path == "None":
                    out = input(
                        "")
                    os.chdir("../")
                else:
                    Parser.set("Settings", "path", path)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print(Language.Translation.Translate_Language(filename,"Configuration","Update-Path","NotChanged"))
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def modify_update_pass():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Password","Choice2")  + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile:
                Parser = ConfigParser()
                Parser.read(nomefile)
                passw = getpass.getpass(
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Password","Modify2")  + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                while passw == "":
                    passw = str(input(
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Password","Modify2")  + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if passw == "None":
                    out = input(
                        "\n")
                    os.chdir("../")
                else:
                    Parser.set("Settings", "password", passw)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                        print("\n")
                        out = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                        os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def modify_key():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Api","Choice")  + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                key = str(input(
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Api","Modify")  + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while key == "":
                    key = str(input(
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Api","Modify")  + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if key == "None":
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Api","NotChanged"))
                    os.chdir("../")
                else:
                    Parser.set("Settings", "api_key", key)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print(Language.Translation.Translate_Language(filename,"Configuration","Api","Changed"))
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def modify_proxy():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Proxy","Choice")  + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                proxy_path = str(input(
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Proxy","Modify")  + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while proxy_path == "":
                    proxy_path = str(input(
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Proxy","Modify") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if proxy_path == "None":
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Proxy","NotChanged"))
                    os.chdir("../")
                else:
                    Parser.set("Settings", "proxy_list", proxy_path)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print(Language.Translation.Translate_Language(filename,"Configuration","Proxy","Changed"))
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def modify_Log():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Logs","Choice")  + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                Logs = int(input(
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Logs","Modify") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if Logs == 1:
                    Logs = "True"
                elif Logs == 2:
                    Logs = "False"
                else:
                    os.chdir("../")
                    Config.main()
                Parser.set("Settings", "show_logs", Logs)
                with open(nomefile, 'w') as configfile:
                    Parser.write(configfile)
                    print(Language.Translation.Translate_Language(filename,"Configuration","Logs","Changed"))
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")
    
    @staticmethod
    def modify_Database_Visibility():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Database","Choice")  + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                Data = int(input(
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Database","Modify")  + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if Data == 1:
                    Data = "True"
                elif Data == 2:
                    Data = "False"
                else:
                    os.chdir("../")
                    Config.main()
                Parser.set("Settings", "database", Data)
                with open(nomefile, 'w') as configfile:
                    Parser.write(configfile)
                    print(Language.Translation.Translate_Language(filename,"Configuration","Database","Changed"))
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")
    
    @staticmethod
    def modify_Language():
        os.chdir(dest)
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Lang","Choice")  + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                Lang = str(input(
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Lang","Modify")  + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while Lang == "":
                    Lang = str(input(
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Lang","Modify") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if Lang == "None":
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Lang","NotChanged"))
                    os.chdir("../")
                else:
                    Parser.set("Settings", "language", Lang)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print(Language.Translation.Translate_Language(filename,"Configuration","Lang","Changed"))
                    out = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                    os.chdir("../")
            else:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Configuration","Main","Error"))
                os.chdir("../")
        else:
            os.chdir("../")

    @staticmethod
    def main():
        while True:
            Config.Banner()
            filename = Language.Translation.Get_Language()
            filename
            option = Language.Translation.Translate_Language(filename,"Configuration","Main","Options")
            options = str(option)
            print(Font.Color.GREEN + Language.Translation.Translate_Language(filename,"Configuration","Main","Text"))
            print(Font.Color.WHITE + options)
            sce = int(input(Font.Color.GREEN +
                      "\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if sce == 1:
                Config.modify_recipient()
            elif sce == 2:
                Config.modify_destination()
            elif sce == 3:
                Config.modify_password()
            elif sce == 4:
                Config.modify_server()
            elif sce == 5:
                Config.modify_port()
            elif sce == 6:
                Config.modify_update_pass()
            elif sce == 7:
                Config.modify_path()
            elif sce == 8:
                Config.modify_key()
            elif sce == 9:
                Config.modify_proxy()
            elif sce == 10:
                Config.modify_Log()
            elif sce == 11:
                Config.modify_Database_Visibility()
            elif sce == 12:
                Config.modify_Language()
            elif sce == 13:
                inp = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
                holmes.Main.Menu()
            else:
                Config.main()
