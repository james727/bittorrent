from parse import ParseTorrent
from torrent import Torrent
from tracker_connect import TrackerConnect
from manage import Connection
from filemanager import FileManager

torrent = ParseTorrent('temp2.torrent').parse()
tc = TrackerConnect(torrent)
conn = Connection(tc, torrent)
