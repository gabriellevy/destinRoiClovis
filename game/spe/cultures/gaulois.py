from abs.univers import culture
from abs.humanite import metier
from abs.humanite import trait
# from extremis.geographie import quartier
import random

class Gaulois(culture.Culture):

    NOM = u"Gaulois"
    ID = u"gaulois"

    def __init__(self):
        self.nom_ = Gaulois.NOM
        self.id_ = Gaulois.ID
        # self.quartier_ = quartier.SaintDenis.NOM

    def GetGentile(self, masculin):
        if masculin:
            return "gaulois"
        else:
            return "gauloise"

    def GetPoidsDemo(self):
        """
        à quel point cette coterie est nombreuse dans la population
        1.0 = normal
        0.1 = 10 fois moins que la moyenne
        """
        return 0.3

    def CreerNom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        return random.choice(Gaulois.NOMS)

    def CreerPrenom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        if masculin:
            return random.choice(Gaulois.PRENOMS_M)
        else:
            return random.choice(Gaulois.PRENOMS_F)

    NOMS = []

    PRENOMS_M = [
    u"Acedillus", u"Acedilu", u"Adbitus", u"Adcanaunos", u"Adcomaros", u"Adebugi", u"Adebugius", u"Adgennus", u"Adgenus", u"Adginnius",
    u"Adiatorix", u"Adiatumarus", u"Adietuanus", u"Adietumarus", u"Admatius", u"Adnamati", u"Adnamatius", u"Adnamatus", u"Adretilis",
    u"Adrotus", u"Advorix", u"Aesarius", u"Agedilicus", u"Agedilio", u"Agedilios", u"Agedilli", u"Agedillus", u"Agedovirus", u"Agisilius",
    u"Agisillus", u"Aicovindo", u"Aisus", u"Albic", u"Albius", u"Albus", u"Alebece", u"Allecnus", u"Allinus", u"Allobroxus", u"Allovico",
    u"Alluci", u"Allucius", u"Alpius", u"Alpus", u"Ambadus", u"Ambaxius", u"Ambilli", u"Ambillus", u"Ambilo", u"Ambilos", u"Ambimogidus",
    u"Ambisauus", u"Ambisavus", u"Ambudsuilus", u"Andangi", u"Andecarius", u"Andecarus", u"Andegalli", u"Andegasi", u"Andegasus", u"Andereseni",
    u"Andergi", u"Andergos", u"Andolatius", u"Andosion", u"Andosten", u"Andosteni", u"Andosteno", u"Andoston", u"Andreine", u"Anducor",
    u"Annamatus", u"Annamoris", u"Annamus", u"Antedrigus", u"Anteremius", u"Areobindus", u"Arimanus", u"Ateano", u"Atecilus", u"Atecurus",
    u"Ategnutis", u"Atepatus", u"Atepiccus", u"Ateponirus", u"Ateponius", u"Ateponus", u"Ateratos", u"Atesios", u"Atesmertus", u"Atesos",
    u"Atessatis", u"Atesso", u"Atestas", u"Ateuritus", u"Atgite", u"Atolisus", u"Atporix", u"Atrectius", u"Atrectus", u"Atregtius", u"Atrextus",
    u"Atrixtos", u"Attectius", u"Atuirus", u"Atusonius", u"Audatus", u"Audeti", u"Audoenus", u"Audoti", u"Aventinius", u"Aventinus", u"Balaesus",
    u"Balatonux", u"Balorix", u"Banni", u"Bannio", u"Banu", u"Banui", u"Banuillus", u"Banuo", u"Banuus", u"Bellognatus", u"Bilicedo", u"Biliureto",
    u"Billiccissioni", u"Billicedo", u"Birucatus", u"Bocontius", u"Bodenia", u"Bodocenos", u"Bodocenus", u"Boduogenus", u"Bogionius", u"Borili",
    u"Borillus", u"Boritus", u"Borso", u"Borsus", u"Boruonicus", u"Borvonicus", u"Boudillus", u"Bravecci", u"Brigomaglos", u"Britomartis",
    u"Britomartus", u"Brocchus", u"Broccius", u"Broccus", u"Bussumarius", u"Bussumarus", u"Busturo", u"Butiro", u"Buturo", u"Cabriabantos",
    u"Cabrus", u"Caccuso", u"Cacurio", u"Cacurius", u"Cambo", u"Cambulus", u"Cambus", u"Camerianus", u"Camerinus", u"Camulatucus", u"Camulixus",
    u"Camulorigi", u"Caracco", u"Caracus", u"Caraddounius", u"Caraddounus", u"Caramantius", u"Carantacus", u"Carantillo", u"Caranto", u"Carantorius",
    u"Carasius", u"Carathounus", u"Caratillus", u"Caratodius", u"Cariaus", u"Carigo", u"Carigus", u"Carino", u"Carisianus", u"Caritosus", u"Carix",
    u"Caromarus", u"Carominius", u"Carucenus", u"Carugenus", u"Carulirus", u"Cassicius", u"Cassicus", u"Cassitalus", u"Cassutus", u"Castonius",
    u"Catabar", u"Catacius", u"Catacus", u"Catamandus", u"Catamanus", u"Catavignus", u"Caterto", u"Cathirix", u"Caticorix", u"Catinius", u"Catlus",
    u"Catonianus", u"Catotigirni", u"Catoualos", u"Cattabbot", u"Cattabus", u"Cattabuttas", u"Cattaus", u"Cattedius", u"Cattulus", u"Cattuvir",
    u"Cattuvvir", u"Catuen", u"Catuenus", u"Caturicus", u"Caturo", u"Catusius", u"Caurius", u"Caurus", u"Cenalus", u"Cenicus", u"Cenno", u"Ceno",
    u"Cenocantus", u"Centugeni", u"Centus", u"Cicedu", u"Cimarius", u"Cimarus", u"Cinge", u"Cinges", u"Cingessus", u"Cingetoutus", u"Cingius",
    u"Cintio", u"Cinto", u"Cintu", u"Cintugenus", u"Cintumarus", u"Cintusminius", u"Coaeddus", u"Cobledulitauus", u"Cobledulitavus", u"Coimagni",
    u"Colomagni", u"Comanus", u"Comatullus", u"Combaromarus", u"Comnertus", u"Conbertius", u"Conbertus", u"Conconnetodumnus", u"Condarillus",
    u"Condercus", u"Coneddus", u"Congenno", u"Congonetiacus", u"Congonnetiacus", u"Conteddius", u"Contesilo", u"Contessilo", u"Contoutos",
    u"Convictolitavis", u"Corbagni", u"Corio", u"Cornutos", u"Coro", u"Corobus", u"Coteus", u"Cotilius", u"Cotillus", u"Cotilus", u"Cotis",
    u"Cotius", u"Cottalus", u"Cottilus", u"Cottio", u"Cottius", u"Cotto", u"Cottro", u"Cottus", u"Cotus", u"Cotusus", u"Couertomotul",
    u"Covertomotul", u"Covirius", u"Covirus", u"Criciro", u"Criciru", u"Cricirus", u"Crigiru", u"Cunegni", u"Cunigni", u"Cunovicodu", u"Curcagni",
    u"Curcagnus", u"Dacotoutus", u"Dagillus", u"Dagobius", u"Dagomarus", u"Dalagni", u"Dannonus", u"Dano", u"Dattovir", u"Deoratus", u"Dercillos",
    u"Dercillus", u"Deuus", u"Devus", u"Diddignatus", u"Diocaitus", u"Diorix", u"Diuicatus", u"Divicatus", u"Divos", u"Dobagni", u"Doninas",
    u"Donnadu", u"Donnedo", u"Donnius", u"Donnotaurus", u"Donnus", u"Dovagni", u"Drutalus", u"Dubnotalus", u"Dubnovellaun", u"Dubnovellaunos",
    u"Dumnobellaunus", u"Dumnovellaunos", u"Ebicatos", u"Ebredus", u"Eburianus", u"Eburio", u"Eburius", u"Eburo", u"Elusco", u"Elusconos",
    u"Endouellicus", u"Endovellicus", u"Epacus", u"Epasius", u"Epatus", u"Epetinus", u"Epo", u"Epomedius", u"Epos", u"Epotsiorouidus",
    u"Epotsorouidus", u"Eppo", u"Eqqegni", u"Ercaviccas", u"Escengolatis", u"Escincos", u"Esumagius", u"Excingillius", u"Excingomarus",
    u"Excingullus", u"Exscincious", u"Exsomnus", u"Gabrius", u"Gabrus", u"Gedilli", u"Genetlus", u"Genillus", u"Gennalo", u"Girgani", u"Gnatusius",
    u"Grimiggni", u"Haesus", u"Iantasio", u"Iantinus", u"Iantumalius", u"Iantumar", u"Iantumarus", u"Iatinius", u"Iccalus", u"Iccinus", u"Iccnus",
    u"Icomius", u"Ientinus", u"Ientius", u"Iliatus", u"Illiomarus", u"Indercillus", u"Iotobito", u"Isarnouallanos", u"Itavus", u"Itosius",
    u"Itotagi", u"Lanianus", u"Laniogaius", u"Latauis", u"Leucamulo", u"Licno", u"Licnos", u"Licnus", u"Litauus", u"Litavis", u"Litgenes",
    u"Litgenus", u"Litigius", u"Litugenius", u"Lituriri", u"Losagni", u"Lucterius", u"Lugetus", u"Lugius", u"Lugurix", u"Macareus", u"Macarius",
    u"Maccarus", u"Maccis", u"Magiacos", u"Maglagni", u"Magurio", u"Magurius", u"Mailagni", u"Malucnus", u"Mando", u"Maritalus", u"Martalos",
    u"Martilinus", u"Martoualus", u"Meddignatius", u"Meddugnatus", u"Megaravico", u"Melmandus", u"Mertoualus", u"Mesillus", u"Messillus",
    u"Metilius", u"Metillius", u"Miletumarus", u"Moddagni", u"Nantonos", u"Nertomaros", u"Netacari", u"Nisigni", u"Oclicno", u"Oclicnos",
    u"Ollocnus", u"Ollognus", u"Onalisus", u"Oppianicnos", u"Perrius", u"Perrus", u"Peruincus", u"Perus", u"Qasigni", u"Qenilocgni", u"Regenos",
    u"Regenus", u"Regininus", u"Reginius", u"Reginus", u"Remico", u"Remicus", u"Reovalis", u"Reticius", u"Reticus", u"Retomarus", u"Rextugeos",
    u"Rigalis", u"Ripcicnus", u"Ritogenus", u"Rittuvvecc", u"Rituvvecas", u"Rovicus", u"Sacrovir", u"Sacrovirus", u"Sagillius", u"Sagillus",
    u"Samaconius", u"Samalus", u"Samio", u"Samis", u"Samius", u"Sammio", u"Sammo", u"Sammus", u"Samo", u"Samocenus", u"Samocinus", u"Samogenus",
    u"Samognatius", u"Samus", u"Sancotalus", u"Sanicios", u"Scilagni", u"Segolatius", u"Segomaros", u"Senecio", u"Senecius", u"Senocarus",
    u"Senovir", u"Senucaris", u"Silanus", u"Smertulitanus", u"Sollouico", u"Sollovico", u"Suadinus", u"Suadugenus", u"Suadutto", u"Suratus",
    u"Talagni", u"Talavus", u"Talis", u"Talius", u"Tallius", u"Tallus", u"Tallutius", u"Talotius", u"Talussanus", u"Talutius", u"Tanco",
    u"Tanotalos", u"Tarbunus", u"Taruiacus", u"Tascius", u"Tascus", u"Tasgetios", u"Tasgetius", u"Tauratis", u"Tauri", u"Taurio", u"Taurocutius",
    u"Taurou", u"Teutagonus", u"Teuto", u"Teutomalius", u"Teutomus", u"Totavali", u"Toutio", u"Touto", u"Toutobocio", u"Toutobocios", u"Toutos",
    u"Toutus", u"Trenacatus", u"Trenaccatlo", u"Triti", u"Trito", u"Tritos", u"Tritus", u"Trogimarus", u"Trouceteius", u"Tuticanius", u"Tuticanus",
    u"Ulcagni", u"Ulccagni", u"Urogenonertus", u"Valatonius", u"Valis", u"Vallio", u"Vallius", u"Vallo", u"Vallus", u"Vebro", u"Vebru", u"Vecatus",
    u"Vecconius", u"Vecius", u"Vectimarius", u"Vectimarus", u"Vecto", u"Velagenius", u"Velagenus", u"Velenius", u"Velitas", u"Velitius", u"Vello",
    u"Velugni", u"Velugnius", u"Vendagni", u"Vendogni", u"Venecarus", u"Venedius", u"Venextos", u"Venicarus", u"Venixamus", u"Venixxamus",
    u"Vennenus", u"Vennonius", u"Venucius", u"Vepotalus", u"Veqreq", u"Vercatus", u"Vercombogio", u"Vercombogious", u"Vercombogus", u"Versicnos",
    u"Versignos", u"Verter", u"Verto", u"Vertos", u"Vertros", u"Veruecco", u"Veruico", u"Veugnus", u"Vicatus", u"Vicixtillus", u"Victi", u"Viction",
    u"Vindedo", u"Vindicatus", u"Vinicarus", u"Vinovaleius", u"Viranus", u"Virato", u"Viratus", u"Viri", u"Viriacius", u"Viriaicus", u"Virianto",
    u"Viriatis", u"Viriatius", u"Virici", u"Virico", u"Viriodacus", u"Virisimi", u"Virlus", u"Virocantus", u"Vironianus", u"Virotalus",
    u"Virotutus", u"Vitousurix", u"Vlatcani", u"Vlatos", u"Vlatucni", u"Vlatucnos", u"Vlatugni", u"Vocagni", u"Vocarantus", u"Vocorix",
    u"Vogitoutus", u"Voltodaga", u"Vopiscus", u"Voretouirius", u"Voretoviros", u"Vosegus", u"Vridolanos", u"Vrittakos"
     ]

    PRENOMS_F = [
    u"Abrezta", u"Acca", u"Acisillia", u"Adbugiouna", u"Adbugissa", u"Adginna", u"Adgonna", u"Adiania", u"Adianta", u"Admata", u"Adnama", u"Adnamata",
    u"Adnamatia", u"Adnamita", u"Adnamu", u"Adreticia", u"Aduorix", u"Advorix", u"Aesica", u"Aesiua", u"Agedia", u"Agisiaca", u"Agisilia", u"Agisilla",
    u"Aisa", u"Albina", u"Albisia", u"Albucia", u"Aleasiumara", u"Alla", u"Alleicea", u"Alleticia", u"Allia", u"Allouira", u"Allusa", u"Alpina",
    u"Alpinia", u"Alpinula", u"Alteurita", u"Ambada", u"Andaitia", u"Andarta", u"Andebrocirix", u"Andeca", u"Anderca", u"Anderica", u"Anderina",
    u"Anderitia", u"Andilia", u"Andoca", u"Andueia", u"Anduenna", u"Annama", u"Ariola", u"Arrotala", u"Arsulana", u"Atebodua", u"Atectorigiana",
    u"Ategenta", u"Ategnissa", u"Atepa", u"Atepu", u"Atessatia", u"Atestatia", u"Atestia", u"Ateurita", u"Atigenta", u"Atioxta", u"Atreba", u"Atrebia",
    u"Attisaga", u"Atturita", u"Auamacimaria", u"Audata", u"Audenta", u"Auentina", u"Aulricmara", u"Aventina", u"Avitianomara", u"Balatonaua",
    u"Ballatulla", u"Banna", u"Bannua", u"Banona", u"Betudaca", u"Bileseton", u"Bilisa", u"Billia", u"Bimottia", u"Bitudaga", u"Bora", u"Borissa",
    u"Boudenna", u"Boudilla", u"Boudinna", u"Brocchia", u"Brogimara", u"Buscilla", u"Bussia", u"Bussugnata", u"Cabrilla", u"Cabura", u"Caburena",
    u"Caccosa", u"Cacossa", u"Cacudia", u"Cambaria", u"Cambosa", u"Camelognata", u"Camolatia", u"Camoulatia", u"Camula", u"Camulata", u"Camulatia",
    u"Camuledu", u"Camulia", u"Camulilia", u"Camullia", u"Cantexta", u"Caraddouna", u"Caranta", u"Carantana", u"Carantia", u"Carantiana", u"Carantila",
    u"Carantilla", u"Carantina", u"Carantodia", u"Carantusa", u"Carata", u"Caratila", u"Caratilla", u"Caratulla", u"Careia", u"Carenta", u"Caretosa",
    u"Caria", u"Carina", u"Carisia", u"Carissa", u"Carosa", u"Carosia", u"Carrotala", u"Cartulla", u"Caruca", u"Caruiliena", u"Caruonia", u"Cassa",
    u"Cassia", u"Cassibodua", u"Cassicia", u"Cassimara", u"Cassiola", u"Casticia", u"Castina", u"Cata", u"Catalia", u"Catia", u"Catica", u"Catilia",
    u"Catilla", u"Catiola", u"Catnea", u"Catronia", u"Catta", u"Cattara", u"Cattea", u"Cattia", u"Cattira", u"Cattulla", u"Cattuviqqa", u"Catuallauna",
    u"Catucia", u"Catulla", u"Catullia", u"Caturica", u"Caturigia", u"Caturisa", u"Cauaria", u"Caura", u"Cauru", u"Cavaria", u"Cenia", u"Ceniuria",
    u"Cenos", u"Censonia", u"Centa", u"Centogenea", u"Centusmia", u"Cigemma", u"Cincia", u"Cincissa", u"Cingetissa", u"Cinia", u"Cintucra", u"Cintugena",
    u"Cintusma", u"Cintusmina", u"Cintussa", u"Cintussia", u"Cloutina", u"Clutamilla", u"Cobiatia", u"Coblanuo", u"Coblucia", u"Cobnerta", u"Cobromara",
    u"Cobronia", u"Cobruna", u"Comacia", u"Comatia", u"Comatimara", u"Comatulla", u"Combara", u"Comerta", u"Comiomara", u"Condexua", u"Congenetia",
    u"Congenncia", u"Consuadullia", u"Contessia", u"Corasia", u"Corobilla", u"Corrodu", u"Cotina", u"Cotira", u"Cotta", u"Cottia", u"Cottina", u"Cottira",
    u"Cottula", u"Cotu", u"Cotuconi", u"Cotulia", u"Counerta", u"Cricconia", u"Cubria", u"Cunacena", u"Dagania", u"Dania", u"Danissa", u"Dannia",
    u"Dannumaa", u"Danotala", u"Danu", u"Deiotariana", u"Derceia", u"Deuila", u"Deuillia", u"Deuognata", u"Devignata", u"Diona", u"Diorata", u"Diougenia",
    u"Diuilla", u"Diuuogna", u"Diuvogna", u"Diveca", u"Divogenia", u"Donilla", u"Donisia", u"Dubna", u"Dubnia", u"Dumnana", u"Dumnia", u"Eburia",
    u"Eburila", u"Eliomara", u"Elovissa", u"Elvissa", u"Emogenia", u"Epa", u"Epetina", u"Epia", u"Epilla", u"Epillia", u"Epiu", u"Eppa", u"Eppacta",
    u"Eppaxtia", u"Eppia", u"Epponina", u"Etiona", u"Etolugnia", u"Exapia", u"Excinga", u"Excingilla", u"Exobna", u"Exomna", u"Exouna", u"Fimmilene",
    u"Friagabi", u"Gabra", u"Genaca", u"Genetodia", u"Genna", u"Genobia", u"Genucia", u"Gnata", u"Gnatia", u"Gnatilla", u"Iantulla", u"Iantumara", u"Iatta",
    u"Iattossa", u"Ibliomaria", u"Iccia", u"Ilateuta", u"Inatura", u"Inderca", u"Indercilea", u"Isosae", u"Itta", u"Kareia", u"Karina", u"Lanpendia",
    u"Larma", u"Leuca", u"Leucena", u"Leucimara", u"Leucona", u"Leuconia", u"Litania", u"Litogena", u"Littiossa", u"Litu", u"Litua", u"Litucca",
    u"Lituccia", u"Litugena", u"Litullina", u"Loucita", u"Loucitta", u"Lugiola", u"Luppa", u"Macaria", u"Maccira", u"Maccirra", u"Magunia", u"Magunna",
    u"Magusatia", u"Mandelana", u"Manduilla", u"Manduissa", u"Marilla", u"Martidia", u"Martilia", u"Martiria", u"Martna", u"Mata", u"Mataura", u"Materiona",
    u"Matia", u"Maticia", u"Matidia", u"Matina", u"Matona", u"Matonia", u"Matta", u"Mattia", u"Mattosa", u"Mattua", u"Matua", u"Matucenia", u"Matucia",
    u"Matugena", u"Matugenia", u"Matullina", u"Matuna", u"Medilotamica", u"Medlotama", u"Meducena", u"Melicia", u"Meliginna", u"Messilia", u"Messilla",
    u"Metela", u"Metilia", u"Moria", u"Moriena", u"Mottu", u"Motuca", u"Motuidiaca", u"Nama", u"Namia", u"Namidia", u"Namiola", u"Namma", u"Nammia",
    u"Nammota", u"Namu", u"Namusa", u"Namuta", u"Nantia", u"Nantiorix", u"Nemetocena", u"Nemetogena", u"Nerta", u"Nertilla", u"Nertomaria", u"Netelia",
    u"Nitiogenna", u"Ollia", u"Olliadu", u"Olluna", u"Olugnia", u"Orbia", u"Orbiana", u"Orbissa", u"Origena", u"Oxidubna", u"Pera", u"Perra", u"Peruia",
    u"Perula", u"Rega", u"Regallia", u"Regina", u"Reginia", u"Regula", u"Rematia", u"Resia", u"Ressatu", u"Ressilla", u"Ressona", u"Resta", u"Restia",
    u"Reticiana", u"Rextugeniana", u"Riceina", u"Ricina", u"Ricua", u"Riguiru", u"Rikua", u"Ritomara", u"Ritulla", u"Ritumara", u"Rituscia", u"Rotama",
    u"Rotania", u"Sagila", u"Sagillia", u"Sama", u"Samacia", u"Samaxa", u"Samia", u"Samianta", u"Samicantu", u"Samicia", u"Saminia", u"Samma", u"Sammia",
    u"Sammiola", u"Sammola", u"Sammulla", u"Samuda", u"Sattomata", u"Sedata", u"Sedatia", u"Sedecennis", u"Sedia", u"Sedida", u"Segla", u"Segolia",
    u"Segusiaua", u"Senila", u"Senilla", u"Sennaucia", u"Senocenna", u"Senodona", u"Senodonna", u"Sila", u"Solimara", u"Suadugena", u"Suaduilla",
    u"Suadulla", u"Suagria", u"Suausia", u"Sucaria", u"Sueta", u"Sumaria", u"Sumela", u"Sumelia", u"Sumenu", u"Talauia", u"Talavica", u"Taliounia",
    u"Talisia", u"Talissa", u"Taluppa", u"Talussa", u"Tancina", u"Tancorix", u"Tascilla", u"Tasgilia", u"Tasgilla", u"Tauria", u"Taurica", u"Taurilla",
    u"Taurina", u"Teolugnia", u"Teuta", u"Teutalu", u"Teutana", u"Trita", u"Tritia", u"Trocina", u"Troucetissa", u"Troucisa", u"Troucissa", u"Valagenta",
    u"Valeia", u"Valicinia", u"Vallia", u"Vandania", u"Vebromara", u"Vebronara", u"Vebrumma", u"Veca", u"Vecticia", u"Vectinia", u"Velacena", u"Velacosta",
    u"Veleda", u"Velitia", u"Vellibia", u"Vena", u"Venaesia", u"Venia", u"Veniala", u"Venica", u"Venicia", u"Veniena", u"Venimara", u"Veninia", u"Venisama",
    u"Veniuallia", u"Venivallia", u"Venixama", u"Venixema", u"Venixiema", u"Venna", u"Vennonia", u"Venulanta", u"Venuleia", u"Verbronara", u"Verica",
    u"Verodumna", u"Vertia", u"Verucia", u"Vicana", u"Viccu", u"Viccus", u"Victisarana", u"Victulliena", u"Vindaina", u"Vindama", u"Vindauscia",
    u"Vindilla", u"Vindoinissa", u"Vindu", u"Viniuallia", u"Viralira", u"Viratia", u"Viriana", u"Viriata", u"Viricia", u"Viriciu", u"Viriola",
    u"Viriondaga", u"Virodu", u"Virotouta", u"Visurix", u"Vlattia", u"Vlattu", u"Vlatuna", u"Vocara", u"Vocontia", u"Volatia", u"Vritea", u"Vrittia",
    u"Vrogenia" ]
