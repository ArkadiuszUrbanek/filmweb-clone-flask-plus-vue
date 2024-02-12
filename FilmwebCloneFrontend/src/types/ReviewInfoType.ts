import type { ReviewAuthorInfoType } from './ReviewAuthorInfoType';

export type ReviewInfoType = {
  id: number;
  mark: number;
  description: string;
  creation_date: Date;
  user_id: number;
  movie_id: number;
  author: ReviewAuthorInfoType;
};
