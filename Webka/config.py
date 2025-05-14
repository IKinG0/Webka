# config.py
TELEGRAM_BOT_TOKEN = "" # сюда токен бота, от FatherBot
ALLOWED_USER_IDS = [] # сюда user_id своего аккаунта telegram, без ковычек

MIN_CONTOUR_AREA = 1000
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

CAPTURE_DELAY = 2.0

PHOTO_COOLDOWN_PERIOD = 3 # период в секундах между фотками
VIDEO_FPS = 30 # фпс записываемого видео
VIDEO_NO_MOTION_STOP_DELAY = 5 # через сколько секунд остановка видео после того как на нём нету объекта
VIDEO_RECORD_PATH = "motion_videos"
SCREENSHOT_DIR = "motion_screenshots"
