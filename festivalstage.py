from projects.playlistmanager.song import Song
from datastructures.linkedlist import LinkedList



class FestivalStage:
    """Class to manage a playlist for a music festival stage."""

    def __init__(self, name: str):
        """Initialize the stage with a name and an empty playlist."""
        self._name: str = name
        self._playlist: LinkedList[Song] = LinkedList([])

    def add_song(self, song: Song) -> None:
        """Add a song to the end of the playlist."""
        self._playlist.append(song)

    def emergency_insert(self, song: Song, position: int) -> None:
        """Insert a song at a specific position for urgent additions."""
        self._playlist.insert_at(song, position-1)

    def remove_song(self, title: str) -> Song:
        """Remove and return a song by its title."""
        index = 0
        for song in self._playlist:
            if song.title == title:
                item = self._playlist.pop_at(index)
            index += 1
        return item

    def swap_songs(self, pos1: int, pos2: int) -> None:
        """Swap the positions of two songs in the playlist."""
        self._playlist[pos1-1], self._playlist[pos2-1] = self._playlist[pos2-1], self._playlist[pos1-1]

    def create_energy_wave(self) -> None:
        """Reorder playlist to alternate between high and low energy songs."""
        self.crowd_pleaser_mode()
        boolean = True
        new_list = self._playlist
        new_list2 = LinkedList([])
        for i in range(len(new_list)):
            if boolean:
                item = new_list.pop_front()
            else:
                item = new_list.pop_back()
            new_list2.append(item)
            #new_list2.append(new_list.pop_front) if boolean else new_list2.append(new_list.pop_back)
            boolean = not boolean
        self._playlist = new_list2
        

    def crowd_pleaser_mode(self) -> None:
        """Move all high-energy songs to the front of the playlist."""
        for i in range(len(self._playlist)):
            sorted = True
            for j in range(len(self._playlist) - i - 1):
                if self._playlist[j].energy_level < self._playlist[j + 1].energy_level:
                    self._playlist[j].energy_level, self._playlist[j + 1].energy_level = self._playlist[j + 1].energy_level, self._playlist[j].energy_level
                    sorted = False
            if sorted:
                break

    def genre_block(self, genre: str) -> None:
        """Group all songs of a specified genre together."""
        new_list = LinkedList([])
        index = 0
        for song in self._playlist:
            if song.genre == genre:
                new_list.append(self._playlist.pop_at(index))
            else:
                index += 1
        for song in self._playlist:
            new_list.append(song)
        self._playlist = new_list

    def estimated_time_remaining(self) -> int:
        """Calculate total remaining time in the playlist."""
        time = 0
        for song in self._playlist:
            time += song.duration
        return time

    def print_playlist(self) -> None:
        """Display the current playlist with song details."""
        number = 1
        for song in self._playlist:
            print(f'{number}. {song.title} - {song.artist} ({song.duration//60}:{song.duration%60:02}) [{song.genre}] Energy: {song.energy_level}')
            number += 1
        print(f'Total Time: {(self.estimated_time_remaining())//60}:{(self.estimated_time_remaining())%60:02}')

    def play_current_song(self) -> Song:
        """Play (remove) the first song in the playlist."""
        song = self._playlist.pop_front()
        return song
    