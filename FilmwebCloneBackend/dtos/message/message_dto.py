from enums import UserGender

class MessageDto():
  id = 0
  text = ''
  forum_id = 0
  user_id = 0
  user_first_name = ''
  user_last_name = ''
  user_gender = UserGender.MALE
  main_message_id = 0
  messages = None
  creation_date = None
  modification_date = None

  def to_dict(self):
    return {
      'id' : str(self.id),
      'text' : self.text,
      'forum_id' : str(self.forum_id),
      'user_id' : str(self.user_id),
      'user_first_name' : str(self.user_first_name),
      'user_last_name' : str(self.user_last_name),
      'user_gender' : str(self.user_gender),
      'main_message_id' : str(self.main_message_id),
      'messages' : self.messages.to_dict() if self.messages != None else None,
      'creation_date' : str(self.creation_date),
      'modification_date' : str(self.modification_date),
    }