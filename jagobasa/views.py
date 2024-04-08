from django.shortcuts import render
from django.views import generic
from ctypes  import *




from .models import (Catalogo, Collezione, Tipo, Prodotto,
                     ProdottoImg, ProdottoDet, ProdottoLuc, ProdottoSchede,
                     Progetto, TipoStanza)



# ============== INDEX =============================
def index(request):
# =============== Index Quantita =============
    num_catalogo = Catalogo.objects.all().count()
    num_collezione = Collezione.objects.all().count()
    num_prodotto = Prodotto.objects.all().count()
    num_images_prod = ProdottoImg.objects.all().filter(image__isnull=False).count()
    num_tipi = Tipo.objects.all().count()
    num_progetto = Progetto.objects.all().count()
    num_images = num_collezione + num_images_prod + num_progetto

#=============== Index Novita =============
    novita = Prodotto.objects.all().filter(status = "Novita")
    novita_count = Prodotto.objects.all().filter(status = "Novita").count()
    prodotti_nov = []
    for prod in novita:
        line = []
        images = ProdottoImg.objects.all().filter(prodotto = prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto = prod.id).count()
        for x in range (image_count):
            line = line + [prod.id]                 #0 id
            line = line + [images[x].img_nome]      #1 nome_image
            path = str(images[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]                    #2 image_prodotto
            line = line + [images[x].prodotto]      #3 nome
            line = line + [prod.collezione]         #4 collezione
            prodotti_nov = prodotti_nov + [line]

# =============== Index Collezione Slide =============
    collezionelist = Collezione.objects.all().filter(status__contains="Home").order_by('status')
    i = 0
    for coll in collezionelist:
        coll.path = str(coll.image_back)
        coll.path = coll.path[coll.path.find("static")+7:]
        i += 1
        coll.slide = i

# =============== Index Collezione Tutti =============
    collezioni_tutti = Collezione.objects.all().order_by('nome')

    for coll in collezioni_tutti:
        coll.path = str(coll.image)
        coll.path = coll.path[coll.path.find("static")+7:]


# =============== Index Progetti =============
    progettolist = Progetto.objects.all().filter(status__contains="Home").order_by('status')

    for prog in progettolist:
        prog.path = str(prog.image)
        prog.path = prog.path[prog.path.find("static")+7:]

# =============== Index Cataloghi =============
    catalogolist = Catalogo.objects.all().filter(status__contains="Home").order_by('status')
    catalogo_colllist = []
    for cata in catalogolist:
        cata.path = str(cata.image)
        cata.path = cata.path[cata.path.find("static") + 7:]
        collist = Collezione.objects.all().filter(catalogo = cata.id)
        cata.num_coll = Collezione.objects.all().filter(catalogo = cata.id).count()
        if cata.num_coll > 20: y = 20
        else: y = cata.num_coll
        for x in range(y):
            line = []
            line = line + [cata.nome]                 # 0 catalogo
            line = line + [collist[x].id]             # 1 id_collezione
            line = line + [collist[x].nome]           # 2 nome_collezione
            path = str(collist[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]                      # 3 image_collezione
            catalogo_colllist = catalogo_colllist + [line]


# =============== Render INDEX =============
    return render(
        request,
        'index_K.html',
        context={'num_cata': num_catalogo,
                 'num_coll': num_collezione,
                 'num_prod': num_prodotto,
                 'num_tipi': num_tipi,
                 'num_imag': num_images,
                 'num_prog': num_progetto,
                 'novita': prodotti_nov, 'novita_count': novita_count,
                 'progettolist': progettolist,
                 'collezionelist': collezionelist,
                 'collezioni_tutti': collezioni_tutti,
                 'catalogolist': catalogolist, 'catalogo_colllist': catalogo_colllist,
                 # 'width': width, 'height': height,
                 'modo': "mobil1",

                 }
    )
# ============== end INDEX =============================

# ============== COLLEZIONE =============================
def collezione(request):
    collist = Collezione.objects.all().order_by('nome')
    num_collezione = Collezione.objects.all().count()

    for col in collist:
        col.path = str(col.image)
        col.path = col.path[col.path.find("static")+7:]



    return render(
        request,
        'collezione_list_K.html',
        context={'collist': collist,
                 'num_collezione': num_collezione,
                 'tytle_nome': 'Collezioni',
                 'right_img': 'img_background/collezione_spazio 01 rose.jpg',
                 'right_text': "Collezioni",
                 'url_nome': 'collezione',
                                        }
    )
# ============== END collezione =======================

# ============== CATALOGO =============================
def catalogo(request):
    catlist = Catalogo.objects.all().order_by('nome')
    num_catalogo = Catalogo.objects.all().count()

    for cat in catlist:
        cat.path = str(cat.image)
        cat.path = cat.path[cat.path.find("static")+7:]

    return render(
        request,
        'catalogo_list_K.html',
        context={'catlist': catlist,
                 'num_catalogo': num_catalogo,
                 }
    )
# ============== END catalogo =======================

# ============== TIPO =============================
def tipo(request):
    tiplist = Tipo.objects.all().order_by('tipo')

    for tip in tiplist:
        tip.path = str(tip.image)
        tip.path = tip.path[tip.path.find("static")+7:]

    num_tipi = Tipo.objects.all().count()

    return render(
        request,
        'tipo_list_K.html',
        context={'tiplist': tiplist,  #set
                 'num_tipi': num_tipi,
                                        }
    )
# ============== END tipo =======================

# ============== COLLEZIONE Detail =============================

def collezione_detail(request, pk):

    collezione = Collezione.objects.get(pk = pk)
    collezione.img_back = str(collezione.image_back)
    collezione.img_back = collezione.img_back[collezione.img_back.find("static") + 7:]
    collezione.img = str(collezione.image)
    collezione.img = collezione.img[collezione.img.find("static") + 7:]

    cataloghi = Collezione.objects.get(pk = pk).catalogo.all()
    catalogo_pk = cataloghi[0].pk


    prodotto = Prodotto.objects.all().filter(collezione = pk)
    prodotti = []
    prodotti_count = 0

    for prod in prodotto:
        prodotti_count += 1
        line = []
        images = ProdottoImg.objects.all().filter(prodotto = prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto = prod.id).count()
        for x in range (image_count):
            line = line + [prod.id]                 #0 id
            line = line + [images[x].img_nome]      #1 nome_image
            path = str(images[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]                    #2 image_prodotto
            line = line + [images[x].prodotto]      #3 nome
            prodotti = prodotti + [line]


    return render(
        request,
        'prodotti_coll_tipo_K.html',
        context={'collezione': collezione,  #set
                 'collezione_id': pk, 'catalogo_id': catalogo_pk, 'url_id': pk,
                 'prodotti': prodotti,
                 'prodotti_count': prodotti_count,
                 'background': collezione.img_back,
                 'tytle_nome': 'Collezione ',
                 'right_img': collezione.img,
                 'right_text': collezione.nome,
                 'nome_url': 'collezione',
                 'set': '1', 'tipo_id': 1,
                 'catalogo_ind': "0",
                 }
    )
# ============== END Collezione Detail =============================

# ============== CATALOGO Detail =============================

def catalogo_detail(request, pk):

    catalogo = Catalogo.objects.get(id = pk)
    catalogo.img = str(catalogo.image)
    catalogo.img = catalogo.img[catalogo.img.find("static") + 7:]
    catalogo_pk = pk

    collist = Collezione.objects.all().filter(catalogo = pk)
    num_collezione = 0
    for col in collist:
        num_collezione += 1
        col.path = str(col.image)
        col.path = col.path[col.path.find("static")+7:]

    return render(
        request,
        'collezione_list_K.html',
        context={'collist': collist,
                 'num_collezione': num_collezione,
                 'tytle_nome': 'Collezioni di ',
                 'right_img': catalogo.img,
                 'right_text': catalogo.nome,
                 'url_nome': 'catalogo',
                 'catalogo_pk': catalogo_pk,
                 }

    )

# ============== END Catalogo Detail =============================

# ============== CATALOGO Detail Collezione =============================

def catalogo_detail_collezione(request, pk, col):

    catalogo = Catalogo.objects.get(pk = pk)
    catalogo.img = str(catalogo.image)
    catalogo.img = catalogo.img[catalogo.img.find("static") + 7:]
    catalogo_pk = pk

    collezione = Collezione.objects.get(pk=col)
    collezione.img_back = str(collezione.image_back)
    collezione.img_back = collezione.img_back[collezione.img_back.find("static") + 7:]
    collezione.img = str(collezione.image)
    collezione.img = collezione.img[collezione.img.find("static") + 7:]
    collezione_id = collezione.pk

    prodotto = Prodotto.objects.all().filter(collezione=col)
    prodotti = []
    prodotti_count = 0

    for prod in prodotto:
        prodotti_count += 1
        line = []
        images = ProdottoImg.objects.all().filter(prodotto=prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto=prod.id).count()
        for x in range(image_count):
            line = line + [prod.id]  # 0 id
            line = line + [images[x].img_nome]  # 1 nome_image
            path = str(images[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]  # 2 image_prodotto
            line = line + [images[x].prodotto]  # 3 nome
            prodotti = prodotti + [line]

    return render(
        request,
        'prodotti_coll_tipo_K.html',
        context={'collezione': collezione,  #set
                 'collezione_id': collezione_id,
                 'catalogo_id': catalogo_pk, 'url_id': catalogo_pk,
                 'prodotti': prodotti,
                 'prodotti_count': prodotti_count,
                 'background': collezione.img_back,
                 'tytle_nome': 'Prodotti di ',
                 'right_img': collezione.img,
                 'right_text': collezione.nome,
                 'nome_url': 'catalogo_detail',
                 'catalogo_ind': "1",
                 'set': '3', 'tipo_id': 1,
                 }

    )

# ============== END Catalogo Detail Collezione=============================


# ============== TIPI DETAIL =============================

def tipo_detail(request, pk ):

    tipo = Tipo.objects.get(pk = pk)
    tipo.img = str(tipo.image)
    tipo.img = tipo.img[tipo.img.find("static") + 7:]


    prodotto = Prodotto.objects.all().filter(tipo=pk)
    prodotti = []
    prodotti_count = 0

    for prod in prodotto:
        prodotti_count += 1
        line = []
        images = ProdottoImg.objects.all().filter(prodotto=prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto=prod.id).count()
        for x in range(image_count):
            line = line + [prod.id]             # 0 id
            line = line + [images[x].img_nome]  # 1 nome_image
            path = str(images[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]                # 2 image_prodotto
            line = line + [images[x].prodotto]  # 3 nome
            prodotti = prodotti + [line]

    return render(
        request,
        'prodotti_coll_tipo_K.html',
        context={'prodotti': prodotti,
                 'prodotti_count': prodotti_count,
                 'background': 'img_background/tipo_spazio 03 blackblu.jpg',
                 'tytle_nome': 'Prodotti di ',
                 'right_img': tipo.img,
                 'right_text': tipo.tipo,
                 'nome_url': 'tipo',
                 'set': '2',
                 'tipo_id': tipo.id, 'url_id': tipo.id,
                 'catalogo_ind': "0",
                 }
    )

# ============== END Tipi Detail =============================

# ============== PRODOTTO =============================

def prodotto(request, pk, set, url_id):

    prodotto = Prodotto.objects.get(id = pk)
    prod_nome = prodotto.nome
    collezione_id = prodotto.collezione
    prodotto_set = []
    right_img = ""
    right_text = ""
    # background = "3"

    if set != "2":   # da COLLEZIONE
        prodotto_set = Prodotto.objects.all().filter(collezione = collezione_id)
        set_data = Collezione.objects.get(nome = collezione_id)
        set_data.path_back = str(set_data.image_back)
        set_data.path_back = set_data.path_back[set_data.path_back.find("static") + 7:]
        set_data.path_img = str(set_data.image)
        set_data.path_img = set_data.path_img[set_data.path_img.find("static") + 7:]
        right_img = set_data.path_img
        right_text = set_data.nome
        background = set_data.path_back

    if set == "2":   # da TIPO
        prodotto_set = Prodotto.objects.all().filter(tipo = url_id)
        set_data = Tipo.objects.get(id = url_id)
        set_data.path_img = str(set_data.image)
        set_data.path_img = set_data.path_img[set_data.path_img.find("static") + 7:]
        right_text = set_data.tipo
        right_img = set_data.path_img
        background = 'img_background/tipo_spazio 03 blackblu.jpg'
    #  ===================================
    prodotti = []
    prodotti_count = 0

    for prod in prodotto_set:
        prodotti_count = prodotti_count + 1
        line = []
        images = ProdottoImg.objects.all().filter(prodotto=prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto=prod.id).count()
        for x in range(image_count):
            line = line + [prod.id]             # 0 id
            line = line + [images[x].img_nome]  # 1 nome_image
            path = str(images[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]                # 2 image_prodotto
            line = line + [images[x].prodotto]  # 3 nome
            prodotti = prodotti + [line]

    #  ===================================
    images = ProdottoImg.objects.all().filter(prodotto = pk)
    for img in images:
        img.path = str(img.image)
        img.path = img.path[img.path.find("static") + 7:]
        prod_nome = img.img_nome

    #  ===================================
    tipi = Prodotto.objects.get(id = pk).tipo.all() # ManyToMany Tutti Tipi per Prodotto !!!!!!!!!!!!!
    for tip in tipi:
        tip_split = tip.tipo.split()
        if len(tip_split) != 1:
            tip.tipo = tip.tipo[len(tip_split[0]):]

    #  ===================================
    misura = "-"
    altezza = "-"
    materiale = "-"

    prodotto_det = ProdottoDet.objects.all().filter(nome = prodotto.nome)
    if prodotto_det:
        for pro in prodotto_det:
            if pro.profondita:
                misura = str(pro.forma) + " " + str(pro.larghezza) + " x " + str(pro.profondita) + " mm"
            else:
                misura = str(pro.forma) + " " + str(pro.larghezza) + " mm"
            if pro.altezza_min:
                altezza = "H = " + str(pro.altezza_min) + " ... " + str(pro.altezza_max) + " mm"
            else:
                altezza = "H = " + str(pro.altezza_max) + " mm"
            if pro.catena:
                altezza = altezza + " + " + str(pro.catena)
            if pro.materiale:
                materiale = str(pro.materiale)


    #  ===================================
    prodotto_luc = ProdottoLuc.objects.all().filter(nome=prodotto.nome)

    #  ===================================
    prodotto_schede = ProdottoSchede.objects.filter(prodotto=pk)
    img_scheda = None
    if len(prodotto_schede) > 0:
        img_scheda = str(prodotto_schede[0].image)
        img_scheda = img_scheda[img_scheda.find("static") + 7:]

    #  ===================================
    # if Prodotto.objects.get(id=pk).progetto.all():
    prodotto_progetti = Progetto.objects.all().filter(prodotto = pk)

    return render(
        request,
        'prodotto_K.html',
        context={'collezione': set_data,  # set
                 'prodotti': prodotti,  # set user
                 'prodotto_progetti': prodotto_progetti,  # set
                 'prodotti_count': prodotti_count,
                 'prodotto': prodotto, # set
                 'prod_images': images,  # set
                 'background': background,
                 'prod_nome': prod_nome,
                 'right_img': right_img,
                 'right_text': right_text,
                 'tipi': tipi, # set
                 'misura': misura, 'altezza': altezza,  'materiale': materiale,
                 'prodotto_luc': prodotto_luc,  # set
                 'set': set,
                 'url_id': url_id,
                 'img_scheda': img_scheda,

                 }
    )
# ============== END Prodotto =============================

# ============== PROGETTI =============================
def progetto(request, stanza):

    if stanza != '0':
        stanza_id = int(stanza)
        progettolist = Progetto.objects.all().filter(stanza = stanza_id).order_by('nome')
        num_progetti = Progetto.objects.all().filter(stanza = stanza_id).count()
        text_count = "Progetti di " + str(progettolist[0].stanza)
    else:
        progettolist = Progetto.objects.all().order_by('nome')
        num_progetti = Progetto.objects.all().count()
        text_count = "Progetti"

    for prog in progettolist:
        prog.path = str(prog.image)
        prog.path = prog.path[prog.path.find("static")+7:]
        menu = prog.nome.split()
        prog.menu = menu[0] + " " + menu[1]


    stanzalist = TipoStanza.objects.all()
    for stanza in stanzalist:
        stanza.num_prog = Progetto.objects.all().filter(stanza = stanza.id).count()



    return render(
        request,
        'progetto_list_K.html',
        context={'progettolist': progettolist,  #set
                 'progetto_nome': progettolist[0].menu,
                 'num_progetti': num_progetti,
                 'text_count': text_count,
                 'stanzalist': stanzalist,
                 'modo': 1,
                 'stanza': stanza,

                                        }
    )
# ============== END progetti =======================

# ============== PROGETTO DETAIL =============================

def progetto_detail(request, stanza, pk ):

    progetto = Progetto.objects.get(id = pk)
    progetto.path = str(progetto.image)
    progetto.path = progetto.path[progetto.path.find("static") + 7:]
    menu = progetto.nome.split()
    progetto.menu = menu[0] + " " + menu[1]

    # progetto_nome = progetto[0].nome

    progettolist = Progetto.objects.all()

    for prog in progettolist:
        prog.path = str(prog.image)
        prog.path = prog.path[prog.path.find("static") + 7:]
        menu = prog.nome.split()
        prog.menu = menu[0] + " " + menu[1]

    prodotti = Progetto.objects.get(pk = pk).prodotto.all()  # ManyToMany Tutti Prodotti per Progetto !!!!!!!!!!!!!

    num_progetti = Progetto.objects.all().count()

    stanza_progetto = TipoStanza.objects.get(nome = stanza)
    stanza_id = stanza_progetto.id

    return render(
        request,
        'progetto_K.html',
        context={'progetto_nome': progetto.menu,
                 'progetto_stanza': progetto.stanza,
                 'progetto': progetto,    #set
                 'progetto_id': stanza,
                 'stanza_id': stanza_id,
                 'text_count': "Progetti totali",
                 'num_progetti': num_progetti,
                 'progettolist': progettolist,
                 'prodotti': prodotti,  #set
                 'modo': 2,

                 }
    )

# ============== END Progetto Detail =============================

# ============== PROGETTI ==??????===========================
def progetto_(request):
    progettolist = Progetto.objects.all().order_by('nome')

    for prog in progettolist:
        prog.path = str(prog.image)
        prog.path = prog.path[prog.path.find("static")+7:]

    num_progetti = Progetto.objects.all().count()

    return render(
        request,
        'progetto_list_K.html',
        context={'progettolist': progettolist,  #set
                 'num_progetti': num_progetti,
                 'modo': 1,

                                        }
    )
# ============== END progetti =======================

