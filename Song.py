class Song:
 
  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  #  Getter method for the title attribute, called get_title
  def get_title(self):
    return self.__title
  
  
  #  Setter method for the next_song attribute, called set_title. Titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    self.__title = title.title()


  #  Getter method for the next_song attribute.
  def get_next_song(self):
    return self.__next_song


  # Setter method for the next_song attribute.
  def set_next_song(self, next_title):
    self.__next_song = next_title


  # Returns a string of the song title.
  def __str__(self):
    return f"{self.get_title()}"


  # Returns a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    if self.__next_song is not None:
      return f"{self.get_title()} --> {self.__next_song}"
    return f"{self.get_title()} --> None"
