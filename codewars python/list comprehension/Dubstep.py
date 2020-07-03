def song_decoder(song):
    song = song.split("WUB")
    lst = [el for el in song if el !=""]
    return " ".join(lst).strip()