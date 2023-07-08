
# Third party
from rest_framework.routers import DefaultRouter

#Local
from . import views


router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')
urlpatterns = router.urls
