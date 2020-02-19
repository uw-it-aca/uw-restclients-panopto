from restclients_core.util.decorators import use_mock
from uw_panopto.dao import Panopto_DAO

fdao_panopto_override = use_mock(Panopto_DAO())
