import requests
from django.core.management.base import BaseCommand
from movies.models import Movie, Director, Actor


class Command(BaseCommand):
    help = 'Fetches movie data from an external API and populates the database'
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to fetch movie data...'))
        
        # 외부 api url (대괄호 제거)
        url = "http://43.200.28.219:1313/movies/"

        try:
            res = requests.get(url)
            res.raise_for_status()
            movies_data = res.json().get('movies', [])

            for movie_data in movies_data:
                director_name = movie_data.get('director_name')
                director, created = Director.objects.get_or_create(
                    name=director_name, 
                    defaults={'image_url': movie_data.get('director_image_url', '')}
                )
                
                movie, movie_created = Movie.objects.get_or_create(
                    title_kor=movie_data['title_kor'],
                    defaults={
                        'title_eng': movie_data.get('title_eng', ''),
                        'poster_url': movie_data.get('poster_url', ''),
                        'genre': movie_data.get('genre', ''),
                        'showtime': movie_data.get('showtime', ''),
                        'release_date': movie_data.get('release_date', ''),
                        'plot': movie_data.get('plot', ''),
                        'rating': movie_data.get('rating', ''),
                        'director': director
                    }
                )
                
                if not movie_created:
                    self.stdout.write(self.style.WARNING(f"Movie '{movie.title_kor}' already exists. Skipping."))
                    continue

                # 배우정보처리
                actors_data = movie_data.get('actors', [])
                for actor_data in actors_data:
                    actor, created = Actor.objects.get_or_create(
                        name=actor_data['name'],  # 문법 오류 수정
                        character=actor_data.get('character', ''),
                        defaults={'image_url': actor_data.get('image_url', '')}
                    )
                    movie.actors.add(actor)
                
                self.stdout.write(self.style.SUCCESS(f"Successfully added movie: {movie.title_kor}"))
        
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching data: {e}'))
        
        self.stdout.write(self.style.SUCCESS('Finished populating database.'))