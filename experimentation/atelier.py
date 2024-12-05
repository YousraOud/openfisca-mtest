import numpy

from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_mtest import CountryTaxBenefitSystem
from openfisca_mtest.reforms.plf_2025 import plf_2025



print("> salaire")
salaires = numpy.array([30002, 40002, 180002])
print(salaires)
print("")

tax_benefit_system = CountryTaxBenefitSystem()
# print(tax_benefit_system.parameters(2024).impot.bareme)
simulation_builder = SimulationBuilder()
simulation = simulation_builder.build_default_simulation(tax_benefit_system, count=3)
simulation.set_input("salaire", 2024, salaires)
print("> impot sur le revenu 2024:")
print(simulation.calculate("impot_revenu", 2024))
print("")


reformed_tax_benefit_system = plf_2025(tax_benefit_system)
simulation_builder_reformed = SimulationBuilder()
simulation_reformed = simulation_builder_reformed.build_default_simulation(reformed_tax_benefit_system, count=3)
#salaires_2025 = numpy.array([30002, 10000, 10000])
simulation_reformed.set_input("salaire", 2025, salaires)
print("> impot sur le revenu 2025:")
print(simulation_reformed.calculate("impot_revenu", 2025))
