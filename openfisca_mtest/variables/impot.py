from openfisca_core.periods import YEAR
from openfisca_core.variables import Variable
from openfisca_core.model_api import ADD
from openfisca_mtest.entities import Contribuable


class impot_revenu(Variable):
    value_type = float
    entity = Contribuable
    definition_period = YEAR
    label = "Montant de l'impot sur le revenu (IR) des contribuables "

    def formula(contribuable, period, parameters):
        salaire = contribuable('salaire', period, options=[ADD])
        bareme = parameters(period).impot.bareme
        return bareme.calc(salaire)
