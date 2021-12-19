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
    from chapitres.classes import syagrius
    from chapitres.classes import clovis

    auMoinsAnnee486 = condition.Condition(temps.Date.DATE_ANNEES, 486, condition.Condition.SUPERIEUR_EGAL)
    # conditions syagrius
    syagriusEnGuerre = condition.Condition(syagrius.Syagrius.C_GUERRE, 1, condition.Condition.EGAL)
    syagriusPasEnGuerre = condition.Condition(syagrius.Syagrius.C_GUERRE, 1, condition.Condition.DIFFERENT)
    # vase de soissons:
    vaseSoissonsVengeance = condition.Condition(clovis.Clovis.C_VASE_SOISSONS, 1, condition.Condition.EGAL)
    def MiseEnPlaceGuerreSyagrius():
        global situation_
        situation_.SetValCarac(syagrius.Syagrius.C_GUERRE, 1)

    def AjouterEvtGuerreSyagrius():
        global selecteur_
        combat_avant_garde = declencheur.Declencheur(proba.Proba(0.2, True), "combat_avant_garde")
        combat_avant_garde.AjouterCondition(syagriusEnGuerre)
        combat_avant_garde.AjouterCondition(syagriusPasVaincu)
        selecteur_.ajouterDeclencheur(combat_avant_garde)

        vase_de_soissons_le_retour = declencheur.Declencheur(proba.Proba(0.3, True), "vase_de_soissons_le_retour")
        vase_de_soissons_le_retour.AjouterCondition(auMoinsAnnee486)
        vase_de_soissons_le_retour.AjouterCondition(vaseSoissonsVengeance)
        selecteur_.ajouterDeclencheur(vase_de_soissons_le_retour)

label invasion_syagrius:
    play music guerre1 noloop
    $ MiseEnPlaceGuerreSyagrius()
    "Votre armée est maintenant bien avancée en territoire ennemi et vous savez que Syagrius a fini de lever la sienne."
    menu:
        "Si vous suivez la coutume franque de le défier sur le champs de bataille de son choix.":
            "Syagrius accepte le défi et choisit un champs près de sa capitale Soissons."
            "Vos hommes sont pressés d'en venir aux mains et sont heureux que vous ayez respecté les lois d'Odin. Thor et les walkyrie vous soutiendront."
            $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
            $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
        "Si vous vous dirigez vers sa capitale Soissons pour l'écraser le plus tôt possible.":
            "Syagrius semble vouloir éviter un siège et vient à votre rencontre. Heureusement pour vous car la prise de ville n'est pas la spécialité de vos guerrier."
        "Si vous avancez lentement et prenez le temps de piller le pays.":
            "Les terres romaines sont bien plus riches que les vôtres. Vous faites un grand butin de richesse et d'esclaves. Vos hommes sont satisfaits."
            "Syagrius quitte Soissons pour venir vous arrêter. Heureusement pour vous car la prise de ville n'est pas la spécialité de vos guerrier."
            $ AjouterACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(syagrius.Syagrius.C_PILLAGE, 2)
            $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)

    jump bataille_soisson

