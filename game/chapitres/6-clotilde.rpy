init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import germains
    from chapitres.classes import clovis

    auMoinsAnnee490 = condition.Condition(temps.Date.DATE_ANNEES, 490, condition.Condition.SUPERIEUR_EGAL)
    auMoinsAnnee492 = condition.Condition(temps.Date.DATE_ANNEES, 492, condition.Condition.SUPERIEUR_EGAL)
    auMoinsAnnee493 = condition.Condition(temps.Date.DATE_ANNEES, 493, condition.Condition.SUPERIEUR_EGAL)
    auMoinsAnnee495 = condition.Condition(temps.Date.DATE_ANNEES, 495, condition.Condition.SUPERIEUR_EGAL)
    auMoinsAnnee497 = condition.Condition(temps.Date.DATE_ANNEES, 497, condition.Condition.SUPERIEUR_EGAL)
    auMoinsAnnee498 = condition.Condition(temps.Date.DATE_ANNEES, 498, condition.Condition.SUPERIEUR_EGAL)
    auMoinsAnnee500 = condition.Condition(temps.Date.DATE_ANNEES, 500, condition.Condition.SUPERIEUR_EGAL)
    # conditions clotilde
    decision_mariage_clotildePasFaite = condition.Condition("decision_mariage_clotilde", 1, condition.Condition.DIFFERENT)
    infos_sur_clotildePasFaite = condition.Condition("infos_sur_clotilde", 1, condition.Condition.DIFFERENT)
    infos_sur_clotildeFaite = condition.Condition("infos_sur_clotilde", 1, condition.Condition.EGAL)

    fiance_a_clotilde = condition.Condition(clovis.Clovis.C_FIANCE_CLOTHILDE, 1, condition.Condition.EGAL)
    marie_a_clotilde = condition.Condition(clovis.Clovis.C_MARIE_CLOTHILDE, 1, condition.Condition.EGAL)
    pas_marie_a_clotilde = condition.Condition(clovis.Clovis.C_MARIE_CLOTHILDE, 1, condition.Condition.DIFFERENT)

    gloireAuMoins5 = condition.Condition(clovis.Clovis.C_GLOIRE, 5, condition.Condition.SUPERIEUR_EGAL)

    # enfants :
    a0enfants = condition.Condition(clovis.Clovis.C_NB_ENFANTS, 0, condition.Condition.EGAL)
    a1enfants = condition.Condition(clovis.Clovis.C_NB_ENFANTS, 1, condition.Condition.EGAL)
    a2enfants = condition.Condition(clovis.Clovis.C_NB_ENFANTS, 2, condition.Condition.EGAL)
    a3enfants = condition.Condition(clovis.Clovis.C_NB_ENFANTS, 3, condition.Condition.EGAL)
    a4enfants = condition.Condition(clovis.Clovis.C_NB_ENFANTS, 4, condition.Condition.EGAL)

    def AjouterEvtsClothilde():
        global selecteur_
        # premiers echos sur Clothilde
        infos_sur_clotilde = declencheur.Declencheur(proba.Proba(0.7, True), "infos_sur_clotilde")
        infos_sur_clotilde.AjouterCondition(auMoinsAnnee490)
        infos_sur_clotilde.AjouterCondition(infos_sur_clotildePasFaite)
        selecteur_.ajouterDeclencheur(infos_sur_clotilde)
        # décision du mariage
        decision_mariage = declencheur.Declencheur(proba.Proba(0.7, True), "decision_mariage")
        decision_mariage.AjouterCondition(decision_mariage_clotildePasFaite)
        decision_mariage.AjouterCondition(auMoinsAnnee492)
        decision_mariage.AjouterCondition(gloireAuMoins5)
        decision_mariage.AjouterCondition(infos_sur_clotildeFaite)
        selecteur_.ajouterDeclencheur(decision_mariage)
        # mariage
        mariage = declencheur.Declencheur(proba.Proba(0.7, True), "mariage")
        mariage.AjouterCondition(fiance_a_clotilde)
        mariage.AjouterCondition(auMoinsAnnee492)
        mariage.AjouterCondition(pas_marie_a_clotilde)
        selecteur_.ajouterDeclencheur(mariage)
        # soutien de Clotilde
        soutienDeClotilde = declencheur.Declencheur(proba.Proba(0.1, True), "soutienDeClotilde")
        soutienDeClotilde.AjouterCondition(marie_a_clotilde)
        soutienDeClotilde.AjouterCondition(estPasChretien)
        selecteur_.ajouterDeclencheur(soutienDeClotilde)
        # 1er enfant
        enfant1 = declencheur.Declencheur(proba.Proba(0.3, True), "enfant1")
        enfant1.AjouterCondition(marie_a_clotilde)
        enfant1.AjouterCondition(a0enfants)
        enfant1.AjouterCondition(auMoinsAnnee493)
        selecteur_.ajouterDeclencheur(enfant1)
        # 2ème enfant
        enfant2 = declencheur.Declencheur(proba.Proba(0.3, True), "enfant2")
        enfant2.AjouterCondition(marie_a_clotilde)
        enfant2.AjouterCondition(a1enfants)
        enfant2.AjouterCondition(auMoinsAnnee495)
        selecteur_.ajouterDeclencheur(enfant2)
        # 3ème enfant
        enfant3 = declencheur.Declencheur(proba.Proba(0.3, True), "enfant3")
        enfant3.AjouterCondition(marie_a_clotilde)
        enfant3.AjouterCondition(a2enfants)
        enfant3.AjouterCondition(auMoinsAnnee497)
        selecteur_.ajouterDeclencheur(enfant3)
        # 4ème enfant
        enfant4 = declencheur.Declencheur(proba.Proba(0.3, True), "enfant4")
        enfant4.AjouterCondition(marie_a_clotilde)
        enfant4.AjouterCondition(a3enfants)
        enfant4.AjouterCondition(auMoinsAnnee498)
        selecteur_.ajouterDeclencheur(enfant4)
        # 5ème enfant
        enfant5 = declencheur.Declencheur(proba.Proba(0.3, True), "enfant5")
        enfant5.AjouterCondition(marie_a_clotilde)
        enfant5.AjouterCondition(a4enfants)
        enfant5.AjouterCondition(auMoinsAnnee500)
        selecteur_.ajouterDeclencheur(enfant5)

