import type { GenderType } from './GenderType';

export type ForumMessagesInfoType = {
  id: number;
  name: string;
  description: string;
  tags: string;
  creation_date: Date;
  modfication_date: Date;
  messages: {
    id: number;
    text: string;
    forum_id: number;
    main_message_id: number;
    creation_date: Date;
    modification_date: Date;
    user_id: number;
    user_first_name: string;
    user_last_name: string;
    user_gender: GenderType;
  }[];
};
