

# declare dataArray that will be filled with the data from the data.txt
# DISCLAIMER: I'm not sure yet if this is the smartest way to store the values
dataArray = []

# read in data
with open('./data.txt') as f:
    lines = f.readlines()

# split information: stride, array size and time per access
for line in lines:

    # a line looks like this: [2,16000,2.4983e-09],
    # so we would need to remove the first character and the last two to clean up
    cleanLine = line.lstrip('[')[:-3]

    # we can now split at the commas and get an array for each line
    cleanArray = cleanLine.split(',')

    # there are faulty arrays at the beginning and the end, so we have to filter them out
    if len(cleanArray) >= 3:

        # since all the values where strings, we need to convert them
        numericalArray = [int(cleanArray[0]), int(cleanArray[1]), float(cleanArray[2])]

        # and in the end we can add this array to our dataArray
        dataArray.append(numericalArray)

print(dataArray)