label bataille_soisson:
    scene bg francs
    $ puissanceArmeeSyagrius = situation_.GetValCaracInt(syagrius.Syagrius.C_MILITAIRE)
    "{b}Bataille de Soissons.{/b}"
    "Syagrius a rangé son armée de manière ordonnée à la romaine. Mais la discipline apparente ne vous impressionne pas. La plupart des soldats sont des germains qui combattront sans grand entousiasme."
    menu:
        "D'où allez vous combattre ?"
        "Au premier rang !":
            jump bataille_soisson_combat
        "En soutien au second rang.":
            "Vous faites avancer votre armée en bon ordre. Les soldats sont motivés par votre présence et veulent se faire remarquer par leur bravoure."
            $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeSyagrius, situation_)
            menu:
                "Les romains se préparent au choc. [testCombat.affichage_]":
                    $ reussi = testCombat.TesterDifficulte(situation_)
                    if reussi:
                        "Vos hommes dominent si bien la bataille que votre première ligne semble suffire à repousser les romains."
                        jump bataille_soisson_2
                    else:
                        "La première ligne est enfoncée. Vous allez devoir aller au contact avec votre garde d'honneur pour la soutenir."
                        jump bataille_soisson_combat

        "En retrait pour avoir une vue d'ensemble et rester en sécurité.":
            "De puis une petite colline vous donnez vos ordres pour faire avancer votre infanterie."
            "Vos soldats obéissent restent confiants et disciplinés mais il est clair qu'ils apprécient peu que le descendant des dieux que vous êtes reste à l'arrière."
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
            $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
            $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeSyagrius, situation_)
            menu:
                "Les romains se préparent au choc. [testCombat.affichage_]":
                    $ reussi = testCombat.TesterDifficulte(situation_)
                    if reussi:
                        "Vos hommes dominent si bien la bataille que votre première ligne semble suffire à repousser les romains."
                        jump bataille_soisson_2
                    else:
                        "Les pertes sont lourdes mais vos soldats sont meilleurs et plus motivés. Ils prennent l'avantage."
                        $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
                        jump bataille_soisson_2

    label bataille_soisson_combat:
        "Vous formez un groupe compact avec l'élite de vos hommes et avancez droit sur le centre ennemi."
        "Les romains tentent de rester en formation serrée avec leur boucliers levés. Vous ordonnez alors à vos hommes de lancer leurs lourds javelots à crochet."
        "La plupart sont bloqués par les boucliers ennemis mais ils sont si lourds et solides que les romains ne peuvent plus manoeuvrer et peinent à lever leurs boucliers."
        $ testCombat = testDeCarac.TestDeCarac(metier.Guerrier.NOM, 4, situation_)
        menu:
            "C'est le moment de lancer une charge complète.[testCombat.affichage_]":
                $ reussi = testCombat.TesterDifficulte(situation_)
                if not reussi:
                    "Alors que vous atteignez les lignes ennemies un javelot bien lancé vous frappe en plein visage. Votre court règne s'arrête ici."
                    jump mort
                else:
                    "Vous avez repéré un officier empêtré par un javelot dans son bouclier. Vous écartez le bouclier d'un coup de pied dans le javelot et poignardez facilement son corps découvert avec votre scramasax."
                    $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
                    $ testCombat = testDeCarac.TestDeCarac(metier.Guerrier.NOM, 7, situation_)
                    menu:
                        "Enhardi vous vous jetez en avant en chantant à la gloire d'Odin.[testCombat.affichage_]":
                            $ reussi = testCombat.TesterDifficulte(situation_)
                            if reussi:
                                "Vous empoignez votre francisque et faites un grand massacre des romains terrifiés et désordonnés."
                                $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
                                jump bataille_soisson_2
                            else:
                                "Vous avez été repéré et une volée de javelot s'abat sur vous. Votre bouclier tient le choc mais les pointent le traversent et s'arrêtent à un doigt de votre visage."
                                "Sous le choc, vous êtes heureusement secourus par vos fidèles gardes du corps qui couvrent votre corps de leurs boucliers."
                                jump bataille_soisson_2

    jump bataille_soisson_2

