import pyvisual as pv


def create_page_0_ui(window,ui):
    """
    Create and return UI elements for Page 0.
    :param container: The page widget for Page 0.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["Rectangle_0"] = pv.PvRectangle(container=window, x=130, y=201, width=40,
        height=100, idle_color=(255, 255, 255, 1), border_color=None, border_thickness=0,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Rectangle_1"] = pv.PvRectangle(container=window, x=124, y=52, width=52,
        height=227, idle_color=None, border_color=(0, 0, 0, 1), border_thickness=6,
        corner_radius=18, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Circle_2"] = pv.PvCircle(container=window, x=100, y=247, width=100,
        height=100, idle_color=(255, 255, 255, 1), border_color=(0, 0, 0, 1), border_thickness=6,
        border_style="solid", on_hover=None, on_click=None, on_release=None,
        opacity=1, is_visible=True, tag=None)

    ui_page["Rectangle_3"] = pv.PvRectangle(container=window, x=129, y=209, width=42,
        height=76, idle_color=(255, 255, 255, 1), border_color=None, border_thickness=0,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["moving_rect"] = pv.PvRectangle(container=window, x=136, y=71, width=28,
        height=198, idle_color=(240, 103, 46, 1), border_color=None, border_thickness=0,
        corner_radius=0, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Circle_5"] = pv.PvCircle(container=window, x=117, y=265, width=66,
        height=65, idle_color=(240, 103, 46, 1), border_color=(0, 0, 0, 1), border_thickness=0,
        border_style="solid", on_hover=None, on_click=None, on_release=None,
        opacity=1, is_visible=True, tag=None)

    ui_page["Rectangle_6"] = pv.PvRectangle(container=window, x=171, y=73, width=27,
        height=7, idle_color=(0, 0, 0, 1), border_color=None, border_thickness=0,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Rectangle_7"] = pv.PvRectangle(container=window, x=171, y=104, width=27,
        height=7, idle_color=(0, 0, 0, 1), border_color=None, border_thickness=0,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Rectangle_8"] = pv.PvRectangle(container=window, x=171, y=135, width=27,
        height=7, idle_color=(0, 0, 0, 1), border_color=None, border_thickness=0,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Rectangle_9"] = pv.PvRectangle(container=window, x=173, y=166, width=27,
        height=7, idle_color=(0, 0, 0, 1), border_color=None, border_thickness=0,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Rectangle_10"] = pv.PvRectangle(container=window, x=173, y=197, width=27,
        height=7, idle_color=(0, 0, 0, 1), border_color=None, border_thickness=0,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Rectangle_11"] = pv.PvRectangle(container=window, x=173, y=228, width=27,
        height=7, idle_color=(0, 0, 0, 1), border_color=None, border_thickness=0,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_12"] = pv.PvText(container=window, x=200, y=68, width=51,
        height=16, idle_color=(194, 155, 215, 0), text='50°', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_13"] = pv.PvText(container=window, x=200, y=99, width=51,
        height=16, idle_color=(194, 155, 215, 0), text='40°', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_14"] = pv.PvText(container=window, x=200, y=130, width=51,
        height=16, idle_color=(194, 155, 215, 0), text='30°', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_15"] = pv.PvText(container=window, x=200, y=161, width=51,
        height=16, idle_color=(194, 155, 215, 0), text='20°', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_16"] = pv.PvText(container=window, x=200, y=192, width=51,
        height=16, idle_color=(194, 155, 215, 0), text='10°', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_17"] = pv.PvText(container=window, x=200, y=223, width=51,
        height=16, idle_color=(194, 155, 215, 0), text='0°', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["temp_text"] = pv.PvText(container=window, x=130, y=30, width=105,
        height=22, idle_color=(194, 155, 215, 0), text='0°C', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=22,
        font_color=(240, 103, 46, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Rectangle_19"] = pv.PvRectangle(container=window, x=0, y=286, width=300,
        height=116, idle_color=(240, 103, 46, 1), border_color=None, border_thickness=0,
        corner_radius=0, border_style="solid", opacity=0.22, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["humidity_text"] = pv.PvText(container=window, x=235, y=328, width=49,
        height=26, idle_color=(194, 155, 215, 0), text='0%', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=22,
        font_color=(240, 103, 46, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Rectangle_21"] = pv.PvRectangle(container=window, x=-51, y=0, width=98,
        height=45, idle_color=(240, 103, 46, 0.77), border_color=None, border_thickness=0,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_22"] = pv.PvText(container=window, x=225, y=302, width=68,
        height=26, idle_color=(194, 155, 215, 0), text='Độ Ẩm', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/BeVietnamPro/BeVietnamPro.ttf', font_size=18,
        font_color=(0, 0, 0, 1), bold=True, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Icon_23"] = pv.PvIcon(container=window, x=-2, y=5, width=36,
        height=36, idle_color=(255, 255, 255, 1), preserve_original_colors=False, icon_path='assets/icons/e5e67c2908.svg',
        corner_radius=5, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    return ui_page
