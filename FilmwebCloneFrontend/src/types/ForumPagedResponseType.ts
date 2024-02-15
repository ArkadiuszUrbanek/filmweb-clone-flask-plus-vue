import type { MessageUploadType } from './MessageUploadType';

export type ForumPagedResponseType = {
  pages_count: number;
  results_count: number;
  current_page_results_count: number;
  forums: {
    id: number;
    name: string;
    description: string;
    tags: string;
    creation_date: Date;
    modification_date: Date;
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
    }[];
    messages_count: number;
    user_id: number;
    user_first_name: string;
    user_last_name: string;
    movie_id: number;
  }[];
};
