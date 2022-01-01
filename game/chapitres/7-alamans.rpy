init -5 python:
    import random
    from spe import dec_clo
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

    alamansVaincus = condition.Condition(germains.Alamans.C_VAINCU, 1, condition.Condition.EGAL)
    def AjouterEvtGuerreAlamans():
        global selecteur_
        invasion_alamans = dec_clo.DecClovisU(proba.Proba(0.4, True), "bataille_tolbiac", 495)
        selecteur_.ajouterDeclencheur(invasion_alamans)

        # 1ère invasion des wisigoths
        invasion_wisigoths1 = dec_clo.DecClovisU(proba.Proba(0.4, True), "invasion_wisigoths1", 496)
        invasion_wisigoths1.AjouterCondition(alamansVaincus)
        selecteur_.ajouterDeclencheur(invasion_wisigoths1)

label invasion_wisigoths1:
    scene bg tolbiac
    with dissolve
    "Ragaillardi par la victoire inespérée de Tolbiac et ayant toute votre armée levée et avide de pillage vous êtes tenté d'envahier le territoire d'Alaric, roi des wisigoths."
    "Alaric n'a pas levé son armée et ses frontières sont sans défense mais c'est un ennemi riche et puissant."
    $ valArmee = situation_.GetValCaracInt(clovis.Clovis.C_MILITAIRE)
    if valArmee < 2:
        "Et votre propre armée est très affaiblie."
    menu:
        "Envahir les wisigoths":
            jump invasion_wisigoths1_ok
        "Renoncer":
            jump fin_cycle

    label invasion_wisigoths1_ok:
        "En suivant la voie romaine à grand pas vous parvenez à vous emparer sans trop de pertes de Tours, Poitiers, puis Saintes."
        $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
        $ AjouterACarac(trait.Richesse.NOM, 1)
        "Malheureusement Alaric finit par réorganiser son armée et acourir."
        "Puis il déploie astucieusement ses wisigoths, en particulier sa redoutable cavalerie lourde, et vous met en très mauvaise posture."
        $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE, metier.Stratege.NOM], 8, situation_)
        menu:
            "Si vous faites face [testCombat.affichage_]":
                $ reussi = testCombat.TesterDifficulte(situation_)
                if reussi:
                    "Contre toute attente vous parvenez à repousser les wisigoths et leur tuer suffisament de monde pour qu'ils fuient et se retranchent dans Saintes."
                    "Vous n'avez cependant pas les moyens de les assiéger car la maladie décime votre armée mal approvisionnée."
                    "Vous devez rentrer à Paris mais votre force a gandement impressionné les wisigoths et les galloromains qui répandent les rumeurs de vos exploits."
                    $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
                    $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
                    jump fin_cycle
                else:
                    "La cavalerie lourde des Wisigoths fracasse vos lignes sous les sabots de ses destriers. Vous êtes obligé d'abandonner le terrain avec de lourdes pertes."
                    $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 2)
                    $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
                    jump fin_cycle
            "Si vous vous repliez.":
                "Alaric ne vous force pas à combattre. Il préfère vous harceler en douceur sans prendre de risque."
                "Vous parvenez à rentrer à Paris sain et sauf mais avec une armée épuisée et sans grand honneur."
                $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
                $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
                jump fin_cycle
    jump fin_cycle

label invasion_alamans:
    scene bg tolbiac
    with dissolve
    "Ce que vous craigniez depuis des années a fini par vous arriver : les tribus germaniques de l'Est qu'on appelle Alamans se sont décidées à envahir les territoires francs avec une armée particulièrement nombreuse."
    "Pour l'instant c'est le territoire de vos voisins et alliés les francs du Rhin qui est touché."
    $ situation_.SetValCarac(germains.Alamans.C_GUERRE, 1)
    play music guerre2 noloop
    "Vous levez immédiatement l'armée pour les secourir. De toute façon si vous ne le faites pas ils seront vaincus et vous serez le suivant."

    "Quand vous atteignez la zone de guerre vous constatez que l'armée des alamans est nettement plus nombreuse que la vôtre et qu'elle assiège la fortresse de Tolbiac de votre cousin Sigebert des francs Rhénans."
    menu:
        "Attaquer les alamans ?":
            jump bataille_tolbiac
        "Ravager le territoire non défendu eds alamans pour les forcer à abandonner le siège.":
            "Cette manoeuvre est habile et aurait pu fonctionner si les francs du Rhin avaient tenu bon retranchés dans Tolbiac."
            "Mais vos éclaireurs vous informent qu'ils sont en fuite et que les alamans sont maintenant sur le point d'envahier vos propres terres."
            "Vous êtes obligé de tourner bride pour combattre."
            jump bataille_tolbiac

    jump bataille_tolbiac

