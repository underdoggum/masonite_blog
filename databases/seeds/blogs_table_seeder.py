"""BlogsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogsTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "Ello Gov'nah", "body": "It's a fine day today, innit?"})
        Blog.create({"title": "Oy m8y", "body": "Y'ar be plunderin' me filth!"})
        Blog.create({"title": "ey Good chap", "body": "What y'all got goin' on???"})
        Blog.create({"title": "Last post for a while...", "body": "Tired of making these gotdang voices"})
