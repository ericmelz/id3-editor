from dotenv import load_dotenv
import os

load_dotenv()

ALBUM          = os.getenv('ALBUM')
ARTIST         = os.getenv('ARTIST')
SHORT_NAME     = os.getenv('Zero Hour')
SOURCE_BASEDIR = os.getenv('SOURCE_BASEDIR')
TOTAL_DISCS    = os.getenv('TOTAL_DISCS')

SOURCE_DIR=f'{SOURCE_BASEDIR}/{ARTIST}/{ALBUM}'