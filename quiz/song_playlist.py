def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    res, avail = [], max_size
    subSongs = songs[1:]
    
    sortedSubSongs = sorted(subSongs, key = lambda s: s[2])
    # print(sortedSubSongs)
    
    if songs[0][2] <= avail:
        res.append(songs[0][0])
        avail -= songs[0][2]
        
    for s in sortedSubSongs:
        if s[2] <= avail:
            res.append(s[0])
            avail -= s[2]
        else:
            break
    return res
    
# songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
# print(song_playlist(songs, 11))
songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
print(song_playlist(songs, 12.2))
