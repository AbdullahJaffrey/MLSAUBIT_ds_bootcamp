import streamlit as st
import hashlib
import warnings
import requests
import pandas as pd
from difflib import get_close_matches


# Function to hash passwords
def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()


# Function to create an account
def create_account(username, password, user_data):
  hashed_password = hash_password(password)

  # Create a new DataFrame with the updated data
  new_user_data = pd.concat([
      user_data,
      pd.DataFrame({
          'Username': [username],
          'Password': [hashed_password]
      })
  ],
                            ignore_index=True)

  # Save the updated DataFrame to the CSV file
  new_user_data.to_csv('user_data.csv', index=False)

  return new_user_data


# Function to check login credentials
def check_login(username, password, user_data):
  hashed_password = hash_password(password)
  user = user_data[(user_data['Username'] == username)
                   & (user_data['Password'] == hashed_password)]
  return not user.empty


# Function to get movie details using TMDb API
def get_movie_details(movie_id):
  url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
  data = requests.get(url)
  data = data.json()
  return data


# Function to find similar movie names
def find_similar_movies(movie_name, available_movies):
  matches = get_close_matches(movie_name, available_movies, n=1, cutoff=0.6)
  return matches[0] if matches else None


# # Recommendation function
# def recommend(movie_name):
# index = movie_name[movie_name['title'] == movie_name].index[0]
# distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
# recommended_movie_names = []
# recommended_movie_posters = []
# for i in distances[1:6]:
#     # Helps in fetching the movies poster
#     movie_id = movie_name.iloc[i[0]].movie_id
#     recommended_movie_posters.append(fetch_poster(movie_id))
#     recommended_movie_names.append(movie_name.iloc[i[0]].title)

# return recommended_movie_names,recommended_movie_posters

# Load user data from CSV file or create a new DataFrame if the file doesn't exist
try:
  user_data = pd.read_csv('user_data.csv')
except FileNotFoundError:
  user_data = pd.DataFrame(columns=['Username', 'Password'])

# Streamlit app
st.title('Movie Recommendation System: ')
# Page state
page_state = st.experimental_get_query_params().get("page", ["login"])[0]

if page_state == "signup":
  st.subheader('Sign Up')
  new_username = st.text_input('Username:')
  new_password = st.text_input('Password:', type='password')

  if st.button('Create Account'):
    if new_username and new_password:
      user_data = create_account(new_username, new_password, user_data)
      st.success('Account created successfully! Please login.')
      st.experimental_set_query_params(page="login")
    else:
      st.warning('Please enter both username and password.')

elif page_state == "login":
  st.subheader('Login')
  username = st.text_input('Username:')
  password = st.text_input('Password:', type='password')

  if st.button('Login'):
    if username and password:
      if check_login(username, password, user_data):
        st.success(f'Welcome, {username}! [Movie here](?page=movie)')
        page_state = "movie"
        st.experimental_set_query_params(page="movie")

      else:
        st.warning('Invalid username or password. Please try again.')
    else:
      st.warning('Please enter both username and password.')

