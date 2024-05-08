from django.contrib import admin

from .models import (Catalogo, Collezione, Tipo, Prodotto,
                     ProdottoImg, ProdottoDet, ProdottoLuc, ProdottoSchede,
                     Progetto, TipoStanza)

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


#========================== COLLEZIONE ==============================
class CollezioneResource(resources.ModelResource):

   class Meta:
       model = Collezione

class CollezioneAdmin(ImportExportActionModelAdmin):
    resourse_class = CollezioneResource
    list_display = ('id', 'nome', 'status', 'image', )
    list_filter = ('catalogo', )

admin.site.register(Collezione, CollezioneAdmin)

#========================= Collezione ===================================
#========================= CATALOGO ===================================
class CatalogoResource(resources.ModelResource):

    class Meta:
        model = Catalogo

class CatalogoAdmin(ImportExportActionModelAdmin):
    resourse_class = CatalogoResource
    list_display = ('id', 'nome', 'status', 'image',)

admin.site.register(Catalogo, CatalogoAdmin)


#========================= Catalogo ===================================
# ======================== TIPO =======================================
class TipoResource(resources.ModelResource):

   class Meta:
       model = Tipo

class TipoAdmin(ImportExportActionModelAdmin):
    resourse_class = TipoResource
    list_display = ('id', 'tipo', 'image', 'ita', 'eng', 'rus', )

admin.site.register(Tipo, TipoAdmin)

#========================= Tipo ===================================
# ======================== PRODOTTO =======================================
class ProdottoResource(resources.ModelResource):

   class Meta:
       model = Prodotto

class ProdottoAdmin(ImportExportActionModelAdmin):
    resourse_class = ProdottoResource
    list_display = ('id', 'nome', 'collezione', 'preise',)
    list_filter = ('collezione', 'tipo', 'status',)

admin.site.register(Prodotto, ProdottoAdmin)

#========================= Prodotto ===================================
#========================== PRODOTTOIMG ==============================
class ProdottoImgResource(resources.ModelResource):

   class Meta:
       model = ProdottoImg

class ProdottoImgAdmin(ImportExportActionModelAdmin):
    resourse_class = ProdottoImgResource
    list_display = ('id', 'img_nome', 'image',)
    # list_filter = ('catalogo', )

admin.site.register(ProdottoImg, ProdottoImgAdmin)

#========================== Prodottoimg ==============================
#========================== PRODOTTODET ==============================
class ProdottoDetResource(resources.ModelResource):

   class Meta:
       model = ProdottoDet

class ProdottoDetAdmin(ImportExportActionModelAdmin):
    resourse_class = ProdottoDetResource
    list_display = ('id', 'nome', 'prodotto', 'larghezza', 'profondita', 'altezza_max', 'materiale')
    # list_filter = ('catalogo', )

admin.site.register(ProdottoDet, ProdottoDetAdmin)

#========================== ProdottoDet ==============================
#========================== PRODOTTO SCHEDE ==============================
class ProdottoSchedeResource(resources.ModelResource):

   class Meta:
       model = ProdottoSchede

class ProdottoSchedeAdmin(ImportExportActionModelAdmin):
    resourse_class = ProdottoSchedeResource
    list_display = ('id', 'prodotto', 'scheda_nome', 'image', 'image_blanc')
    # list_filter = ('prodotto', )

admin.site.register(ProdottoSchede, ProdottoSchedeAdmin)

#========================== Prodotto SCHRDE ==============================

#========================== PRODOTTO LUCI ==============================
class ProdottoLucResource(resources.ModelResource):

   class Meta:
       model = ProdottoLuc

class ProdottoLucAdmin(ImportExportActionModelAdmin):
    resourse_class = ProdottoLucResource
    list_display = ('id', 'nome', 'prodotto', 'lampadina', 'quantita',)
    # list_filter = ('prodotto', )

admin.site.register(ProdottoLuc, ProdottoLucAdmin)

#========================== Prodotto LUCI ==============================

#========================== PROGETTO ==============================
class ProgettoResource(resources.ModelResource):

   class Meta:
       model = Progetto

class ProgettoAdmin(ImportExportActionModelAdmin):
    resourse_class = ProgettoResource
    list_display = ('id', 'nome', 'stanza', 'status', 'testo', 'image',)
    list_filter = ('stanza', )

admin.site.register(Progetto, ProgettoAdmin)

#========================== Progetto ==============================

#========================== TIPO STANZA ==============================
class TipoStanzaResource(resources.ModelResource):

   class Meta:
       model = TipoStanza

class TipoStanzaAdmin(ImportExportActionModelAdmin):
    resourse_class = TipoStanzaResource
    list_display = ('id', 'nome', 'image', 'ita', 'eng', 'rus',)


admin.site.register(TipoStanza, TipoStanzaAdmin)

#========================== Tipo Stanza ==============================



