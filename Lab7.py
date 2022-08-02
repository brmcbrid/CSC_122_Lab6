# CSC 122
# Print Largest & Smallest Value & Index in a List
# By Brian McBride

"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""
# Instructor's Solution
# define findLargest function here
def findLargest(sens):
    largest=sens[0];
    for i in range (len(sens)):
        if sens[i]>largest:
            largest=sens[i]
            index=i
    return [largest,index]

# define findSmallest function here
def findSmallest(sens):
    smallest=sens[0];
    for i in range (len(sens)):
        if sens[i]<smallest:
            smallest=sens[i]
            index=i
    return [smallest,index]
           
# defining main function
def main():
    # defining sensor list
    sensor=[76.25, 85.45, -45.90, 99.34, 72.20, -65.90, 66.33, 99.77, 88.5,
            -44.12, 45.75, 57.77, -88.42, 99.47, 75.75, 88.45, 65.64, 77.21, -24,62]
    highSensor=findLargest(sensor) # calling findLargest and passing sensor list
    lowSensor=findSmallest(sensor) # calling findSmallest and passing sensor list
    print(f"The highest sensor value read is at index {highSensor[1]} and is {highSensor[0]}")
    print(f"The lowest sensor value read is at index {lowSensor[1]} and is {lowSensor[0]}")

if __name__ == "__main__":#calling main function
    main()
