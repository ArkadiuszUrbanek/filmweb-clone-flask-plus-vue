import type { FilmGenreClass } from './FilmGenreType';

export type FilmDetailedInfoType = {
  id: number;
  title: string;
  subtitle?: string;
  description: string;
  premiere_date: Date;
  length_time: number;
  file_path: string;
  bannerPath: string;
  genres: FilmGenreClass[];
  reviews_count: number;
  average_rating: number;
};

export function getGenres(genres: FilmGenreClass[]) {
  let outputGenre = '';
  for (let genre of genres) {
    outputGenre = genre.name + ' ';
  }
  return outputGenre;
}
