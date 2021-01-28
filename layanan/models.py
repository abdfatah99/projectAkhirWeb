from django.db import models

from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class catalog(models.Model):

    LOKASI = (
                ('semua lokasi','Semua Lokasi'),
                ('perpustakaan ft','Perpustakaan FT'),
                ('perpustakaan fkip','Perpustakaan FKIP'),
                ('perpustakaan fk','Perpustakaan FK'),
                ('perpustakaan fisip','Perpustakaan FISIP'),
                ('perpustakaan ffs','Perpustakaan FFS'),
                ('perpustakaan feb','Perpustakaan FEB'),   
            )

    KATALOG_JURUSAN = (
                ('psikologi','Psikologi'),
                ('informatika','Informatika'),
                ('teknik mesin','Teknik Mesin'),
                ('teknik elektro','Teknik Elektro'),
                ('kedokteran','Kedokteran'),
                ('farmasi','Farmasi'),
                ('biologi','Biologi'),
                ('fisika','Fisika'),
            )

    BAHASA = (
        ('indonesia','Indonesia'),
        ('english','English')
    )

    lokasi = models.CharField(max_length=200, choices=LOKASI, default='semua lokasi')
    judul = models.CharField(max_length=200, blank=True)
    penulis = models.CharField(max_length=200, blank=True)
    katalog_jurusan = models.CharField(max_length=200, choices=KATALOG_JURUSAN, default='psikologi')
    keyword = models.CharField(max_length=200, null=True, blank=True)
    jumlah_buku = models.IntegerField()
    bahasa = models.CharField(max_length=200, null=True, choices=BAHASA)

    def __str__(self):
        return "{}".format(self.judul)

class journal(models.Model):

    judul_artikel   = models.CharField(max_length=200, blank=True)
    judul_terbitan  = models.CharField(max_length=200)
    issn            = models.IntegerField(blank=True)
    bahasa          = models.CharField(max_length=200)
    tempat_terbit   = models.CharField(max_length=200)
    tahun           = models.IntegerField()
    volume          = models.CharField(max_length=200)
    penerbit        = models.CharField(max_length=200)
    frekuensi_penerbitan = models.CharField(max_length=200)
    penulis         = models.CharField(max_length=200, blank=True)
    abstraksi       = models.TextField()
    kata_kunci      = models.CharField(max_length=200, blank=True)
    lokasi          = models.CharField(max_length=200, blank=True)
    terakreditasi   = models.CharField(max_length=200)
    slug            = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul_artikel)
        super().save()

    def get_absolute_url(self):
        return reverse('layanan:journal_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return "{}".format(self.judul_artikel)

class repository(models.Model):
    JENIS_PENULISAN = (
                ('semua penulisan', 'Semua Penulisan'),
                ('disertasi','Disertasi'),
                ('tesis','Tesis'),
                ('skripsi','Skripsi'),
            )

    LOKASI = (
                ('semua fakultas','Semua Fakultas'),
                ('ekonomi bisnis','Ekonomi dan Bisnis'),
                ('teknik','Teknik'),
                ('agama islam','Agama Islam'),
                ('psikologi','Psikologi'),
                ('kedokteran','Kedokteran'),
                ('keguruan','Keguruan dan Ilmu Pendidikan'),
                ('ilmu kesehatan','Ilmu Ilmu Kesehatan'),
                ('farmasi','Farmasi dan Sains'),
                ('sosial politik', 'Ilmu Sosial dan Ilmu Politik'),
                ('pascasarjana','Pascasarjana')  
            )

    judul           = models.CharField(max_length=200, blank=True)
    penulis         = models.CharField(max_length=200, blank=True)
    abstraksi       = models.TextField()
    keyword         = models.CharField(max_length=200, null=True, blank=True)
    pembimbing      = models.CharField(max_length=200)
    jenis_penulisan = models.CharField(max_length=200, choices=JENIS_PENULISAN, default='semua penulisan')
    lokasi          = models.CharField(max_length=200, choices=LOKASI, default='semua fakultas')
    slug            = models.SlugField(blank=True, editable=False)


    def __str__(self):
        return "{}".format(self.judul)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def get_absolute_url(self):
        return reverse('layanan:repository_detail', kwargs={'slug': self.slug})