label bataille_soisson_2:
    scene bg francs
    $ puissanceArmeeSyagrius = situation_.GetValCaracInt(syagrius.Syagrius.C_MILITAIRE)
    $ a_convaincu_chararic = situation_.GetValCaracBool("a_convaincu_chararic")
    if a_convaincu_chararic:
        "Voyant que l'armée ennemie faiblit vous constatez que votre parent Chararic, qui devait vous soutenir avec sa cavalerie, n'intervient pas."
        "Impossible de s'occuper de lui pour l'instant, mais il ne perd rien pour attendre."
        $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)

    $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeSyagrius, situation_)
    menu:
        "Les romains sont prêts à céder."
        "C'est le moment de faire donner les réserves de cavalerie.[testCombat.affichage_]":
            $ reussi = testCombat.TesterDifficulte(situation_)
            if reussi:
                "Les romains n'avaient plus besoin que de ce choc pour fuir en désordre. Votre cavalerie en massacre un grand nombre durant leur fuite."
            else:
                "Les romains s'obstinent à résister et il faut des heures pour que finalement, brisés de fatigue ils succombent."
                $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
    "Pas trace de Syagrius quand vous pénétrez en arme dans sa capitale Soissons sans que personne n'essaye de vous résister. Soit il est mort, soit il a fui. C'est de toute façon une victoire écrasante dont il ne se remettra pas."
    $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
    # fin de la guerre (en théorie)
    $ situation_.SetValCarac(syagrius.Syagrius.C_VAINCU, 1)
    $ situation_.SetValCarac(syagrius.Syagrius.C_GUERRE, 0)
    jump vase_de_soissons

label vase_de_soissons:
    "La ville de Soissons est pillée de fond en comble et vous en tirez, vous et vos hommes, de grandes richesses. En particulier du palais de Syagrius et des églises."
    "Une délégation de prêtres catholiques menés par un évèque vient cependant vous demander humblement de leur restituer un grand et magnifique vase sacré."
    "La règle franques veut qu'un cinquième du butin, tiré au sort, vous revienne. Mais il ne s'agit que d'un vase et en roi victorieux vous pouvez vous permettre d'exceptionnellement prendre ce vase."
    menu:
        "Que faites vous ?"
        "Refuser et renvoyer l'évèque":
            $ RetirerACarac(clovis.Clovis.C_CHRISTIANISME, 1)
        "Accepter mais seulement si le sort vous accorde le vase.":
            $ unACinq = random.randint(1,5)
            if unACinq == 1:
                "Par chance le tirage au sort vous donne le vase. Vous le rendez aux prêtres qui vous sont très reconnaissants."
                jump fin_cycle
            else:
                "Le tirage au sort ne vous donne pas le vase sacré. Les prêtres repartent les mains vides."
                $ RetirerACarac(clovis.Clovis.C_CHRISTIANISME, 1)
                jump fin_cycle
        "Demander à vos soldats de vous laisser ce vase hors part.":
            "Arrivant à Soissons où toute la masse du butin avait été placée au milieu, vous dites : "
            cl "Je vous prie, ô très valeureux guerriers, de ne pas vous opposer à ce que me soit concédé hors part ce vase."
            "A ces mots ceux qui avaient l'esprit sain répliquent : "
            "{i}Tout ce que nous voyons ici, glorieux Roi, est à toi et nous mêmes sommes soumis à ta domination. Fais donc maintenant ce qui convient à ton bon plaisir.{/i}"
            "Or après qu'ils eurent parlé ainsi, un homme léger, jaloux et frivole, ayant levé sa hache, frappa le vase en criant à voix forte : "
            "{i}Tu n'auras rien ici que ce que le sort t'attribuera vraiment !{/i}"
            $ testCombat = testDeCarac.TestDeCarac(metier.Guerrier.NOM, 5, situation_)
            menu:
                "C'est ce que dit la loi mais un tel affront vous rend furieux."
                "le faire exécuter":
                    "Vos hommes vous obéissent et le misérable est décapité sous vos yeux. Vous voyez bien néanmoins que c'est par peur qu'on vous obéit et que votre mépris des coutumes rend furieux plus d'un franc."
                    $ AjouterACarac(clovis.Clovis.C_USURPATION, 3)
                "L'attaquer immédiatement [testCombat.affichage_]":
                    $ reussi = testCombat.TesterDifficulte(situation_)
                    if reussi:
                        "Le combat ne dure qu'un instant. Vous fendez le crâne du misérable à coup de hache et il s'effondre au milieu du butin et de vos hommes ébahis."
                        $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
                        "Vous voyez bien néanmoins que c'est par peur qu'on vous obéit et que votre mépris des coutumes rend furieux plus d'un homme."
                        $ AjouterACarac(clovis.Clovis.C_USURPATION, 2)
                    else:
                        "Malgré sa surprise le soldat réagit à la vitesse de l'éclair et sous les yeux de vos hommes ébahis il vous poignarde en plein coeur avec sa scramasaxe."
                        "Mourir de la main de ses propres hommes pour une bête histoire de partage du butin. Quelle fin misérable pour celui qui aurait pu être un grand roi."
                        jump mort
                "Accepter de suivre la coutume":
                    $ situation_.SetValCarac(clovis.Clovis.C_VASE_SOISSONS, 1)
                    "Vous parvenez à contenir votre ressentiment avec une douce patience."
                    "Au moins, le vase qui est en métal n'a pas été brisé et le tirage au sort vous le donne. Ce qui vous permet de le rendre aux envoyés de l'évèque."

    "En prenant en compte les propriétés que vous avez saisies votre part de butin est colossale. Vous n'avez jamais été aussi riche."
    $ AjouterACarac(trait.Richesse.NOM, 6)
    "Vos hommes se sont aussi considérablement enrichis et vous sont plus fidèles que jamais."
    $ RetirerACarac(clovis.Clovis.C_USURPATION, 2)
    scene bg carte486
    "Votre royaume est agrandi sans compter que sans Syagrius les terres vers l'ouest seront sans doute très peu défendues."
    jump fin_cycle