elif page_state == "movie":

  movie_ids = {
      'Inception': {
          'id': 27205,
          'genre': 'Sci-Fi'
      },
      'The Shawshank Redemption': {
          'id': 278,
          'genre': 'Drama'
      },
      'The Godfather': {
          'id': 238,
          'genre': 'Crime'
      },
      'Pulp Fiction': {
          'id': 680,
          'genre': 'Crime'
      },
      'The Dark Knight': {
          'id': 155,
          'genre': 'Action'
      },
      'Schindler\'s List': {
          'id': 424,
          'genre': 'Biography'
      },
      'Forrest Gump': {
          'id': 13,
          'genre': 'Drama'
      },
      'Fight Club': {
          'id': 550,
          'genre': 'Drama'
      },
      'The Matrix': {
          'id': 603,
          'genre': 'Action'
      },
      'The Lord of the Rings: The Fellowship of the Ring': {
          'id': 120,
          'genre': 'Adventure'
      },
      'The Silence of the Lambs': {
          'id': 274,
          'genre': 'Crime'
      },
      'Titanic': {
          'id': 597,
          'genre': 'Romance'
      },
      'Star Wars: Episode IV - A New Hope': {
          'id': 11,
          'genre': 'Sci-Fi'
      },
      'Jurassic Park': {
          'id': 329,
          'genre': 'Adventure'
      },
      'The Lion King': {
          'id': 8587,
          'genre': 'Animation'
      },
      'Casablanca': {
          'id': 289,
          'genre': 'Drama'
      },
      'Gone with the Wind': {
          'id': 770,
          'genre': 'Drama'
      },
      'Citizen Kane': {
          'id': 15,
          'genre': 'Drama'
      },
      'Avatar': {
          'id': 19995,
          'genre': 'Sci-Fi'
      },
      'The Terminator': {
          'id': 218,
          'genre': 'Action'
      },
      'The Shining': {
          'id': 694,
          'genre': 'Horror'
      },
      'Braveheart': {
          'id': 197,
          'genre': 'Biography'
      },
      'The Departed': {
          'id': 1422,
          'genre': 'Crime'
      },
      'The Godfather: Part II': {
          'id': 240,
          'genre': 'Crime'
      },
      'The Lord of the Rings: The Two Towers': {
          'id': 121,
          'genre': 'Adventure'
      },
      'The Lord of the Rings: The Return of the King': {
          'id': 122,
          'genre': 'Adventure'
      },
      'Inglourious Basterds': {
          'id': 16869,
          'genre': 'Adventure'
      },
      'Goodfellas': {
          'id': 769,
          'genre': 'Biography'
      },
      'The Usual Suspects': {
          'id': 629,
          'genre': 'Crime'
      },
      'Se7en': {
          'id': 807,
          'genre': 'Crime'
      },
      'The Green Mile': {
          'id': 497,
          'genre': 'Drama'
      },
      'The Pianist': {
          'id': 423,
          'genre': 'Biography'
      },
      'Gladiator': {
          'id': 98,
          'genre': 'Action'
      },
      'The Intouchables': {
          'id': 65754,
          'genre': 'Biography'
      },
      'The Prestige': {
          'id': 1124,
          'genre': 'Drama'
      },
      'Memento': {
          'id': 77,
          'genre': 'Mystery'
      },
      'The Grand Budapest Hotel': {
          'id': 120467,
          'genre': 'Adventure'
      },
      'The Revenant': {
          'id': 281957,
          'genre': 'Adventure'
      },
      'A Beautiful Mind': {
          'id': 453,
          'genre': 'Biography'
      },
      'The Sixth Sense': {
          'id': 745,
          'genre': 'Drama'
      },
      'The Social Network': {
          'id': 37799,
          'genre': 'Biography'
      },
      'Jaws': {
          'id': 578,
          'genre': 'Adventure'
      },
      'E.T. the Extra-Terrestrial': {
          'id': 601,
          'genre': 'Sci-Fi'
      },
      'Back to the Future': {
          'id': 105,
          'genre': 'Adventure'
      },
      'The Princess Bride': {
          'id': 2493,
          'genre': 'Adventure'
      },
      'Forrest Gump': {
          'id': 13,
          'genre': 'Drama'
      },
      'The Big Lebowski': {
          'id': 115,
          'genre': 'Comedy'
      },
      'Blade Runner': {
          'id': 78,
          'genre': 'Sci-Fi'
      },
      'The Breakfast Club': {
          'id': 802,
          'genre': 'Drama'
      },
      'The Truman Show': {
          'id': 37165,
          'genre': 'Comedy'
      },
      'The Dark Knight Rises': {
          'id': 49026,
          'genre': 'Action'
      },
      'American History X': {
          'id': 73,
          'genre': 'Drama'
      },
      'A Clockwork Orange': {
          'id': 185,
          'genre': 'Crime'
      },
      'The Great Gatsby': {
          'id': 64682,
          'genre': 'Drama'
      },
      'The Usual Suspects': {
          'id': 629,
          'genre': 'Crime'
      },
      'The Silence of the Lambs': {
          'id': 274,
          'genre': 'Crime'
      },
      'The Terminator': {
          'id': 218,
          'genre': 'Action'
      },
      'Eternal Sunshine of the Spotless Mind': {
          'id': 38,
          'genre': 'Drama'
      },
      'Inglourious Basterds': {
          'id': 16869,
          'genre': 'Adventure'
      },
      'The Matrix Reloaded': {
          'id': 604,
          'genre': 'Action'
      },
      'The Matrix Revolutions': {
          'id': 605,
          'genre': 'Action'
      },
      'The Hangover': {
          'id': 18785,
          'genre': 'Comedy'
      },
      'The Wolf of Wall Street': {
          'id': 106646,
          'genre': 'Biography'
      },
      'Django Unchained': {
          'id': 68718,
          'genre': 'Western'
      },
      'The Big Short': {
          'id': 318846,
          'genre': 'Biography'
      },
      'Interstellar': {
          'id': 157336,
          'genre': 'Sci-Fi'
      },
      'Inception': {
          'id': 27205,
          'genre': 'Sci-Fi'
      },
      'The Martian': {
          'id': 286217,
          'genre': 'Adventure'
      },
      'Gravity': {
          'id': 49047,
          'genre': 'Sci-Fi'
      },
      'La La Land': {
          'id': 313369,
          'genre': 'Musical'
      },
      'Whiplash': {
          'id': 244786,
          'genre': 'Drama'
      },
      'Casino Royale': {
          'id': 36557,
          'genre': 'Action'
      },
      'Skyfall': {
          'id': 37724,
          'genre': 'Action'
      },
      'The Bourne Identity': {
          'id': 2501,
          'genre': 'Action'
      },
      'The Bourne Supremacy': {
          'id': 2502,
          'genre': 'Action'
      },
      'The Bourne Ultimatum': {
          'id': 2503,
          'genre': 'Action'
      },
      'The Shawshank Redemption': {
          'id': 278,
          'genre': 'Drama'
      },
      'The Green Mile': {
          'id': 497,
          'genre': 'Drama'
      },
      'The Godfather': {
          'id': 238,
          'genre': 'Crime'
      },
      'The Godfather: Part II': {
          'id': 240,
          'genre': 'Crime'
      },
      'The Dark Knight': {
          'id': 155,
          'genre': 'Action'
      },
      'Schindler\'s List': {
          'id': 424,
          'genre': 'Biography'
      },
      'Pulp Fiction': {
          'id': 680,
          'genre': 'Crime'
      },
      'Fight Club': {
          'id': 550,
          'genre': 'Drama'
      },
      'Forrest Gump': {
          'id': 13,
          'genre': 'Drama'
      },
      'The Silence of the Lambs': {
          'id': 274,
          'genre': 'Crime'
      },
      'The Matrix': {
          'id': 603,
          'genre': 'Action'
      },
      'The Lord of the Rings: The Fellowship of the Ring': {
          'id': 120,
          'genre': 'Adventure'
      },
      'The Lord of the Rings: The Two Towers': {
          'id': 121,
          'genre': 'Adventure'
      },
      'The Lord of the Rings: The Return of the King': {
          'id': 122,
          'genre': 'Adventure'
      },
      'Titanic': {
          'id': 597,
          'genre': 'Romance'
      },
      'Avatar': {
          'id': 19995,
          'genre': 'Sci-Fi'
      },
      'Jurassic Park': {
          'id': 329,
          'genre': 'Adventure'
      },
      'The Lion King': {
          'id': 8587,
          'genre': 'Animation'
      },
      'Casablanca': {
          'id': 289,
          'genre': 'Drama'
      },
      'Gone with the Wind': {
          'id': 770,
          'genre': 'Drama'
      },
      'Citizen Kane': {
          'id': 15,
          'genre': 'Drama'
      },
      'The Terminator': {
          'id': 218,
          'genre': 'Action'
      },
      'Braveheart': {
          'id': 197,
          'genre': 'Biography'
      },
      'Gladiator': {
          'id': 98,
          'genre': 'Action'
      },
      'The Shawshank Redemption': {
          'id': 278,
          'genre': 'Drama'
      },
      'The Godfather': {
          'id': 238,
          'genre': 'Crime'
      },
      'The Dark Knight': {
          'id': 155,
          'genre': 'Action'
      },
      'Pulp Fiction': {
          'id': 680,
          'genre': 'Crime'
      },
      'The Silence of the Lambs': {
          'id': 274,
          'genre': 'Crime'
      },
      'Fight Club': {
          'id': 550,
          'genre': 'Drama'
      },
      'Forrest Gump': {
          'id': 13,
          'genre': 'Drama'
      },
      'The Matrix': {
          'id': 603,
          'genre': 'Action'
      },
      'The Lord of the Rings: The Fellowship of the Ring': {
          'id': 120,
          'genre': 'Adventure'
      },
      'The Lord of the Rings: The Two Towers': {
          'id': 121,
          'genre': 'Adventure'
      },
      'The Lord of the Rings: The Return of the King': {
          'id': 122,
          'genre': 'Adventure'
      },
      'Titanic': {
          'id': 597,
          'genre': 'Romance'
      },
      'Jurassic Park': {
          'id': 329,
          'genre': 'Adventure'
      },
      'The Lion King': {
          'id': 8587,
          'genre': 'Animation'
      },
      'Casablanca': {
          'id': 289,
          'genre': 'Drama'
      },
      'Gone with the Wind': {
          'id': 770,
          'genre': 'Drama'
      },
      'Citizen Kane': {
          'id': 15,
          'genre': 'Drama'
      },
      'The Terminator': {
          'id': 218,
          'genre': 'Action'
      },
      'Braveheart': {
          'id': 197,
          'genre': 'Biography'
      },
      'Inglourious Basterds': {
          'id': 16869,
          'genre': 'War'
      },
      'Goodfellas': {
          'id': 769,
          'genre': 'Biography'
      },
      'The Usual Suspects': {
          'id': 629,
          'genre': 'Crime'
      },
      'Se7en': {
          'id': 807,
          'genre': 'Crime'
      },
      'The Green Mile': {
          'id': 497,
          'genre': 'Crime'
      },
      'The Pianist': {
          'id': 423,
          'genre': 'Biography'
      },
      'Gladiator': {
          'id': 98,
          'genre': 'Action'
      },
      'The Intouchables': {
          'id': 65754,
          'genre': 'Biography'
      },
      'The Prestige': {
          'id': 1124,
          'genre': 'Drama'
      },
      'Memento': {
          'id': 77,
          'genre': 'Mystery'
      },
      'The Grand Budapest Hotel': {
          'id': 120467,
          'genre': 'Adventure'
      },
      'The Revenant': {
          'id': 281957,
          'genre': 'Action'
      },
      'A Beautiful Mind': {
          'id': 453,
          'genre': 'Biography'
      },
      'The Sixth Sense': {
          'id': 745,
          'genre': 'Drama'
      },
      'The Social Network': {
          'id': 37799,
          'genre': 'Biography'
      },
      'Jaws': {
          'id': 578,
          'genre': 'Adventure'
      },
      'E.T. the Extra-Terrestrial': {
          'id': 601,
          'genre': 'Family'
      },
      'Back to the Future': {
          'id': 105,
          'genre': 'Adventure'
      },
      'The Princess Bride': {
          'id': 2493,
          'genre': 'Adventure'
      },
      'Forrest Gump': {
          'id': 13,
          'genre': 'Drama'
      },
      'The Big Lebowski': {
          'id': 115,
          'genre': 'Comedy'
      },
      'Blade Runner': {
          'id': 78,
          'genre': 'Action'
      },
  }
  # Convert the dictionary to a DataFrame for easier display
  movies_df = pd.DataFrame(list(movie_ids.items()), columns=['Title', 'Info'])

  # Split the 'Info' column into 'ID' and 'Genre' columns
  movies_df[['ID', 'Genre']] = pd.DataFrame(movies_df['Info'].tolist(),
                                            index=movies_df.index)

  # Display the table with full genre names
  genre_mapping = {
      'S': 'Sci-Fi',
      'D': 'Drama',
      'C': 'Crime',
      'A': 'Action',
      'B': 'Biography',
      'H': 'Horror'
  }
  movies_df['Genre'] = movies_df['Genre'].str[0].map(genre_mapping)

  st.subheader('Available Movies:')
  st.table(movies_df[['Title', 'Genre']].head(7))

  # User selects either Movie or Genre
  selection_type = st.radio("Select by:", ["Movie", "Genre"])

  # Movie selection
  if selection_type == "Movie":
    # User enters a movie name
    movie_name_input = st.text_input('Enter a movie name:')

    # Check if the entered movie name is in the available movies
    if movie_name_input in movies_df['Title'].tolist():
      selected_movie_title = movie_name_input
      selected_movie_data = get_movie_details(
          movie_ids[selected_movie_title]['id'])
      # Redirect to a new page to display movie details
      st.markdown(
          f"[Movie Details](#{selected_movie_title.replace(' ', '-')} Movie Details)"
      )
    else:
      # Find similar movies and recommend
      similar_movie = find_similar_movies(movie_name_input, movies_df['Title'])
      if similar_movie:
        st.warning(f"Movie not found. Did you mean: {similar_movie}")
      else:
        st.warning("Movie not found. No similar movies available.")

    # Display the selected movie details
    if 'selected_movie_data' in locals() and selected_movie_data:
      # Display movie details on a new page
      st.markdown(
          f"<h2 id='{selected_movie_title.replace(' ', '-')} Movie Details'>{selected_movie_title}</h2>",
          unsafe_allow_html=True)
      st.image(
          f"https://image.tmdb.org/t/p/w500/{selected_movie_data['poster_path']}",
          caption='Movie Poster',
          use_column_width=True)
      st.write(f"Title: {selected_movie_data['title']}")
      st.write(
          f"Genre: {', '.join([genre['name'] for genre in selected_movie_data['genres']])}"
      )
      st.write(f"Release Date: {selected_movie_data['release_date']}")
      st.write(f"Overview: {selected_movie_data['overview']}")
      st.write(f"Rating: {selected_movie_data['vote_average']}")

  # Genre selection
  elif selection_type == "Genre":
    # User selects a genre
    selected_genre = st.selectbox('Select a genre',
                                  movies_df['Genre'].dropna().unique())
    filtered_movies_df = movies_df[movies_df['Genre'] == selected_genre]

    # Display table of movies in the selected genre on a separate page
    st.markdown(
        f"<h2 id='{selected_genre.replace(' ', '-')} Movies'>{selected_genre} Movies</h2>",
        unsafe_allow_html=True)
    st.subheader(f'Movies in the {selected_genre} genre:')
    st.table(filtered_movies_df[['Title', 'Genre']])
    # ML Based Work

    # movies = pickle.load(open('movie_list.pkl','rb'))
    # similarity = pickle.load(open('similarity.pkl','rb'))

    # movie_list = movies['title'].values
    # selected_movie = st.selectbox(
    #     "Type or select a movie from the dropdown",
    #     movie_list
    # )

    # if st.button('Show Recommendation'):
    #   recommended_movie_names,recommended_movie_posters = recommend(movie_name_input)
    #   col1, col2, col3 = st.columns(3)
    #   with col1:
    #       st.text(recommended_movie_names[0])
    #       st.image(recommended_movie_posters[0])
    #   with col2:
    #       st.text(recommended_movie_names[1])
    #       st.image(recommended_movie_posters[1])
    #   with col3:
    #       st.text(recommended_movie_names[2])
    #       st.image(recommended_movie_posters[2])

# Add a link to switch between signup and login pages
if page_state == "signup":
  st.markdown("Already have an account? [Login here](?page=login)")
else:
  st.markdown("Don't have an account? [Sign up here](?page=signup)")
