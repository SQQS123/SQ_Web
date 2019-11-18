from django.db import models


def paints_upload_to(instance, filename):
    ext = os.path.splitext(filename)[1]
    fn = "%s_%s%s" % (timezone.now().strftime("%Y%m%d%H%M%S"),
                      random.randint(100000, 999999),
                      ext)
    return "portrait/%s" % fn


# Create your models here.
class Comics(models.Model):
    class Meta:
        db_table = "comics"
    bookename = models.CharField(max_length=20)
    paintername = models.ForeignKey(to="Home.Users", on_delete=models.CASCADE)
    paintsfile = models.ImageField(upload_to=paints_upload_to)

    def get_paintsfile_url(self):
        if not self.paintsfile:
            return
        return self.paintsfile.url