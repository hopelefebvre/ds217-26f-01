from operator import add


measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# Replace this scaffold output with your calculation, loop, decision, and summary.
review_threshold = int(review_threshold_text)
total = 0
review_count = 0
for measurement in measurements:
    total += measurement
    if(measurement >= review_threshold):
        label = "review"
    else:
        label = "within range"
    if label == "review":
        review_count += 1
    print("Measurement: " + str(measurement) + " " + str(label))
mean = total / len(measurements)
print("Count: " + str(len(measurements)))
print("Total: " + str(total))
print("Mean: " + str(mean))
print("Review count: " + str(review_count))