label enfant1:
    show clotilde at right
    with moveinright
    "Joie ! Votre premier fils, Ingomer, est né."
    "Très peu de temps après, Clothilde organise son baptème à la foi catholique sans vous consulter."
    "Elle décore somptueusement l'église de voilage et de tentures et fait tremper l'enfant dans l'eau selon sa coutume."
    "Vous acceptez que la mère décide de ces choses. Surtout qu'elle avait peur que le petit erre éternellement dans les limbes si il n'était pas baptisé."
    "Mais malheureusement le petit meurt peu après dans les vêtements blancs, ceux mêmes dans lesquels il avait été régénéré."
    "Votre tristesse est grande mais plus grande encore est votre amertume."
    cl "Si l'enfant avait été voué à mes dieux, il aurait vécu de toute façon ; mais maintenant il n'a pas pu vivre du tout, baptisé au nom de votre Dieu."
    clot "Je rends grâce à Dieu tout puissant, créateur de toutes choses, qui ne m'a pas jugée complètement indigne puisqu'il a daigné accueillir dans son royaume celui qui a été conçu dans mon sein."
    clot "Mon coeur n'est pas frappé de douleur pour cette cause, parce que je sais qu'il a été rappelé de ce monde alors qu'il était dans des vêtements blancs pour être nourri sous le regarde de Dieu."
    $ RetirerACarac(clovis.Clovis.C_CHRISTIANISME, 1)
    jump fin_cycle

label enfant2:
    "Enfin ! Votre deuxième fils, Clodomir, est né."
    "Cette fois encore Clothilde prend l'initiative de le baptiser sans vous en informer malgré la mort d'Ingomer après son baptème il y a deux ans."
    "C'est un coup dur quand vous apprenez que Clodomir aussi est tombé malade peu de temps après son baptème."
    show clotilde at right
    with moveinright
    cl "Il ne peut pas lui arriver autre chose que ce qui est survenu à son frère ; baptisé au nom de votre Christ il mourra aussitôt."
    "Les jours qui suivent sont pénibles, vous vivez dans l'inquiétude et l'impuissance tandis que Clotilde prie du matin au soir avec ferveur."
    "Enfin, Clodomir reprend des forces et des couleurs. Il est sauvé et devient rapidement robuste. Christ n'est peut-être pas un tueur d'enfant."
    jump fin_cycle

label enfant3:
    "Votre troisième fils Childebert est né."
    jump fin_cycle

label enfant4:
    "Votre quatrième fils Clotaire est né."
    jump fin_cycle

label enfant5:
    "Votre fille Clothilde est née."
    jump fin_cycle

label soutienDeClotilde:
    show clotilde at right
    with moveinright
    "Par sa douceur, sa bonté et sa patience Clotilde adoucit vos dures journées de roi."
    "Ses prières vous sont aussi d'un grand soulagement et plus le temps passe plus vous priez avec elle."
    $ AjouterACarac(clovis.Clovis.C_CHRISTIANISME, 1)
    jump fin_cycle

