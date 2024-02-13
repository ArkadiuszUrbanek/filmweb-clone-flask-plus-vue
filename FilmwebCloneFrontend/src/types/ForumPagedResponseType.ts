export type ForumPagedResponseType = {
  pages_count: number;
  results_count: number;
  current_page_results_count: number;
  forums: {
    id: number;
    name: string;
    creation_date: Date;
    messages_count: number;
    author: {
      id: number;
      firstName: string;
      lastName: string;
    };
  }[];
};
