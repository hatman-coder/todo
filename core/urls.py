from django.contrib import admin
from django.urls import path, include
from external.swagger.swagger import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from renderer.views import render_index_page


swagger_urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger_ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
    path('', render_index_page, name='home_page'),
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls'))
] + swagger_urlpatterns
