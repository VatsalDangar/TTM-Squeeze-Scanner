
from snapshot import *
from squeeze import *
from candlesticks import *
import keyboard
from datetime import *
import socket 

def check_connection():
    try:
        socket.create_connection(("1.1.1.1",53))
        return True
    except OSError:
        pass
    return False

def UpdateSensex():
    # CurrentTime = datetime.now()
    
    snapSensex30()
    ComputeTTM("Datasets")
    
    
def UpdateLowCap():
    SnapLowCap()
    ComputeTTM("Datasets_LowCap")




    
print("\t\t\t\t\t-----------------------------------------------")
print("\t\t\t\t\t    ***  *****   ***   **    *  *  *  ***")
print("\t\t\t\t\t    *      *    *   *  * *   *  * *   *")
print("\t\t\t\t\t    ***    *    *   *  *  *  *  **    ***")
print("\t\t\t\t\t      *    *    *   *  *   * *  * *     *")
print("\t\t\t\t\t    ***    *     ***   *    **  *  *  ***")
print("\t\t\t\t\t-----------------------------------------------\n")


while keyboard.is_pressed('q') == False:
    
    print("\t\t\t\t___________________________________________________________\n")
    print("\t\t\t\t---------------- Welcome to Stonks Scanner ----------------")
    print("\t\t\t\t___________________________________________________________\n")
    
    if (check_connection() == False):
        print("\n\t\t\t\t__________________________________________________________")
        print("\t\t\t\t                  Connect to Internet                     ")
        print("\t\t\t\t__________________________________________________________\n")
        exit()
    else:
        print("\t\t\t\t\tOptions -->")
        print("\t\t\t\t\t             (1) Sensex30")
        print("\t\t\t\t\t             (2) Low Cap Stonks")
        print("\t\t\t\t\t             (3) Add Tickers")
        print("\t\t\t\t\t             (4) Force Update Datasets")
        print("\t\t\t\t\t             (5) Candlestick patterns")
        print("\t\t\t\t\t             (6) Exit")

        choice = int(input("\nChoose A Option --> :  "))
        print("\n")

        if(choice == 1):
            UpdateSensex()
        elif(choice == 2):
            UpdateLowCap()
        elif(choice == 3):
            addTickers()
        elif(choice == 4):
            ForceUpdate()
        elif(choice == 5):
            candlemenu()
        elif(choice == 6):
            exit()
        else:
            print("-- INVALID OPTION --")
        


        
