from dotenv import load_dotenv
import os

load_dotenv()

SOURCE_BASEDIR=os.getenv('SOURCE_BASEDIR')
ARTIST=os.getenv('ARTIST')
ALBUM=os.getenv('ALBUM')
SOURCE_DIR=f'{SOURCE_BASEDIR}/{ARTIST}/{ALBUM}'