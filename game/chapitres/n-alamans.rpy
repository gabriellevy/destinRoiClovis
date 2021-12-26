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

    def AjouterEvtGuerreAlamans():
        global selecteur_
        invasion_alamans = dec_clo.DecClovisU(proba.Proba(0.4, True), "bataille_tolbiac", 495)
        selecteur_.ajouterDeclencheur(invasion_alamans)

label invasion_alamans:
    scene bg tolbiac
    "Ce que vous craigniez depuis des années a fini par vous arriver : les tribus germaniques de l'Est qu'on appelle Alamans se sont décidées à envahir les territoires francs avec une armée particulièrement nombreuse."
    "Pour l'instant c'est le territoire de vos voisins et alliés les francs du Rhin qui est touché."
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
    "Cette bataille s'engage de la pire manière possible : avec votre allié en fuite, face à des alamans supérieurs en nombre, et en étant séparé de vos terres par l'ennemi."
    "Le combat commence en escarmouches entre archer et lanceurs de javelot des deux camps."
    "Mais les alamans se savent supérieurs et ne perdent pas de temps : ils engagent le corps à corps, qui dégénère rapidement en un sanglant massacre."

    "Lentement mais surement votre armée perdu du terrain et semble sur le point d'être exterminée. Plusieurs de vos gardes du corps sont tombés et vous êtes sur le point d'être encerclé."
    "Impossible de trouver une issue pour faire retraite en bon ordre, et vous savez que les alamans seront sans pitié si ils vous atteignent."
    "Dans ce péril extrême vous repensez à l'aide que Wotan devrait vous apporter pour soutenir votre race divine. Vous reviennent aussi les paroles de Clothilde vous assurant qu'un tel moment arriverait tôt ou tard où vous devriez accepter Jésus Christ comme sauveur."
    $ peut_se_debrouiller = 1
    label appel_divin_choix:
        $ testCourage = testDeCarac.TestDeCarac(trait.Courage.NOM, 8, situation_)
        menu:
            "Qu'allez-vous faire ?"
            "Invoquer l'aide de Wotan pour détruire l'ennemi de vos propres mains.":
                $ RetirerACarac(clovis.Clovis.C_CHRISTIANISME, 5)
                "A FAIRE"
                jump fin_cycle
            "Promettre au Dieu de Clothilde que vous vous convertirez si il vous apporte la victoire.":
                $ AjouterACarac(clovis.Clovis.C_CHRISTIANISME, 5)
                "A FAIRE"
                jump fin_cycle
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

    label appel_divin_seul:
        "A FAIRE : se débrouille tout seul et a une chance de s'en sortir"
        jump fin_cycle
