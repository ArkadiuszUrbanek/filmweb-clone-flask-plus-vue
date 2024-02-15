class ForumPagedDto():
  pages_count = 0
  results_count = 0
  current_page_results_count = 0
  forums = []

  def to_dict(self):
    return {
      'pages_count' : str(self.pages_count),
      'results_count' : str(self.results_count),
      'current_page_results_count' : str(self.current_page_results_count),
      'forums' : self.forums,
    }