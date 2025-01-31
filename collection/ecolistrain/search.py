from django.contrib.auth.models import User
from djangoql.schema import DjangoQLSchema

from common.search import (
    SearchCustomFieldUserLastnameWithOptions,
    SearchCustomFieldUserUsernameWithOptions,
)

from ..shared.admin import (
    FieldCreated,
    FieldFormZProject,
    FieldLastChanged,
    FieldUse,
)
from .models import EColiStrain


class EColiStrainSearchFieldUserUsername(SearchCustomFieldUserUsernameWithOptions):
    id_list = EColiStrain.objects.all().values_list("created_by", flat=True).distinct()


class EColiStrainSearchFieldUserLastname(SearchCustomFieldUserLastnameWithOptions):
    id_list = EColiStrain.objects.all().values_list("created_by", flat=True).distinct()


class EColiStrainQLSchema(DjangoQLSchema):
    """Customize search functionality"""

    include = (EColiStrain, User)  # Include only the relevant models to be searched

    def get_fields(self, model):
        """Define fields that can be searched"""

        if model == EColiStrain:
            return [
                "id",
                "name",
                "resistance",
                "genotype",
                "supplier",
                FieldUse(),
                "purpose",
                "note",
                "created_by",
                FieldCreated(),
                FieldLastChanged(),
                FieldFormZProject(),
            ]
        elif model == User:
            return [
                EColiStrainSearchFieldUserUsername(),
                EColiStrainSearchFieldUserLastname(),
            ]
        return super().get_fields(model)
