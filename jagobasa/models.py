from django.db import models

# CATALOGO      Model representing a Catalochi
class Catalogo(models.Model):
    class Meta:
        ordering = ["-status", "id"]

    nome = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='jagobasa/static/img_catalogo', null=True, default = "")

    def __str__(self):
        return self.nome

# End CATALOGO      ===========================================================

# COLLEZIONE        Model representing a Collezione
class Collezione(models.Model):
    class Meta:
        ordering = ["-status", "nome"]

    nome = models.CharField(max_length=50)
    catalogo =  models.ManyToManyField(Catalogo, help_text="Select a catalogo for this collection")
    status = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='jagobasa/static/img_collezione')
    image_back = models.ImageField(upload_to='jagobasa/static/img_col_back', default ="")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('collezione-detail', args=[str(self.id)])

# End COLLEZIONE    ==========================================================

# TIPO        Model representing a Tipi dei prodotti
class Tipo(models.Model):
    class Meta:
        ordering = ["tipo"]

    tipo = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='jagobasa/static/img_tipi', default ="")
    ita = models.CharField(max_length=50, null=True)
    eng = models.CharField(max_length=50, null=True)
    rus = models.CharField(max_length=50, null=True)
    ukr = models.CharField(max_length=50, null=True)



    def __str__(self):
        return self.tipo

# End TIPO      ==========================================================

# PRODOTTO        Model representing a Prodotti
class Prodotto(models.Model):
    class Meta:
        ordering = ["nome"]

    nome = models.CharField(max_length=100)
    collezione = models.ForeignKey('Collezione', on_delete=models.SET_NULL, null=True)
    tipo = models.ManyToManyField(Tipo, help_text="Select a tipo for this prodotto")
    status = models.CharField(max_length=20, null=True)



    def __str__(self):
        return self.nome

# End PRODOTTO       ==========================================================

# PRODOTTO IMAGE        Model representing a Image dei Prodotti
class ProdottoImg(models.Model):
    class Meta:
        ordering = ["img_nome"]

    prodotto = models.ForeignKey('Prodotto', on_delete=models.SET_NULL, null=True)
    img_nome = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='jagobasa/static/img_prodotti')


    def __str__(self):
        return self.img_nome

# End PRODOTTO IMAGE      ==========================================================

# PRODOTTO DETTAGLI        Model representing a Dettagli dei Prodotti
class ProdottoDet(models.Model):
    class Meta:
        ordering = ["nome"]

    prodotto = models.ForeignKey('Prodotto', on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=20, blank=True, null=True)
    forma = models.CharField(max_length=5, blank=True, null=True)
    larghezza = models.IntegerField(blank=True, null=True)
    profondita = models.IntegerField(blank=True, null=True)
    altezza_min = models.IntegerField(blank=True, null=True)
    altezza_max = models.IntegerField(blank=True, null=True)
    catena = models.CharField(max_length=100, blank=True, null=True)
    materiale = models.CharField(max_length=100, blank=True, null=True)
    variante = models.TextField(max_length=1000, blank=True, help_text="", null=True)

    def __str__(self):
        return self.nome

# End PRODOTTO DETTAGLI      ==========================================================

# PRODOTTO LUCI        Model representing a Lampadine dei Prodotti
class ProdottoLuc(models.Model):
    class Meta:
        ordering = ["nome"]

    prodotto = models.ForeignKey('Prodotto', on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=20, blank=True, null=True)
    lampadina = models.CharField(max_length=50, null=True)
    quantita = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.nome

# End PRODOTTO LUCI      ==========================================================

# PRODOTTO SCHEDE        Model representing a Image dei Prodotti Schede

class ProdottoSchede(models.Model):
    class Meta:
        ordering = ["scheda_nome"]

    prodotto = models.ForeignKey('Prodotto', on_delete=models.SET_NULL, null=True)
    scheda_nome = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='jagobasa/static/img_schede')
    image_blanc = models.ImageField(upload_to='jagobasa/static/img_schede_blanche', null=True, default = "")


    def __str__(self):
        return self.scheda_nome

# End PRODOTTO SCHEDE      ==========================================================

# PROGETTO        Model representing a Image dei Progetti
class Progetto (models.Model):
    class Meta:
        ordering = ["nome"]

    prodotto = models.ManyToManyField(Prodotto, help_text="Scegli i progetti per questo prodotto")
    nome = models.CharField(max_length=100, null=True)
    stanza = models.ForeignKey('TipoStanza', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='jagobasa/static/img_progetti')
    testo = models.TextField(max_length=1000, blank=True, help_text="", null=True)


    # def __str__(self):
    #     return self.nome

# End PROGETTO     ==========================================================

# TIPO STANZA        Model representing a Tipi dei prodotti
class TipoStanza (models.Model):
    class Meta:
        ordering = ["nome"]

    nome = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='jagobasa/static/img_stanze', default ="")
    ita = models.CharField(max_length=100, null=True)
    eng = models.CharField(max_length=100, null=True)
    rus = models.CharField(max_length=100, null=True)
    ukr = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome

# End TIPO STANZA     ==========================================================
