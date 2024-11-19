from dataclasses import dataclass

@dataclass
class Song:
    title: str
    artist: str
    duration: int  # in seconds
    genre: str
    energy_level: int  # 1-10 scale

    def __lt__(self, song2) -> bool:
        return isinstance(song2, Song) and self.energy_level < song2.energy_level
    
    def __str__(self) -> str:
        return f'{self.title} - {self.artist} ({self.duration//60}:{self.duration%60:02}) [{self.genre}] Energy: {self.energy_level}'