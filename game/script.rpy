define config.menu_include_disabled = True
define gui.choice_button_text_insensitive_color = "#555"

# Persos
define narrator = Character(color="#fafad8", what_italic=True)
define std = Character('Perso standard...', color="#B22222") # personnage standard remplacé selon les situations. (son nom est mis à jour)
define cl = Character('Clovis', color="#80002a")

image clotilde = "perso/clotilde.png"
define clot = Character('Clotilde', color="#800000")

image alboflede = "perso/alboflede.png"
define albo = Character('Alboflède', color="#33cc33")

# Musiques
define audio.roi_mort = "musique/akingisdead.ogg"
define audio.turexgloriae = "musique/turexgloriae.ogg" # baptème etc
define audio.christ1 = "musique/journeytoabsolution.ogg"
define audio.youpi_paien = "musique/Quite An Adventure.ogg"
define audio.printemps = "musique/Sea Season.ogg"
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
    AjouterEvtThuringie()
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
    # jump guerre_burgonde490 # tmp test

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
