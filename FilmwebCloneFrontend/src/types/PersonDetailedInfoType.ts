import type { GenderType } from './GenderType';
import type { PersonNationalityType } from './PersonNationalityType';

export type PersonDetailedInfoType = {
  id: number;
  first_name: string;
  last_name: string;
  gender: GenderType;
  nationality: PersonNationalityType;
  height: number;
  birth_date: Date;
  description: string;
  file_path: string;
};
