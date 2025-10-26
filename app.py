import pyvisual as pv
from ui.ui import create_ui
from cvzone.SerialModule import SerialObject
import threading

arduino = SerialObject()


# ===================================================
# ================ 1. LOGIC CODE ====================
# ===================================================

# (Your logic code here)
def display_data(data, ui):
    temp = data[0]
    hum = data[1]
    print(temp,hum)
    #Zero => x=136, y=228, width=28, height=41
    #Max => x=136, y=71, width=28, height=198
    # Frame => 41 -> 198
    ui["page_0"]["temp_text"].text = temp + '°C'
    ui["page_0"]["humidity_text"].text = hum + '%'

    change = ((int(temp) / 50) * 157)
    ui["page_0"]["moving_rect"].height = 41 + change
    ui["page_0"]["moving_rect"].y = 228 - change
    # if state == 1:
    #     ui["page_0"]["button_rect"].height = 59 - 20
    #     ui["page_0"]["button_rect"].y = 124 + 20
    # else:
    #     ui["page_0"]["button_rect"].height = 59
    #     ui["page_0"]["button_rect"].y = 124




# ===================================================
# ============== 2. EVENT BINDINGS ==================
# ===================================================


def attach_events(ui):
    """
    Bind events to UI components.
    :param ui: Dictionary containing UI components.
    """

    def poll_arduino():
        while True:
            try:
                myData = arduino.getData()
                display_data(myData, ui)
            except:
                pass

    thread = threading.Thread(target=poll_arduino, daemon=True)
    thread.start()


# ===================================================
# ============== 3. MAIN FUNCTION ==================
# ===================================================


def main():
    app = pv.PvApp()
    ui = create_ui()
    attach_events(ui)
    ui["window"].show()
    app.run()


if __name__ == '__main__':
    main()
