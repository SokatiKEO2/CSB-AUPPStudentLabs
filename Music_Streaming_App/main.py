import musicstreamingapp as msa

song1 = msa.Song("Blinding Lights", "The Weeknd", "After Hours", "Pop", "3:20")
song2 = msa.Song("Save Your Tears", "The Weeknd", "After Hours", "Pop", "3:35")
song3 = msa.Song("Can't Feel My Face", "The Weeknd", "Beauty Behind the Madness", "R&B", "3:34")
song4 = msa.Song("Starboy", "The Weeknd", "Starboy", "R&B", "3:50")
song5 = msa.Song("The Hills", "The Weeknd", "Beauty Behind the Madness", "R&B", "4:02")
song6 = msa.Song("In the Night", "The Weeknd", "Beauty Behind the Madness", "R&B", "3:55")
song7 = msa.Song("Heartless", "The Weeknd", "After Hours", "Pop", "3:18")
song8 = msa.Song("I Feel It Coming", "The Weeknd", "Starboy", "R&B", "4:29")
song9 = msa.Song("Pray for Me", "The Weeknd", "Black Panther: The Album", "Hip-Hop", "3:31")
song10 = msa.Song("Earned It", "The Weeknd", "Fifty Shades of Grey (Original Motion Picture Soundtrack)", "R&B", "4:12")
song11 = msa.Song("Positions", "Ariana Grande", "Positions", "Pop", "2:52")
song12 = msa.Song("Thank U, Next", "Ariana Grande", "Thank U, Next", "Pop", "3:27")
song13 = msa.Song("No Tears Left to Cry", "Ariana Grande", "Sweetener", "Pop", "3:25")
song14 = msa.Song("7 Rings", "Ariana Grande", "Thank U, Next", "Pop", "2:58")
song15 = msa.Song("Into You", "Ariana Grande", "Dangerous Woman", "Pop", "4:04")
song16 = msa.Song("Love Story", "Taylor Swift", "Fearless", "Country", "3:54")
song17 = msa.Song("Blank Space", "Taylor Swift", "1989", "Pop", "3:51")
song18 = msa.Song("Shake It Off", "Taylor Swift", "1989", "Pop", "3:39")
song19 = msa.Song("You Belong with Me", "Taylor Swift", "Fearless", "Country", "3:51")
song20 = msa.Song("Cardigan", "Taylor Swift", "Folklore", "Indie Folk", "3:59")
song21 = msa.Song("Sorry", "Justin Bieber", "Purpose", "Pop", "3:20")
song22 = msa.Song("Love Yourself", "Justin Bieber", "Purpose", "Pop", "3:53")
song23 = msa.Song("What Do You Mean?", "Justin Bieber", "Purpose", "Pop", "3:25")
song24 = msa.Song("Yummy", "Justin Bieber", "Changes", "R&B", "3:30")
song25 = msa.Song("Intentions", "Justin Bieber", "Changes", "R&B", "3:32")


song_list =[song1, song2, song3, song4, song5, song6, song7, song8, song9, song10,
            song11, song12, song13, song14, song15, song16, song17, song18, song19, song20,
            song21, song22, song23, song24, song25]


music = msa.MusicLibrary()
for i in song_list:
    music.add_song(i)
    
print(*music.get_songs_by_artist("Ariana Grande"), sep="\n",)
print(f"{'-'*70}\n\n")
print(*music.get_songs_by_album("After Hours"), sep="\n",)
print(f"{'-'*70}\n\n")
print(*music.get_songs_by_genre("R&B"), sep="\n")
print(f"{'-'*70}\n\n")
print(music.get_songs_by_title("Blinding Lights"), sep="\n")
print(f"{'-'*70}\n\n")


print("Adding songs into playlist:")
playlist = msa.Playlist("Sokati")
for i in song_list:
    playlist.add_song(i)
playlist.display_playlist()
print("\n\n")


print("Removing songs from playlist:")
playlist.remove_song(song24)
playlist.display_playlist()
