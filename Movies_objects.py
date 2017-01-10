import Movies
import fresh_tomatoes
import webbrowser

despicable_me_3 = Movies.Movies("Despicable Me 3", "Grusi go Nuts", "https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg",
"https://www.youtube.com/watch?v=Rlq39IC07qA")

spiderman_homecoming = Movies.Movies("Spiderman Homecoming", "Spiderman Rebooted...Once Again", "https://upload.wikimedia.org/wikipedia/en/2/27/SpiderMan_Homecoming_logo.jpg",
"https://www.youtube.com/watch?v=YPUASeS6qc0")

dr_strange = Movies.Movies("Dr. Strange", "Open your mind. Change your reality.", "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
"https://www.youtube.com/watch?v=HSzx-zryEgM")

avengers = Movies.Movies("Avengers Age Of Ultron", "Must be in his mid 30s", "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
"https://www.youtube.com/watch?v=JAUoeqvedMo")

thor = Movies.Movies("Thor The Dark World", "May be a torch could help", "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",
"https://www.youtube.com/watch?v=npvJ9FTgZbM")

captain_amrica = Movies.Movies("Captain America Civil War", "Divided We Fall", "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
"https://www.youtube.com/watch?v=uVdV-lxRPFo")

movies = [despicable_me_3,spiderman_homecoming,dr_strange,avengers,thor,captain_amrica]


fresh_tomatoes.open_movies_page(movies)
