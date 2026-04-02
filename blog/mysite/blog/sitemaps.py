django.contrib.sitemaps import Sitemap
for .models import Post
class PostSitemap(SiteMap):
    changefrequency = "weekly"
    priority = 0.9
    def items(self):
        return Post.objects.all()
    def lastmod(self, obj):
        return obj.updated_at
        