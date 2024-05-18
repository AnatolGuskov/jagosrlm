from django.shortcuts import render
from django.views import generic
from ctypes  import *
import time




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
    nome_novita = ["LCS 045", "NCS 298/16", "NCL 187/Amber", "NCS 287/1", "NCS 143/2", "NCS 282/100", "NCS 496/4/90", "NCS 490/4/100"]
    prodotti_nov = []
    order = -1
    for novita in nome_novita:
        order += 1
        prod = Prodotto.objects.get(nome = novita)
        line = []
        images = ProdottoImg.objects.all().filter(prodotto = prod.id)
        line = line + [prod.id]                 #0 id
        line = line + [images[0].img_nome]      #1 nome_image
        path = str(images[0].image)
        path = path[path.find("static") + 7:]
        line = line + [path]                    #2 image_prodotto
        line = line + [images[0].prodotto]      #3 nome
        # line = line + [" "]  # 3 nome
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

# =============== Index TIPI =============
    tiplist = Tipo.objects.all().order_by('tipo')

    for tip in tiplist:
        tip.path = str(tip.image)
        tip.path = tip.path[tip.path.find("static")+7:]


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
                 'tiplist': tiplist,
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
                 'right_img': 'img_background/spazio 01 rose.jpg',
                 'right_text': "Collezioni",
                 'url_nome': 'collezione',
                                        }
    )
# ============== END collezione =======================