label vase_de_soissons_le_retour:
    "Vous allez bientôt partir en expédition militaire pour éliminer des rebelles et vous passez en revue vos guerriers."
    "Ils sont responsables de l'achat et de l'entretien de leur équipement et savent qu'en temps de guerre vous avez droit de vie et de mort sur eux, aussi sont-ils d'une discipline à tout épreuve."
    "Lors de l'inspection de la phalange vous reconnaissez le guerrier qui vous avait insulté lors du partage du butin de Soissons."
    $ situation_.SetValCarac(clovis.Clovis.C_VASE_SOISSONS, 0)
    menu:
        "Vous préférez oublier et ne laissez rien paraître.":
            jump fin_cycle
        "Vous en profitez pour vous venger.":
            "Vous vous adressez à lui :"
            cl "Personne n'a apporté des armes aussi mal tenues que les tiennes, car ni ta lance, ni ton épée, ni ta hache ne sont en bon état."
            "Et, saississant la hache de l'homme vous la jetez à terre. Mais alors que celui ci s'était un peu incliné pour la ramasser,"
            menu:
                "vous l'humiliez publiquement":
                    "Vous le bousculez et le jetez au sol. L'homme est furieux mais se soumet en silence."
                "Vous le tuez":
                    "levant les mains vous lui envoyez votre propre hache dans la tête."
                    cl "C'est ainsi que tu as fait à Soissons avec le vase."
                    "Quand il fut mort vous ordonnâtes aux autres de se retirer. Ainsi vous leur inspirâtes une grande crainte."
                    $ RetirerACarac(clovis.Clovis.C_USURPATION, 2)

    jump fin_cycle

label combat_avant_garde:
    $ puissanceArmeeSyagrius = situation_.GetValCaracInt(syagrius.Syagrius.C_MILITAIRE)
    $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE], puissanceArmeeSyagrius, situation_)
    menu:
        "Votre avant-garde se heurte à une petite armée romaine."
        "vos ordres sont d'éviter le combat":
            "Vos cavaliers parviennent facilement à échapper aux romains lourds et malabiles."
            jump fin_cycle
        "Au combat ! [testCombat.affichage_]":
            $ reussi = testCombat.TesterDifficulte(situation_)
            if reussi:
                "Vos hommes écrasent facilement ces mauvais militaires et pillent la région."
                $ RetirerACarac(syagrius.Syagrius.C_STABILITE, 1)
                $ AjouterACarac(syagrius.Syagrius.C_PILLAGE, 1)
            else:
                "Vos cavaliers sont incapables de briser la cohorte romaine et s'enfuient. C'est une défaite cuisante. Sans importance stratégique mais humiliante."
                $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
            jump fin_cycle
