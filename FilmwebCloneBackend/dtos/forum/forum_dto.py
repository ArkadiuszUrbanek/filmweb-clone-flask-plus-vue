class ForumDto():
  id = 0
  name = ''
  description = ''
  tags = ''
  creation_date = None
  modification_date = None
  messages = []
  messages_count = 0
  user_id = 0
  user_first_name = ''
  user_last_name = ''
  movie_id = 0

  def to_dict(self):
    return {
      'id' : str(self.id),
      'name' : self.name,
      'description' : self.description,
      'tags' : self.tags,
      'creation_date' : str(self.creation_date),
      'modification_date' : str(self.modification_date),
      'messages' : [message.to_dict() for message in self.messages],
      'messages_count' : str(len(self.messages)),
      'user_id' : str(self.user_id),
      'user_first_name' : self.user_first_name,
      'user_last_name' : self.user_last_name,
      'movie_id' : str(self.movie_id),
    }