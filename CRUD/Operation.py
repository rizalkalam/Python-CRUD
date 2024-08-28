from . import Database
from .Util import random_string
import time
import os

def create_first_data():
    artist = input("Artist: ")
    album = input("Album: ")
    song = input("Song: ")

    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["created_at"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["artist"] = artist + Database.TEMPLATE["artist"][len(artist):]
    data["album"] = album + Database.TEMPLATE["album"][len(album):]
    data["song"] = song + Database.TEMPLATE["song"][len(song):]

    data_str = f'{data["pk"]}, {data["created_at"]}, {data["artist"]}, {data["album"]}, {data["song"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Failed")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            song_count = len(content)
            if "index" in kwargs:
                song_index = kwargs["index"]-1
                if song_index < 0 or song_index > song_count:
                    return False
                else:
                    return content[song_index]
            else:
                return content
    except:
        print("database read error")
        return False
    
def create(song, artist, album):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["created_at"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["artist"] = artist + Database.TEMPLATE["artist"][len(artist):]
    data["album"] = album + Database.TEMPLATE["album"][len(album):]
    data["song"] = song + Database.TEMPLATE["song"][len(song):]

    data_str = f'{data["pk"]}, {data["created_at"]}, {data["artist"]}, {data["album"]}, {data["song"]}\n'
    
    try:
        with open(Database.DB_NAME, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data failed")

def update(song_number, pk, created_at, artist, album, song):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = pk
    data["created_at"] = created_at
    data["artist"] = artist + Database.TEMPLATE["artist"][len(artist):]
    data["album"] = album + Database.TEMPLATE["album"][len(album):]
    data["song"] = song + Database.TEMPLATE["song"][len(song):]

    data_str = f'{data["pk"]}, {data["created_at"]}, {data["artist"]}, {data["album"]}, {data["song"]}\n'

    data_length = len(data_str)

    try:
        with(open(Database.DB_NAME, 'r+', encoding="utf-8")) as file:
            file.seek(data_length*(song_number-1))
            file.write(data_str)
    except:
        print("error update data")

def delete(song_number):
    try:
        with open(Database.DB_NAME, 'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == song_number - 1:
                    pass
                else:
                    with open("data_temp.txt", 'a', encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")
    
    os.replace("data_temp.txt",Database.DB_NAME)