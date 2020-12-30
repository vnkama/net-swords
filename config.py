import pygame as pg     # использован pg.Rect

# party         один запуск авто от начала движения до кончины авто
# generation    одно поколение, состоит из нескольких Party, в конце поколения пересчитываются нейросети
# Series        несколько поколений

# training      режим обучения, машинка едет под управлением нейросети
# show          показ процесса обучения в записи

# =================================================================================


# rtime - реальное время. используется для например для синхронизации FPS или опрса клавиатуры
# gtime - это внутриигровое время, по сюжету игра может длится хоть 10 часов, а на компьютере прошло 5 минут
# dt - временной интервал
# постфиксы
# _ms     милисекунды,
# _sec    секунды
# _f      флоат, аремя с плавающей точкой


#srf        surface




# =================================================================================
DRAW_FPS = 60
UPDATE_FPS = 20

# =================================================================================

KNIGHT_SPEED = 2.0  # два тайла в секунду, погоризонтали







MAIN_WND_TITLE = 'Net swords'       # имя главного окна
MAIN_WND_FULLSCREEN = 0             # 0 - оконный режим
                                    # 1 - полноэкранный режим

MAIN_WND_BACKGROUND = 0x682828      # debug

MAIN_WND_HEIGHT     = 1000           # 768(в окне win)   # размер определен спрайтом зелени 128 * 6 = 768
MAIN_WND_WIDTH      = 1200          # 1400(в окне win)



# размер игровой карты (НЕ экрана)
MAP_SIZE_X = 50
MAP_SIZE_Y = 50
MAP_X_MAX_INDEX = MAP_SIZE_X - 1
MAP_Y_MAX_INDEX = MAP_SIZE_Y - 1

TILE_SIZE = 16      #px
#MAP_SIZE_XY = (MAP_SIZE_X, MAP_SIZE_Y)
#MAP_SIZE_RECT = pg.Rect(0, 0, MAP_SIZE_X, MAP_SIZE_Y)





################################################


THEME_BLACK_CLR                 = 0x090909
THEME_RED_CLR                   = 0xFB0D1C
THEME_GREEN_CLR                 = 0x2AC325
THEME_BLUE_CLR                  = 0x426DF9
THEME_DARK_GREY_CLR             = 0x282828
THEME_MED_GREY_CLR              = 0x606060
THEME_LIGHT_GREY_CLR            = 0xe7e7e7
THEME_SWAMP_GREEN_CLR           = 0xACB78E

THEME_BORDER_CLR_LOW            = THEME_MED_GREY_CLR
THEME_BORDER_CLR_HIGH           = THEME_LIGHT_GREY_CLR
THEME_BACKGROUND_CLR            = THEME_DARK_GREY_CLR
THEME_BACKGROUND_HOVER_CLR      = 0x1A1A1A
THEME_FONT_CLR                  = THEME_LIGHT_GREY_CLR
THEME_FONT_DISABLED_CLR         = THEME_MED_GREY_CLR
THEME_FONT                      = "arial_20"
THEME_FONT_CONTROL              = "arial_14"

THEME_BUTTON_BACKGROUND         = THEME_BACKGROUND_CLR
THEME_BUTTON_BACKGROUND_HOVER   = THEME_BACKGROUND_HOVER_CLR
THEME_BUTTON_BORDER_CLR         = THEME_BORDER_CLR_HIGH
THEME_BUTTON_BORDER_DISABLED_CLR = THEME_BORDER_CLR_LOW

THEME_SEMAPHOR_GREY             = THEME_DARK_GREY_CLR
THEME_SEMAPHOR_GREEN            = 0x10F010
THEME_SEMAPHOR_RED              = 0xE01010


THEME_SELECT_BACKGROUND_CLR         = THEME_BACKGROUND_CLR
THEME_SELECT_BACKGROUND_HOVER_CLR   = THEME_BACKGROUND_HOVER_CLR
THEME_SELECT_BORDER_CLR         = THEME_BORDER_CLR_HIGH
THEME_SELECT_STRING_HEIGHT      = 22

################################################
MAP_BACKGROUND_CLR = THEME_BLACK_CLR
MAP_NET_CLR = THEME_DARK_GREY_CLR

PLAYER_1_CLR = THEME_BLUE_CLR
PLAYER_2_CLR = THEME_GREEN_CLR

################################################

TOOL_WND_WIDTH       = 300
TOOL_WND_RECT        = pg.Rect(MAIN_WND_WIDTH-TOOL_WND_WIDTH, 0, TOOL_WND_WIDTH, MAIN_WND_HEIGHT)   #left top w h
# CONTROL_WND_BACKGROUND  = THEME_DARK_GREY_CLR
TOOL_WND_FONT_SIZE   = 20
# THEME_FONT_CLR  = 0xe7e7e7              # цвет шрифта на контролах
# CONTROL_WND_FONT_DISABLED_COLOR  = THEME_BUTTON_BORDER_DISABLED_CLR


MAP_WND_RECT            = pg.Rect(0,0,MAIN_WND_WIDTH - TOOL_WND_WIDTH,MAIN_WND_HEIGHT) #left top w h
MAP_WND_BACKGROUND      = 0x682848


CONSOLE_CLR_ERROR   = "\033[35m\033[1m"
CONSOLE_CLR_RED     = "\033[31m\033[1m"
CONSOLE_CLR_GREEN   = "\033[32m\033[1m"
CONSOLE_CLR_RESET   = "\033[0m"

#=================================================================================