label mariage:
    # scene bg tolbiac
    # play music guerre2 noloop
    $ situation_.SetValCarac(clovis.Clovis.C_MARIE_CLOTHILDE, 1)
    "Gondebaud a tenu parole. Clotilde vous est envoyée sous bonne garde dans un char à boeufs avec robe et trousseau."
    show clotilde at right
    with dissolve
    "Vous n'avez pas été trompé. Clotilde est aussi douce que belle et reste humble et plaisante malgré la situation difficile."
    "Elle pourrait être brisée ou aigrie d'être donnée en mariage à un inconnu par son oncle Gondebaud qui a tué ses parents mais elle fait bonne figure."
    "Comme le mariage est sensé avoir lieu bientôt elle se décide dès le lendemain de son arrivée à sortir de sa réserve pour vous demander la seule chose qui semble réellement l'inquiéter."
    clot "Grand roi Clovis je suis très honorée de bientôt devenir votre épouse et je promets d'ors et déjà de vous aimer et honorer fidèlement."
    clot "Néanmoins je dois confesser qu'une inquiétude me ronge. Je suis catholique et suis très peinée à l'idée d'être marié sans qu'un prêtre du Dieu unique officie."
    clot "Accepteriez vous que nous nous marions selon les rites du catholicisme ?"
    clot "Ou, sinon, puis-je espérer que les piliers les plus importants du mariage seront respectés ? Je veux parler de la monogamie et de l'indissolubilité."
    menu:
        "Hors de question. Vous serez mariés sous le patronage de Freya déesse de la fertilité.":
            clot "Soit je vous obéirai et trouverai le réconfort dans la prière."
            $ RetirerACarac(clovis.Clovis.C_CHRISTIANISME, 1)
            jump mariage_paien
        "Promettre la monogamie et l'indissolubilité":
            clot "Merci grand roi de prendre mes sentiments en compte. Ces douces promesses fait déjà de notre mariage une cérémonie que Dieu approuvera."
            jump mariage_paien
        "Accepter de vous marier selon les rites catholiques":
            clot "C'est trop d'honneur grand roi vous faites de moi la plus heureus des femmes."
            "Bien que satisfaire Clotilde vous réchauffe le coeur, dès que la rumeur de ce mariage catholique se répand, la colère gronde parmi votre peuple."
            $ AjouterACarac(clovis.Clovis.C_CHRISTIANISME, 3)
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 2)
            jump mariage_catholique
    jump fin_cycle

label mariage_paien:
    "PAS FAIT : mariage païen avec Clotilde"
    jump fin_cycle

label mariage_catholique:
    "PAS FAIT : mariage_catholique avec Clotilde"
    jump fin_cycle

label infos_sur_clotilde:
    # scene bg tolbiac
    # play music guerre2 noloop
    $ situation_.SetValCarac("infos_sur_clotilde", 1)
    show clotilde at right
    with dissolve
    clot "A FAIRE Coucou Clovis !"
    jump fin_cycle

label decision_mariage:
    # scene bg tolbiac
    # play music guerre2 noloop
    $ situation_.SetValCarac("decision_mariage_clotilde", 1)

    show clotilde at right
    with dissolve
    "Vous êtes maintenant un roi craint et renommé dans toutes la Gaulle. Un mariage prestigieux est tout ce qui vous manque pour vous hisser au niveau des grands roi germaniques."
    "L'évèque Rémi vous vante la beauté et la vertu de la princesse Clotilde, nièce du roi des burgondes Gondebaud."
    "Le fait qu'elle soit catholique est sans doute la raison pour laquelle il vous la recommande tant mais enfin il a raison : "
    "le lignage de Clotilde est ancien et prestigieux, bien supérieur au vôtre qui ne doit sa renommée qu'à la gloire militaire de votre père. Et les burgondes sont des voisins puissants dont le soutien vous serait précieux."
    menu:
        "Demandez-vous la main de Clotilde à son oncle Gondebaud ?"
        "Non. Il est hors de question d'épouser une catholique.":
            jump fin_cycle
        "Oui":
            "Vous envoyez un émissaire chargé de cadeaux pour demander la main de la princesse Clotilde."
            "Gondebaud tergiverse beaucoup car en tant que chrétien arien et surtout en tant que meurtrier des parents il a de bonnes raisons de se méfier d'elle."
            "Cependant sa position est très mauvaise entre les puissants royaumes gothiques et il n'ose pas vous opposer de refus au risque de se faire un dangereux ennemi de plus."
            "Il promet de vous envoyer Clotilde très prochainement."
            $ situation_.SetValCarac(clovis.Clovis.C_FIANCE_CLOTHILDE, 1)
    jump fin_cycle
