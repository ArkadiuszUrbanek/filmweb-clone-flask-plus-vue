class ForumDto():
  id = 0
  name = ''
  description = ''
  tags = ''
  creation_date = None
  modification_date = None
  messages = []
  user_id = 0
  movie_id = 0

  def to_dict(self):
    return {
      'id' : str(self.id),
      'name' : self.name,
      'description' : self.description,
      'tags' : self.tags,
      'creation_date' : str(self.creation_date),
      'modficiation_date' : str(self.modification_date),
      'messages' : [{message.to_dict()} for message in self.messages],
      'user_id' : str(self.user_id),
      'movie_id' : str(self.movie_id),
    }