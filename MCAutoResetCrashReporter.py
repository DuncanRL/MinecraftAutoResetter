from MCAutoReset import *
import traceback

if __name__ == "__main__":
    try:
        ara = AutoResetApp()
        ara.mainloop()
    except:
        traceback.print_exc()
        input("Press enter to exit...")