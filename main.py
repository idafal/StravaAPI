import stravaAPI_test as test

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    MasterFlag = {
        0: '0: Test',
        1: '1: Test beta transformation',
    }[0]
    if MasterFlag == '0: Test':
        print("test")
        test.stravaAuthAPIcall()
        test.read_activities()
