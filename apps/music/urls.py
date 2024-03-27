from django.urls import path

from apps.music.api_endpoints.Album import AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumDestroyView, AlbumRetrieveView
from apps.music.api_endpoints.Artist import ArtistList, ArtistCreateView, \
    ArtistUpdateView, ArtistRetrieveView
from apps.music.api_endpoints.Artist.ArtistDestroy.views import ArtistDeleteView
from apps.music.api_endpoints.Song import SongList, SongCreateView, SongUpdateView, SongDeleteView,  \
    SongRetrieveView

urlpatterns = [
    path("song/", SongList.as_view()),
    path("song/create/", SongCreateView.as_view()),
    path("song/<pk>/update/", SongUpdateView.as_view()),
    path("song/<pk>/delete/", SongDeleteView.as_view()),
    path("song/<pk>/retrieve", SongRetrieveView.as_view()),
    path("artist/", ArtistList.as_view()),
    path("artist/create/", ArtistCreateView.as_view()),
    path("artist/<pk>/update/", ArtistUpdateView.as_view()),
    path("artist/<pk>/delete/", ArtistDeleteView.as_view()),
    path("artist/<pk>/retrieve/", ArtistRetrieveView.as_view()),
    path("album/", AlbumListView.as_view()),
    path("album/create/", AlbumCreateView.as_view()),
    path("album/<pk>/update/", AlbumUpdateView.as_view()),
    path("album/<pk>/destroy/", AlbumDestroyView.as_view()),
    path("album/<pk>/retrieve/", AlbumRetrieveView.as_view()),


]