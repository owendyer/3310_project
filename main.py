from rich import get_console
import csv

from .constants import USER_FIELD_NAMES, MOVIE_FIELD_NAMES, RATING_FIELD_NAMES


def convert_users_to_csv():
    parsed_users = []
    with open("./datasets/movielens-100k-dataset/versions/1/ml-100k/u.user") as file:
        for line in file:
            # user_id | age | gender | occupation | zip code
            parsed_line = line.strip().split("|")
            parsed_users.append(parsed_line)

    with open("./datasets/movies_dataset/users.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(USER_FIELD_NAMES)
        writer.writerows(parsed_users)


def convert_movies_to_csv():
    parsed_movies = []
    with open("./datasets/movielens-100k-dataset/versions/1/ml-100k/u.item") as file:
        for line in file:
            # id | movie | title | release | date | video | release | date | IMDb | URL | unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy | Film - Noir | Horror | Musical | Mystery | Romance | Sci - Fi | Thriller | War | Western
            parsed_line = line.strip().split("|")
            parsed_movies.append(parsed_line)

    with open("./datasets/movies_dataset/movies.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(MOVIE_FIELD_NAMES)
        writer.writerows(parsed_movies)


def convert_ratings_to_csv():
    parsed_ratings = []
    with open("./datasets/movielens-100k-dataset/versions/1/ml-100k/u.data") as file:
        for line in file:
            # user_id | movie_id | rating | timestamp
            parsed_line = line.strip().split()
            parsed_ratings.append(parsed_line)

    with open("./datasets/movies_dataset/ratings.csv", "w") as file:
        get_console().print(parsed_ratings)
        writer = csv.writer(file)
        writer.writerow(RATING_FIELD_NAMES)
        writer.writerows(parsed_ratings)


# convert_users_to_csv()
# convert_movies_to_csv()
# convert_ratings_to_csv()