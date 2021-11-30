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

    auMoinsAnnee496 = condition.Condition(temps.Date.DATE_ANNEES, 496, condition.Condition.SUPERIEUR_EGAL)
    # conditions alamans
    alamansEnGuerre = condition.Condition(germains.Alamans.C_GUERRE, 1, condition.Condition.EGAL)
    alamansPasEnGuerre = condition.Condition(germains.Alamans.C_GUERRE, 1, condition.Condition.DIFFERENT)
    batailleTolbiacPasFaite = condition.Condition("batailleTolbiac", 1, condition.Condition.DIFFERENT)

    def MiseEnPlaceGuerreAlamans():
        global situation_
        situation_.SetValCarac(germains.Alamans.C_GUERRE, 1)

    def AjouterEvtGuerreAlamans():
        global selecteur_
        bataille_tolbiac = declencheur.Declencheur(proba.Proba(0.2, True), "bataille_tolbiac")
        bataille_tolbiac.AjouterCondition(alamansEnGuerre)
        bataille_tolbiac.AjouterCondition(auMoinsAnnee496)
        bataille_tolbiac.AjouterCondition(batailleTolbiacPasFaite)
        selecteur_.ajouterDeclencheur(bataille_tolbiac)

# label attaque_alamans:
    # $ MiseEnPlaceGuerreAlamans() # A FAIRE : déclenchement de cette guerre pas encore ajouté
    # jump fin_cycle

label bataille_tolbiac:
    scene bg tolbiac

    jump appel_divin

label appel_divin:
    scene bg tolbiac
    play music guerre2 noloop
    $ situation_.SetValCarac("batailleTolbiac", 1)
    "La bataille tourne de plus en plus mal. Plusieurs de vos gardes du corps sont tombés et vous êtes sur le point d'être encerclé."
    "Impossible de trouver une issue pour faire retraite en bon ordre, et vous savez que les alamans seront sans pitié si ils vous atteignent."
    "Dans ce péril extrême vous repensez à l'aide que Wotan devrait vous apporter pour soutenir votre race divine. Vous reviennent aussi les paroles de Clothilde vous assurant qu'un tel moment arriverait tôt ou tard où vous devriez accepter Jésus Christ comme sauveur ou périr."
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