label bataille_tolbiac:
    scene bg tolbiac
    with dissolve
    "Cette bataille s'engage de la pire manière possible : avec votre allié en fuite, face à des alamans supérieurs en nombre, et en étant séparé de vos terres par l'ennemi."
    "Le combat commence en escarmouches entre archer et lanceurs de javelot des deux camps."
    $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
    "Mais les alamans se savent supérieurs et ne perdent pas de temps : ils engagent le corps à corps, qui dégénère rapidement en un sanglant massacre."

    "Lentement mais surement votre armée perdu du terrain et semble sur le point d'être exterminée. Plusieurs de vos gardes du corps sont tombés et vous êtes sur le point d'être encerclé."
    $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
    "Impossible de trouver une issue pour faire retraite en bon ordre, et vous savez que les alamans seront sans pitié si ils vous atteignent."
    "Dans ce péril extrême vous repensez à l'aide que Wotan devrait vous apporter pour soutenir votre race divine. Vous reviennent aussi les paroles de Clothilde vous assurant qu'un tel moment arriverait tôt ou tard où vous devriez accepter Jésus Christ comme sauveur."
    $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
    $ peut_se_debrouiller = 1
    label appel_divin_choix:
        $ testCourage = testDeCarac.TestDeCarac(trait.Courage.NOM, 8, situation_)
        menu:
            "Qu'allez-vous faire ?"
            "Invoquer l'aide de Wotan pour détruire l'ennemi de vos propres mains.":
                $ RetirerACarac(clovis.Clovis.C_CHRISTIANISME, 2)
                "A FAIRE"
                jump fin_cycle
            "Promettre au Dieu de Clothilde que vous vous convertirez si il vous apporte la victoire.":
                $ AjouterACarac(clovis.Clovis.C_CHRISTIANISME, 5)
                "A FAIRE"
                jump serment_tolbiac
            "Prier Dieu de vous pardonner vos péchés et accepter votre mort prochaine.":
                $ AjouterACarac(clovis.Clovis.C_CHRISTIANISME, 5)
                "A FAIRE"
                jump fin_cycle
            "Repousser les idoles et vous sortir de là par vos propres forces. [testCourage.affichage_]" if peut_se_debrouiller == 1:
                $ reussi = testCourage.TesterDifficulte(situation_)
                if reussi:
                    jump appel_divin_seul
                else:
                    "Le péril est tel que pour la première fois de votre vie vous êtes terrifié, vos hommes tombent les uns après les autres. Dans votre terreur vous sentez que seul un dieu peut vous sauver."
                    $ peut_se_debrouiller = 0
                    jump appel_divin_choix

    label serment_tolbiac:
        cl "Ô Jésus-Christ que Clothilde proclame fils du Dieu vivant, toi qui, dit-on, donnes une aide à ceux qui peinent et qui attribues la victoire à ceux qui espèrent en toi, je sollicite dévotement la gloire de ton assistance."
        cl "Si tu m'accordes la victoire sur ces ennemis et si j'expérimente la vertu miraculeuse que le peuple voué à ton nom déclare avoir mis à l'épreuve je croirai en toi et je me baptiserai en ton nom."
        cl "J'ai en effet invoqué mes dieux mais comme j'en fais l'expérience ils se sont abstenus de m'aider."
        cl "Je crois qu'ils ne sont doués d'aucun pouvoir eux qui ne viennent pas au secours de ceux qui leur obéissent."
        cl "C'est toi que maintenant j'invoque, c'est en toi que je désire croire pourvu que je sois arraché à mes adversaires."
        jump victoire_bataille_tolbiac

    label appel_divin_seul:
        "A FAIRE : se débrouille tout seul et a une chance de s'en sortir"
        jump fin_cycle

    label victoire_bataille_tolbiac:
        $ nomChefAlaman = francs_.CreerPrenom(True)
        "[nomChefAlaman], le chef des alamans, se battait bravement à découvert sur son cheval blanc. Il semblait invincible, possédé par la puissance de Wotan en personne."
        "Soudain, il fut frappé d'une hache de lancer en pleine poitrine et tomba de cheval. Pour tous les alamans comme pour les francs, cela signifiait qu'il avait perdu la faveur de Wotan."
        "Ils commencèrent à s'apeurer, perdirent leur avantage, puis se débandèrent. Finalement pour arrêter le massacre, ils firent leur soumission et jetèrent leurs armes."
        $ AjouterACarac(clovis.Clovis.C_GLOIRE, 2)
        menu:
            "Victoire ! Ils sont à votre merci !"
            "Si vous les exterminez":
                "Après les pertes qu'ils ont subies vos guerriers sont satisfaits de votre ordre et égorgent les alamans qui s'étaient rendus dans un grand massacre."
                jump victoire_alamans
            "Si vous leur ordonnez de quitter la Gaulle à tout jamais":
                "Difficile de dire si ils tiendront parole mais ils obéissent et vous laissent tout leur territoire jusqu'aux frontières de la Gaulle."
                jump victoire_alamans
            "Si vous recrutez parmi eux pour remplacer vos pertes.":
                "Beaucoup acceptent votre offre. Ces renforts sont bienvenus mais ils seront moins fiables que vos guerriers francs."
                $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 2)
                $ AjouterACarac(clovis.Clovis.C_USURPATION, 2)
                "Les autres quittent la Gaulle et vous laissent ce territoire comme prix du vainqueur."
                jump victoire_alamans

        jump fin_cycle

    label victoire_alamans:
        "A FAIRE : insérer carte conquêtes alamans (et mise à jour de la carte actuelle)"
        "Cette victoire vous apporte un gain de territoire mais elle a surtout l'avantage de sécuriser l'Est en neutralisant des voisins très turbulents."
        "Votre royaume n'a jamais été plus puissant et stable."
        $ situation_.SetValCarac(germains.Alamans.C_VAINCU, 1)
        $ situation_.SetValCarac(germains.Alamans.C_GUERRE, "")
        jump fin_cycle
