# Persos
define narrator = Character(color="#fafad8", what_italic=True)
define cl = Character('Clovis', color="#80002a")

# Musiques
define audio.epique_principale = "musique/epique_principale.ogg"
define audio.conquetes = "musique/conquetes.ogg"

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
    AjouterEvtsUsurpation()
    AjouterEvtAvenement()
    AjouterEvtsRien()
    AjouterEvtRenforcement481_485()
    AjouterEvtGuerreSyagrius()
    AjouterEvtGuerreAlamans()
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
    # jump bataille_tolbiac # tmp test

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
