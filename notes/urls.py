from rest_framework.routers import DefaultRouter
from .views import NoteAPIModelViewSet

router_notes = DefaultRouter()

router_notes.register(prefix='notes', basename='notes', viewset=NoteAPIModelViewSet)