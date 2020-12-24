# import pygame as pg
from config import *
from fw.functions import *
# from fw.FwError import FwError

from fw.GuiControl import GuiControl
from Vector import *

#
#
#
class GuiSelectList(GuiControl):

    def __init__(self,params):

        params['background_color'] = params.get('background_color',THEME_SELECT_BACKGROUND_CLR)
        params['background_color_hover'] = params.get('background_color_hover',THEME_SELECT_BACKGROUND_HOVER_CLR)
        params['border_color'] = params.get('border_color',THEME_SELECT_BORDER_CLR)
        params['border_width'] = params.get('border_width',1)

        super().__init__(params)

        self.arr_text = params['text']


        getAppWnd().registerHandler_MOUSEMOTION(self)
        getAppWnd().registerHandler_MOUSEBUTTONDOWN(self)

        self.is_drawed = 0  #пока ни разу не нарисован


    #
    #
    #
    def desctructor(self):
        getAppWnd().unregHandler_MOUSEMOTION(self)
        getAppWnd().unregHandler_MOUSEBUTTONDOWN(self)


    def drawThis(self):

        if not self.mouse_hover_flag:
            self.drawBackground()
        else:
            self.drawBackground(self.background_color_hover)

        self.drawBorder()

        font_obj = getAppWnd().getFont('arial_16')

        # выведем строки в выпадающем спсике
        for i, cur_string in enumerate(self.arr_text):
            text_srf = font_obj.render(cur_string, 1, HRGB(THEME_FONT_CLR))
            self.surface.blit(
                text_srf,
                (5, 1 + i * THEME_SELECT_STRING_HEIGHT)
            )

        # нарисован
        self.is_drawed = 1





    def handle_MouseButtonDown(self, event):
        if self.is_drawed:
            # работаем только в случае если спсиок был нарисован хоть 1 раз

            if self.isPointInWindow(event.pos) and event.button == 1:
                #LB нажата в зоне спиcка

                wnd_d2 = self.surface.get_abs_offset()          #относительно окна приложения/экрана (mainWnd)
                click_d2 = d2_minus(event.pos,wnd_d2)           #координата клика относительно данного
                text_ind = (click_d2[1]-1) // THEME_SELECT_STRING_HEIGHT    #0-based индекс текста, по которому кликунли
                self.closeSetValue(self.arr_text[text_ind])


            else:
                # клик любой кнопкой вне созоны
                self.closeWoSaving()

        return True

