import type { ReviewAuthorInfoType } from './ReviewAuthorInfoType';

export type ReviewInfoType = {
  id: number;
  mark: number;
  description: string;
  creation_date: Date;
  user_id: number;
  movie_id: number;
  user_first_name: string;
  user_last_name: string;
  user_gender: string;
};
