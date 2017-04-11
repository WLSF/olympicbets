from api.v1.users.views import UserViewSet
from api.v1.sports.views import SportViewSet
from api.v1.teams.views import TeamViewSet
from api.v1.regions.views import RegionViewSet
from api.v1.games.views import GameViewSet
from api.v1.leagues.views import LeagueViewSet
from api.v1.bets.views import BetViewSet, BetTypeViewSet
from api.v1.accounts.views import AccountViewSet, TransactionViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sports', SportViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'games', GameViewSet)
router.register(r'leagues', LeagueViewSet)
router.register(r'bets', BetViewSet)
router.register(r'bettypes', BetTypeViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'transaction', TransactionViewSet)

api_urlpatterns = router.urls