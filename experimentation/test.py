from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_mtest import CountryTaxBenefitSystem

tax_benefit_system = CountryTaxBenefitSystem()

simulation_builder = SimulationBuilder()
simulation = simulation_builder.build_default_simulation(tax_benefit_system, count=3)
simulation.set_input('salaire', '2020-01', np.array([1500, 2500, 3500]))

income_tax = simulation.calculate('income_tax', '2020-01')
print("income_tax", income_tax)

