# mean
def mean(numbers):
  return sum(numbers) / len(numbers)

  # median

def median(numbers):
    numbers.sort()
    n=len(numbers)
    mid=n//2

    if n % 2==0:
         (numbers[mid-1] + numbers[mid]) / 2
    else:
        return numbers[mid]

    # Range
def range(list):
      return max(list)-min(list)

  #mode
def mode (list):
  return max((list), key=list.count)

   # calling function

list=[1,2,3,4,5,5,6,7,8,9,10]
print("Mean",mean(list))
print("Median",median(list))
print("Range", range(list))
print("Mode",mode(list))