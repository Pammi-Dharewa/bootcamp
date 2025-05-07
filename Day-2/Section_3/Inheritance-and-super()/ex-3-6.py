class AudioMixin:
    def play_audio(self):
        return f"Playing audio for {self.title}"

class AudioBook(Book, AudioMixin):
    pass

ab = AudioBook("The Hobbit", "Tolkien")
print(ab.play_audio())  # Output: Playing audio for The Hobbit
