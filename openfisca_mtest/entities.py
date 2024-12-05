"""
This file defines the entities needed by our legislation.

Taxes and benefits can be calculated for different entities: Contribuables, household, companies, etc.

See https://openfisca.org/doc/key-concepts/Contribuable,_entities,_role.html
"""

from openfisca_core.entities import build_entity

Household = build_entity(
    # TODO a supprimer pour le modele du Maroc
    key = "household",
    plural = "households",
    label = "All the people in a family or group who live together in the same place.",
    doc = """
    Household is an example of a group entity.
    A group entity contains one or more individual·s.
    Each individual in a group entity has a role (e.g. parent or children). Some roles can only be held by a limited number of individuals (e.g. a 'first_parent' can only be held by one individual), while others can have an unlimited number of individuals (e.g. 'children').

    Example:
    Housing variables (e.g. housing_tax') are usually defined for a group entity such as 'Household'.

    Usage:
    Check the number of individuals of a specific role (e.g. check if there is a 'second_parent' with household.nb_Contribuables(Household.SECOND_PARENT)).
    Calculate a variable applied to each individual of the group entity (e.g. calculate the 'salaire' of each member of the 'Household' with salaries = household.members("salaire", period = MONTH); sum_salaries = household.sum(salaries)).

    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    """,
    roles = [
        {
            "key": "parent",
            "plural": "parents",
            "label": "Parents",
            "max": 2,
            "subroles": ["first_parent", "second_parent"],
            "doc": "The one or two adults in charge of the household.",
            },
        {
            "key": "child",
            "plural": "children",
            "label": "Child",
            "doc": "Other individuals living in the household.",
            },
        ],
    )

Contribuable = build_entity(
    key = "contribuable",
    plural = "contribuables",
    label = "Entite unitaire du modele. Contribuable au sens des impots.",
    doc = """
    Contribuable au sens des articles 39 et 40 de la Constitution.
    """,
    is_person = True,
    )
 
entities = [Household, Contribuable]
