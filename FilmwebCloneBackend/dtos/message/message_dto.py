class MessageDto():
  id = 0
  text = ''
  forum_id = 0
  user_id = 0
  main_message_id = 0
  messages = []
  creation_date = None
  modification_date = None

  def to_dict(self):
    return {
      'id' : str(self.id),
      'text' : self.text,
      'forum_id' : str(self.forum_id),
      'user_id' : str(self.user_id),
      'main_message_id' : str(self.main_message_id),
      'messages' : [{message.to_dict()} for message in self.messages],
      'creation_date' : str(self.creation_date),
      'modification_date' : str(self.modification_date),
    }