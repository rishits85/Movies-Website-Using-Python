import webbrowser

class Movies:

    def __init__(self, name, description, image, video):
        self.title = name
        self.movie_description = description
        self.poster_image_url = image
        self.trailer_youtube_url = video

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
