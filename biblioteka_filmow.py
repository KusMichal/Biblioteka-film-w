import random



class Movies:
    def __init__(self,title,year,genre, curent_played):
        self.title = title
        self.year = year
        self.genre = genre
        self.current_played = curent_played
        
        
    def __str__(self):
        return f'{self.title}, rok produkcji:{self.year}.'
    
    def __repr__(self) -> str:
        return{self.title},{self.year},{self.current_played}
    
    def play(self, played =1):
         self.current_played += played
         
    



class Serials(Movies):
    def __init__(self, episode,sezon,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.episode = episode
        self.sezon = sezon
    
    def __str__(self):
        return f'{self.title}, S{self.sezon:02}E{self.episode:02}.'
    
    def __repr__(self) -> str:
        return f'{self.title} S{self.sezon:02}E{self.episode:02}{self.current_played}'


movie = Movies(title="Sacary Movie", year="2000",genre="Horror, Comedy",curent_played=0 )
serial = Serials(title="The Simson", year="1998",genre="Animation, Comedy", episode=1, sezon =1,curent_played=0)
libary = [movie,serial]


def get_serials():
    serials = []
    for i in libary:
        if type(i) == Serials:
                serials.append(i)
    return(sorted(serials, key=lambda serials: serials.title))               

def get_movies():
    movies = []
    for i in libary:
        if type(i) == Movies:
            movies.append(i)
    return sorted(movies, key=lambda movie: movie.title)
       
def search():
    title = input("Podaj tytuł:  ")
    for i in libary:
        if title == i.title:
            print(i)


def generate_views():
        random_view = random.choice(libary)
        random_number = random.randrange(1,101)
        for i in libary:
            if i == random_view:
               i.play(played = random_number)

def g_views_10():
    for i in range(10):
        generate_views()

def top_titles(top):
    libary_by_curent_played = sorted(libary, key=lambda plays: plays.current_played)
    print(libary_by_curent_played[:top])
    

movie = Movies(title="Scary Movie", year="2000",genre="Horror, Comedy",curent_played=5 )
serial = Serials(title="The Simson", year="1998",genre="Animation, Comedy", episode=1, sezon =1,curent_played=0)
libary = [movie,serial]


generate_views()
g_views_10()
movie.play()
serial.play()
print(movie)
print(movie.current_played)
print(serial)
print(serial.current_played)
print(get_serials())
search()
print(top_titles(0))