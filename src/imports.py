import discord                      # główna biblioteka odpowiedziala za obsługę bota
from discord.ext import commands    # rozszerzenie głównej biblioteki wprowadzające obsługę komend

import configHandler as fH          # moduł ładujący pliki konfiguracyjne z dysku
import loadWords as lW              # moduł ładujący "zakazane" słowa
import serverData as sD             # moduł obsługujący zarządzanie danymi o użytkownikach serwerów

from datetime import datetime       # pobieranie daty do do zapisu logów wiadomości
import os                           # sprawdzanie czy instnieja sciezki
import typing                       # okreslanie typow w funkcjach, przykład w main.py - 92 linia