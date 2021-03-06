class BlogPost(models.Model):
   title = models.CharField(max_length=200, unique=True)
   slug = models.SlugField(max_length=200, unique=True)
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
   description = models.CharField(max_length=500)
   content = RichTextUploadingField(config_name='awesome_ckeditor')
   tags = TaggableManager()
   category = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)
   keywords = models.CharField(max_length=250)
   cover = models.ImageField(upload_to='images/')
   created_on = models.DateTimeField(auto_now_add=True)
   updated_on = models.DateTimeField(auto_now=True)
   status = models.IntegerField(choices=STATUS, default=0)

   def __str__(self):
       return self.title
   def get_absolute_url(self):
       return reverse("blog:detail", args=[str(self.slug)