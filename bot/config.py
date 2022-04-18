import os
from pathlib import Path

class Config:
    
    API_ID = 3796974
    API_HASH = "9511d0112631f9990337eb724d1a7d0d"
    BOT_TOKEN = "5392802848:AAEKmK2Qfxdg5v3t46DzgQGhkT5JvMgfOeI"
    SESSION_NAME = os.environ.get('SESSION_NAME')
    LOG_CHANNEL = -1001771465683
    DATABASE_URL = "mongodb+srv://mjfreeflix:Manya004@cluster0.9oay3.mongodb.net/screenshots?retryWrites=true&w=majority"
    AUTH_USERS = [int(i) for i in os.environ.get('1464063686').split(' ')]
    MAX_PROCESSES_PER_USER = int(os.environ.get('MAX_PROCESSES_PER_USER', 2))
    MAX_TRIM_DURATION = int(os.environ.get('MAX_TRIM_DURATION', 120))
    TRACK_CHANNEL = -1001771465683
    SLOW_SPEED_DELAY = int(os.environ.get('SLOW_SPEED_DELAY', 15))
    HOST = os.environ.get('HOST', '')
    
    SCRST_OP_FLDR = Path('screenshots/')
    SMPL_OP_FLDR = Path('samples/')
    THUMB_OP_FLDR = Path('thumbnails/')
    COLORS = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'gold', 'silver', 'pink']
    FONT_SIZES_NAME = ['Small', 'Medium', 'Large']
    FONT_SIZES = [30, 40, 50]
