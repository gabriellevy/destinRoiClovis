# Persos
define narrator = Character(color="#fafad8", what_italic=True)
define cl = Character('Clovis', color="#80002a")

image clotilde = "perso/clotilde.png"
define clot = Character('Clotilde', color="#800000")

# Musiques
define audio.post_conversation = "musique/journeytoabsolution.ogg"
define audio.guerre1 = "musique/saladinbesiegejerusalem.ogg"
define audio.guerre2 = "musique/siegeofkerak.ogg"
define audio.epique_principale = "musique/hornsofhattinandaftermath.ogg"
define audio.conquetes = "musique/marchtoholyland.ogg" # march vers la terre sainte (crusader king II)

init -10 python:
    from abs import selecteur
    import random

    selecteur_ = selecteur.Selecteur()
    def determinationEvtCourant(situation):
        global selecteur_
        return selecteur_.determinationEvtCourant(situation)

init -1 python:
    from abs import selecteur
    from chapitres.classes import syagrius
    import random

    AjouterEvtsProfessionnels()
    AjouterEvtsRoi()
    AjouterEvtsUsurpation()
    AjouterEvtAvenement()
    AjouterEvtsRien()
    AjouterEvtRenforcement481_485()
    AjouterEvtGuerreSyagrius()
    AjouterEvtBurgondes()
    AjouterEvtsClothilde()
    AjouterEvtGuerreAlamans()
    AjouterEvtBapteme()
    AjouterEvtsPaganisme()
    # mise en place des caracs de bases
    MiseEnPlaceCaracsSyagrius()

# Le jeu commence ici
label start:
    scene bg priere
    # play music musique_menu
    queue music [ epique_principale, conquetes ] # pseudo liste de lecture temporaire
    jump naissance

label debut_cycle:
    show screen valeurs_traits
    $ prochainEvt = determinationEvtCourant(situation_)
    $ renpy.jump(prochainEvt)

label fin_cycle:
    # "Fin d'un cycle."
    # jump comtCritique # tmp test

    $ situation_.TourSuivant()

    if situation_["Santé"] != "Mort":
        jump debut_cycle

label mort:
    menu:
        "Fin de vie."
        "ok":
            pass
    return

label labelGoTo_pasFait:
    "Ce sélecteur d'énévement n'a pas de label go to on dirait"

label pas_evt_trouve:
    " ERREUR : pas d'événement trouvé à ce cycle"

label probaAbsoluesSup100:
    "Le total des probas absolues dépasse 100%% !"
