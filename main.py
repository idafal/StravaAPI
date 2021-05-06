import stravaAPI_test as test
import StravaAPI as strava
import argparse

"""
Source: https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86
"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def useCLI(CLI=True, useFlag=1):
    if CLI is False:
        return useFlag
    else:
        parser = argparse.ArgumentParser(description="Enter task:\n 0: Test\n\n 1: 'Get all data \n\n 2: Test automatic token refresh")
        parser.add_argument('Task', metavar="Task", type=int,
                            help="Enter task. Default is 1.")
        args = parser.parse_args()
        task = vars(args)['Task']
        print(task)
        try:
            assert task in [0, 1, 2]
            return task
        except:
            print("Need 0, 1 or 2.")
            print("Running default task (task 1).")

    return useFlag


if __name__ == '__main__':
    useFlag = useCLI(CLI=True)
    print(useFlag)

    MasterFlag = {
        0: '0: Test',
        1: '1: Get all data',
        2: '2: Test automatic token refresh'
    }[useFlag]
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
