"""
Field names for the .csv files
"""
USER_FIELD_NAMES: list[str] = ["id", "age", "gender", "occupation", "zip_code"]
MOVIE_FIELD_NAMES: list[str] = ["id", "movie", "title", "release", "date", "video", "release", "date", "IMDb", "URL",
                                "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime",
                                "Documentary", "Drama", "Fantasy", "Film - Noir", "Horror", "Musical", "Mystery",
                                "Romance", "Sci - Fi", "Thriller", "War", "Western"]
RATING_FIELD_NAMES: list[str] = ["user_id", "movie_id", "rating", "timestamp"]
"""
Movie genres
"""
MOVIE_GENRES: list[str] = ["unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime",
                           "Documentary", "Drama", "Fantasy", "Film - Noir", "Horror", "Musical", "Mystery", "Romance",
                           "Sci - Fi", "Thriller", "War", "Western"]
"""
Occupations
"""
OCCUPATIONS: list[str] = ["administrator", "artist", "doctor", "educator", "engineer", "entertainment", "executive",
                          "healthcare", "homemaker", "lawyer", "librarian", "marketing", "none", "other", "programmer",
                          "retired", "salesman", "scientist", "student", "technician", "writer"]
