from django.db import models

# Create your models here.
class Source(models.Model):
    source_id = models.AutoField(primary_key=True, default=0)
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f'{self.title}'

class Entry(models.Model):
    nowakowski = models.CharField(max_length=50, primary_key=True)
    kostakis = models.CharField(max_length=50) 
    greek = models.CharField(max_length=200)
    paradigm = models.CharField(max_length=5)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    lemma = models.CharField(max_length=50)
    ipa = models.CharField(max_length=50)
    leonidio = models.BooleanField(default=False, blank=True)
    voskina = models.BooleanField(default=False)
    pragmateutis = models.BooleanField(default=False)
    sampatiki = models.BooleanField(default=False)
    livadi = models.BooleanField(default=False)
    tyros = models.BooleanField(default=False)
    melana = models.BooleanField(default=False)
    sapounakaiika = models.BooleanField(default=False)
    palaiochora = models.BooleanField(default=False)
    agios_andreas = models.BooleanField(default=False)
    kastanitsa = models.BooleanField(default=False)
    sitaina = models.BooleanField(default=False)
    prastos = models.BooleanField(default=False)
    # date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nowakowski
    
class NounParadigm(models.Model):
    paradigm = models.CharField(max_length=5, primary_key=True)
    gen_sing = models.CharField(max_length=20)
    plural = models.CharField(max_length=20) 
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.paradigm

class VerbParadigm(models.Model):
    paradigm = models.CharField(max_length=5, primary_key=True)
    ending = models.CharField(max_length=20)
    orist_aoristos = models.CharField(max_length=20)
    ypot_aoristos = models.CharField(max_length=20)
    metochi = models.CharField(max_length=20)
    ypot_enestotas =  models.CharField(max_length=20)

    def __str__(self):
        return f'{self.paradigm} - {self.ending}'

class AdjectiveParadigm(models.Model):
    paradigm = models.CharField(max_length=5, primary_key=True)
    forms = models.CharField(max_length=50)

    def __str__(self):
        return self.paradigm

# To be added in text section:
# class Text(models.Model):
#     text = models.TextField()
#     title = models.CharField(max_length=200)
#     source_id = models.ForeignKey(Source, on_delete=models.CASCADE)
#     greek_translation = models.TextField()
#     english_translation = models.TextField()
#     notes = models.TextField()
