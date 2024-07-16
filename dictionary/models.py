from django.db import models

# Create your models here.
class Source(models.Model):
    source_id = models.AutoField(primary_key=True, null=False, default=0)
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    year = models.IntegerField(blank=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f'{self.surname}, {self.name} ({self.year}) - {self.title}'

class Entry(models.Model):
    nowakowski = models.CharField(max_length=50, primary_key=True)
    kostakis = models.CharField(max_length=50, null = True) 
    greek = models.CharField(max_length=200, null = True)
    paradigm = models.CharField(max_length=5, null = True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null = True)
    lemma = models.CharField(max_length=50, null = True)
    ipa = models.CharField(max_length=50, null = True)
    leonidio = models.BooleanField(default=False, null=True)
    voskina = models.BooleanField(default=False, null = True)
    pragmateutis = models.BooleanField(default=False, null = True)
    sampatiki = models.BooleanField(default=False, null = True)
    livadi = models.BooleanField(default=False, null = True)
    tyros = models.BooleanField(default=False, null = True)
    melana = models.BooleanField(default=False, null = True)
    sapounakaiika = models.BooleanField(default=False, null = True)
    palaiochora = models.BooleanField(default=False, null = True)
    agios_andreas = models.BooleanField(default=False, null = True)
    kastanitsa = models.BooleanField(default=False, null = True)
    sitaina = models.BooleanField(default=False, null = True)
    prastos = models.BooleanField(default=False, null = True)
    # date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nowakowski
    
class Noun(models.Model):
    paradigm = models.CharField(max_length=5, primary_key=True)
    gen_sing = models.CharField(max_length=20)
    plural = models.CharField(max_length=20) 
    source_id = models.ForeignKey(Source, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)

class Verb(models.Model):
    paradigm = models.CharField(max_length=5, primary_key=True)
    ending = models.CharField(max_length=20)
    orist_aoristos = models.CharField(max_length=20)
    ypot_aoristos = models.CharField(max_length=20)
    metochi = models.CharField(max_length=20)
    ypot_enestotas =  models.CharField(max_length=20)

class Adjective(models.Model):
    paradigm = models.CharField(max_length=5, primary_key=True)
    forms = models.CharField(max_length=50)

# To be added in text section:
# class Text(models.Model):
#     text = models.TextField()
#     title = models.CharField(max_length=200)
#     source_id = models.ForeignKey(Source, on_delete=models.CASCADE)
#     greek_translation = models.TextField()
#     english_translation = models.TextField()
#     notes = models.TextField()
