from abs.religions import religion
from chapitres.classes import syagrius
from chapitres.classes import clovis
from spe.humanite import portrait_roi_clovis
from abs.humanite import portrait
from spe.humanite import pnj_roi_clovis
from abs import situation
from abs.humanite import metier
from abs.humanite import pnj
from abs.humanite import trait

class SituationClovis(situation.Situation):

    def __init__(self):
        situation.Situation.__init__(self, 175000)

    def AffichageArmee(self):
        global debug_
        # armée de clovis
        str = u""
        val = self.GetValCaracInt(clovis.Clovis.C_MILITAIRE)
        if val < 0:
            str = u"Armée insignifiante"
        elif val <= 2:
            str = u"Armée faible"
        elif val <= 4:
            str = u"Bonne armée"
        elif val <= 7:
            str = u"Armée puissante"
        elif val <= 10:
            str = u"Armée redoutable"
        else:
            str = u"Armée invincible"
        if self.debug_:
            return u"{} ({})".format(str, val)
        return str

    def AffichageReligion(self):
        if self.GetValCarac(religion.Religion.C_RELIGION) == religion.Paien.NOM:
            valPretre = self.GetValCaracInt(metier.Pretre.NOM)
            strPretre = u""
            if valPretre > 0:
                strPretre = u" - Prêtre roi"
            str =  u"Païen{}".format(strPretre)
            if self.debug_:
                str = u"{} ({})".format(str, self.caracs_[clovis.Clovis.C_CHRISTIANISME])
            return str
        if self.caracs_[religion.Religion.C_RELIGION] == religion.Christianisme.NOM:
            if self.debug_:
                return u"{} ({})".format(self.caracs_[religion.Religion.C_RELIGION], self.caracs_[clovis.Clovis.C_CHRISTIANISME])

        return self.caracs_[religion.Religion.C_RELIGION]

    def AffichageGloire(self):
        val = self.GetValCarac(clovis.Clovis.C_GLOIRE)
        if self.debug_:
            return u"Gloire : {}".format(val)
        return u""

    def AffichageUsurpation(self):
        val = self.GetValCarac(clovis.Clovis.C_USURPATION)
        if self.debug_:
            return u"Risques d'usurpation : {}".format(val)
        return u""

    def AffichageRichesse(self):
        if ( trait.Richesse.NOM not in self.caracs_):
            if self.debug_:
                return u"Riche (0)"
            return u"Riche"
        strRichesse = self.collectionTraits[trait.Richesse.NOM].GetDescription(self)
        if strRichesse == "":
            strRichesse = u"Riche"
        if self.debug_:
            strRichesse = u"{} ({})".format(strRichesse, self.collectionTraits[trait.Richesse.NOM].GetVal(self))
        return strRichesse

    def DeterminerPortrait(self):
        """
        récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
        celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
        """
        portr = portrait_roi_clovis.PortraitRoiClovis()
        portraitStr = portr.DeterminerPortraitPersoPrincipal(self, True)
        self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
        return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

    # PNJ

    def AffichagePortraitPere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj_roi_clovis.PnjRoiClovis) :
            return pere.portraitStr_
        return ""

    def AffichagePortraitMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj_roi_clovis.PnjRoiClovis) :
            return mere.portraitStr_
        return ""

    def AffichagePere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj_roi_clovis.PnjRoiClovis) :
            str = u"{}".format(pere)
        return str

    def AffichageMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj_roi_clovis.PnjRoiClovis) :
            str = u"{}".format(mere)
        return str
