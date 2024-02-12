import type { FilmGenreClass } from './FilmGenreType';

export type FilmBasicInfoType = {
  id: number;
  title: string;
  subtitle?: string;
  premiere_date: Date;
  length_time: number;
  file_path: string;
  genres: FilmGenreClass[];
  reviews_count: number;
  average_rating: number;
};
