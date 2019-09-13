# Get input:

# n: number of timestamps at which event Y occurs,
# p: % rate at which segment [t1, t2) is being sped-up by,
# k: duration of the sped-up video,
# tn: list of timestamps at which event Y occurs
n, p, k = [float(number) for number in input().split()]
tn = [float(number) for number in input().split()]

# Create list and store the duration of each segment in it:

# Create a segment duration list, a variable for increasing the rate at which the duration of each segment will stretch
# and a memory variable to store the previous timestamp
segments = list()
rate = 100.0
previous_tn = 0.0
# Go over each timestamp to calculate the original duration of each segment (except for the last one)
# and append the each result to the segments duration list
for segment in range(int(n)):
    segments.append((tn[segment]-previous_tn)*(rate/100.0000))
    previous_tn = tn[segment]
    rate += p
# Calculate the duration of the last segment
segments.append((k-previous_tn)*(rate/100.0))
# Sum the duration of all segments and print it
print(sum(segments))