# ============== CATALOGO =============================
def catalogo(request):
    catlist = Catalogo.objects.all().order_by('status')
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


    prodotto = Prodotto.objects.all().filter(collezione = pk).order_by('-nome', 'status')
    prodotti = []
    prodotti_count = 0

    for prod in prodotto:
        prodotto_schede = ProdottoSchede.objects.filter(prodotto=prod.id)
        images = ProdottoImg.objects.all().filter(prodotto = prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto = prod.id).count()
        if image_count > 0: prodotti_count += 1
        for x in range (image_count):
            line = []
            line = line + [prod.id]                 # 0 id
            line = line + [images[x].img_nome]      # 1 image_nome
            path = str(images[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]                    # 2 image_prodotto

            if len(prodotto_schede) > 0:
                line = line + [str(images[x].prodotto) + " +scheda"]  # 3 nome prodotto
            else:
                line = line + [str(images[x].prodotto)]  # 3 nome prodotto

            line = line + [x + 1]                   # 4 numero image
            line = line + [image_count]             # 5 image_count
            line = line + [prod.collezione]         # 6 collezione
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

    prodotto = Prodotto.objects.all().filter(collezione=col).order_by('-nome', 'status')
    prodotti = []
    prodotti_count = 0

    for prod in prodotto:
        prodotto_schede = ProdottoSchede.objects.filter(prodotto=prod.id)
        images = ProdottoImg.objects.all().filter(prodotto=prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto=prod.id).count()
        if image_count > 0: prodotti_count += 1
        for x in range(image_count):
            line = []
            line = line + [prod.id]  # 0 id
            line = line + [images[x].img_nome]   # 1 nome_image
            path = str(images[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]                 # 2 image_prodotto

            if len(prodotto_schede) > 0:
                line = line + [str(images[x].prodotto) + " +scheda"]  # 3 nome prodotto
            else:
                line = line + [str(images[x].prodotto)]               # 3 nome prodotto

            line = line + [x + 1]                # 4 numero image
            line = line + [image_count]          # 5 image_count
            line = line + [prod.collezione]      # 6 collezione
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


    prodotto = Prodotto.objects.all().filter(tipo=pk).order_by('collezione', '-nome', )
    prodotti = []
    prodotti_count = 0

    for prod in prodotto:
        prodotto_schede = ProdottoSchede.objects.filter(prodotto=prod.id)
        images = ProdottoImg.objects.all().filter(prodotto=prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto=prod.id).count()
        if image_count > 0: prodotti_count += 1
        for x in range(image_count):
            line = []
            line = line + [prod.id]             # 0 id
            line = line + [images[x].img_nome]  # 1 image_nome
            path = str(images[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]                # 2 image_prodotto

            if len(prodotto_schede) > 0:
                line = line + [str(images[x].prodotto) + " +scheda"]  # 3 nome prodotto
            else:
                line = line + [str(images[x].prodotto)]               # 3 nome prodotto

            line = line + [x + 1]               # 4 numero image
            line = line + [image_count]         # 5 image_count
            line = line + [prod.collezione]     # 6 collezione
            prodotti = prodotti + [line]

    return render(
        request,
        'prodotti_coll_tipo_K.html',
        context={'prodotti': prodotti,
                 'tytle_nome': 'Prodotti di ',
                 'tipo_id': tipo.id,
                 'prodotti_count': prodotti_count,
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
    prodotto_nome = prodotto.nome
    collezione_nome = prodotto.collezione
    collezione = Collezione.objects.get(nome=collezione_nome)
    collezione_id = collezione.id
    prodotto_set = []
    right_img = ""
    right_text = ""

    if set != "2":   # da COLLEZIONE
        prodotto_set = Prodotto.objects.all().filter(collezione = collezione_id).order_by('-nome', 'status')
        set_data = Collezione.objects.get(nome = collezione_nome)
        set_data.path_back = str(set_data.image_back)
        set_data.path_back = set_data.path_back[set_data.path_back.find("static") + 7:]
        set_data.path_img = str(set_data.image)
        set_data.path_img = set_data.path_img[set_data.path_img.find("static") + 7:]
        right_img = set_data.path_img
        right_text = set_data.nome
        background = set_data.path_back

    if set == "2":   # da TIPO
        prodotto_set = Prodotto.objects.all().filter(tipo = url_id).order_by('-nome', 'status')
        set_data = Tipo.objects.get(id = url_id)
        set_data.path_img = str(set_data.image)
        set_data.path_img = set_data.path_img[set_data.path_img.find("static") + 7:]
        right_text = set_data.tipo
        right_img = set_data.path_img
        background = 'img_background/spazio 01 rose.jpg'
    #  ===================================
    prodotti = []
    prodotti_count = 0

    for prod in prodotto_set:
        prodotti_count = prodotti_count + 1
        images = ProdottoImg.objects.all().filter(prodotto=prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto=prod.id).count()
        prodotto_schede = ProdottoSchede.objects.filter(prodotto=prod.id)

        for x in range(image_count):
            line = []
            line = line + [prod.id]             # 0 id
            line = line + [images[x].img_nome]  # 1 image_nome
            path = str(images[x].image)
            path = path[path.find("static") + 7:]
            line = line + [path]                # 2 image_prodotto

            if len(prodotto_schede) > 0:
                line = line + [str(images[x].prodotto) + " +scheda"]  # 3 nome prodotto
            else:
                line = line + [str(images[x].prodotto)]        # 3 nome prodotto

            line = line + [x + 1]               # 4 numero image
            line = line + [image_count]         # 5 image_count
            line = line + [prod.collezione]     # 6 collezione
            prodotti = prodotti + [line]

    #  ===================================
    images = ProdottoImg.objects.all().filter(prodotto = pk)
    images_count = ProdottoImg.objects.all().filter(prodotto = pk).count()
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
    variante = ""

    prodotto_det = ProdottoDet.objects.all().filter(nome = prodotto.nome)
    if prodotto_det:
        for pro in prodotto_det:
            if pro.forma: pro.forma = pro.forma
            else: pro.forma = ""
            if pro.profondita:
                misura = str(pro.forma) + " " + str(pro.larghezza) + " x " + str(pro.profondita) + " mm"
            else:
                misura = str(pro.forma) + " " + str(pro.larghezza) + " mm"
            if pro.altezza_min:
                altezza = "h= " + str(pro.altezza_min) + " ... " + str(pro.altezza_max) + " mm"
            else:
                altezza = "h= " + str(pro.altezza_max) + " mm"
            if pro.catena:
                altezza = altezza + " + " + str(pro.catena)
            if pro.materiale and pro.materiale != "-":
                materiale = str(pro.materiale)
            else:materiale = ""
            variante = pro.variante


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
    for prog in prodotto_progetti:
        prog.path = str(prog.image)
        prog.path = prog.path[prog.path.find("static")+7:]
        menu = prog.nome.split()
        prog.menu = menu[0] + " " + menu[1]

    return render(
        request,
        'prodotto_K.html',
        context={'collezione': set_data,  # set
                 'prodotti': prodotti,  # set user
                 'prodotto_progetti': prodotto_progetti,  # set
                 'prodotti_count': prodotti_count, 'images_count': images_count,
                 'prodotto': prodotto, # set
                 'prod_images': images,  # set
                 'background': background,
                 'prodotto_nome': prodotto_nome,
                 'collezione_nome': collezione_nome, 'collezione_id': collezione_id,
                 'right_img': right_img,  'right_text': right_text,
                 'tipi': tipi, # set
                 'misura': misura, 'altezza': altezza,  'materiale': materiale,
                 'variante': variante,
                 'prodotto_luc': prodotto_luc,  # set
                 'set': set,
                 'url_id': url_id, 'tipo_id': url_id,
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

    progettolist = Progetto.objects.all()

    for prog in progettolist:
        prog.path = str(prog.image)
        prog.path = prog.path[prog.path.find("static") + 7:]
        menu = prog.nome.split()
        prog.menu = menu[0] + " " + menu[1]

    prodotti = Progetto.objects.get(pk = pk).prodotto.all().order_by("-nome")  # ManyToMany Tutti Prodotti per Progetto !!!!!!!!!!!!!

    prod_images = []
    for prod in prodotti:
        line = []
        images = ProdottoImg.objects.all().filter(prodotto=prod.id)
        prod.path = str(images[0].image)
        prod.path = prod.path[prod.path.find("static") + 7:]
        line = line + [prod.id]           # 0 id
        line = line + [prod.path]         # 1 nome imace
        line = line + [prod.nome]         # 2 nome prodotto
        prod_images = prod_images + [line]


    num_progetti = Progetto.objects.all().count()

    stanza_progetto = TipoStanza.objects.get(nome = stanza)
    stanza_id = stanza_progetto.id

    return render(
        request,
        'progetto_K.html',
        context={'progetto_nome': progetto.menu,
                 'progetto_stanza': progetto.stanza,
                 'progetto': progetto,    #set
                 'prod_images': prod_images,
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

    return render(
        request,
        'progetto_list_K.html',
        context={                       }
    )
# ============== END progetti =======================


# ============== ELENCO ===========================
def elenco(request, sort, coll_pk):
    start_time = time.time()
    if coll_pk == "100":
        prodotto = Prodotto.objects.all()
        right_img = 'img_background/spazio 01 rose.jpg'
        right_text = "Prodotti"
        coll_id = int(coll_pk)
    else:
        prodotto = Prodotto.objects.all().filter(collezione = coll_pk)
        coll_fix = Collezione.objects.get(pk = coll_pk)
        right_img = str(coll_fix.image)
        right_img = right_img[right_img.find("static") + 7:]
        right_text = coll_fix.nome
        coll_id = int(coll_pk)

    prodotto_count = prodotto.count()

    if sort == '1':
        prodotto = prodotto.order_by('collezione','nome')
    if sort == '2':
        prodotto = prodotto.order_by('nome')
    if sort == '3':
        prodotto = prodotto.order_by('tipo',)

    #  ===================================
    prodotti = []

    for prod in prodotto:
        images = ProdottoImg.objects.all().filter(prodotto=prod.id)
        image_count = ProdottoImg.objects.all().filter(prodotto=prod.id).count()
        coll = Collezione.objects.get(nome=prod.collezione)
        #  ===================================
        line = []
        # 0 id
        line = line + [prod.id]
        # 1 nome_prod
        line = line + [prod.nome]
        # 2 nome_coll
        line = line + [coll.nome]
        if image_count > 0: path = str(images[0].image_ico)
        path = path[path.find("static") + 7:]
        # 3 image_prodotto
        line = line + [path]
        #  ===================================
        detagli = ProdottoDet.objects.all().filter(prodotto=prod.id)

        line = line + [detagli[0].messura]             # 4 misura

        line = line + [detagli[0].altezza]           # 5 altezza
        if detagli[0].materiale and detagli[0].materiale != "-": materiale = str(detagli[0].materiale)
        else: materiale = ""
        line = line + [materiale]         # 6 materiale
        line = line + ["'"]               # 7 variante
        #  ===================================
        luci = ProdottoLuc.objects.all().filter(prodotto=prod.id)
        luc_tip = ""
        for luc in luci:
            if luc_tip == "": luc_tip = luc_tip + str(luc.quantita)+"x "+str(luc.lampadina)
            else: luc_tip = luc_tip + ", " + str(luc.quantita) + "x " + str(luc.lampadina)
        line = line + [luc_tip]            # 8 luci

        line = line + [coll.id]            # 9 id_coll
        tipi = Prodotto.objects.get(id = prod.id).tipo.all() # ManyToMany Tutti Tipi per Prodotto !!!!!!!!!!!!!
        tipo = tipi[0].tipo
        tipo = tipo.title()
        line = line + [tipo]       # 10 tipo di prodotti
        #  ===================================
        prodotti = prodotti + [line]
        #  ===================================
        collist = Collezione.objects.all()

        end_time = time.time()
        time_elenco = end_time - start_time
        time_elenco = str(time_elenco)
        time_elenco = time_elenco[:6]
    return render(
        request,
        'elenco_K.html',
        context={
            'prodotti': prodotti,
            'prodotto_count': prodotto_count,
            'collist': collist,
            'coll_pk': coll_pk                                                                                                       ,
            'right_img': right_img, 'right_text': right_text,
            'time_elenco': time_elenco,
        }
    )
# ============== END ELENCO_ =======================


# ============== Elenco_ ?????? service ===========================
def elenco_1 (request):

    return render(
        request,
        'progetto_list_K.html',
        context={  }
    )
# ============== END elenco_ =======================

def elenco_2 (request, sort):

    return render(
        request,
        'progetto_list_K.html',
        context={  }
    )
# ============== END elenco_ =======================
