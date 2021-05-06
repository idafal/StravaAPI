import stravaAPI_test as test
import StravaAPI as strava

"""
Source: https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86
"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    MasterFlag = {
        0: '0: Test',
        1: '1: Get all data',
        2: '2: Test automatic token refresh'
    }[1]
    if MasterFlag == '0: Test':
        print(MasterFlag)
        test.stravaAuthAPIcall()
        test.read_activities()

    if MasterFlag == '1: Get all data':
        print(MasterFlag)
        strava.read_all_activities()
    if MasterFlag == '2: Test automatic token refresh':
        print(MasterFlag)
        strava.testapicall()
