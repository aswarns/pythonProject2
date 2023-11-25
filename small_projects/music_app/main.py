from music import playlist
from ascii_art import logo


def print_playlist():
    for b_index,  band in enumerate(playlist, 1):
        name, songs = band
        for song_num, song in songs:
            print(f" {b_index}: {song_num} {name} -  {song}")


def print_somg(p_bnumber, p_snumber):
    band_name = playlist[p_bnumber-1][0]
    song_name = playlist[band_number-1][1][p_snumber-1][1]
    print(f"\n{band_name} -  {song_name} playing now...")


print(logo)

while True:
    print_playlist()
    current_play = input("\nSelect a song to play using number:(1:1) ")
    band_number = int(current_play[0])
    song_number = int(current_play[2])
    print_somg(band_number, song_number)
    change = input("\nPress C to change the song or any key key to quit APP: ")
    if change == "C" or change == "c":
        continue
    break
print("Goodby! ")
