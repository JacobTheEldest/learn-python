'''
https://www.reddit.com/r/beginnerprojects/comments/1eqt8i/function_mean_median_and_mode/

MAIN GOAL

-Create three functions that allow the user to find the mean, median, and mode
of a list of numbers. If you have access or know of functions that already
complete these tasks, do not use them.

SUBGOALS

-In the mean function, give the user a way to select how many decimal places
they want the answer to be rounded to.

-If there is an even number of numbers in the list, return both numbers that
could be considered the median.

-If there are multiple modes, return all of them.

'''


#Return the sum of a list
def sum(nums):
    '''
    Argument should be a list of numbers
    '''
    
    #Calculate sum of list
    sum = 0
    for x in nums:
        sum += int(x)

    return sum

#Return mean of a list
def mean(nums, decs=3):
    '''
    Takes arguments in the form of (list_of_numbers, decimals to round at)
    '''
    
    return float('{:.{}f}'.format((sum(nums) / len(nums)), decs))

def median(nums):
    '''
    Argument should be a list of numbers.
    Returns both medians as a list, if the list is even.
    '''
    
    nums.sort()

    if len(nums) % 2 == 0:
        return [nums[int((len(nums)/2 - 1))], nums[int((len(nums)/2))]]
    else:
        return nums[len(nums)//2]

def mode(nums):
    '''
    Argument should be a list of numbers.
    '''

    #Pair each value of the list with the count for it
    count_dict = {}
    for x in nums:
        count_dict['{}'.format(x)] = nums.count(x)

    #Find the keys with the highest values
    mode_dict = {list(count_dict.keys())[0]: count_dict[list(count_dict.keys())[0]]}
    for y in list(count_dict.keys()):
        if count_dict[y] > mode_dict[list(mode_dict.keys())[0]]:
            mode_dict = {y: count_dict[y]}
        elif count_dict[y] == mode_dict[list(mode_dict.keys())[0]]:
            mode_dict[y] = count_dict[y]

    return sorted(mode_dict.keys())

#Ask for a list of numbers
num_list = []
print ('Please enter numbers one at a time. Enter any letter to quit.')
while True:
    num_in = input()
    if not num_in.isdigit():
        print('\n')
        break
    
    num_list.append(num_in)

#output
print('List:\t{}\n'.format(num_list))
print('Mean:\t{}'.format(mean(num_list)))
print('Median:\t{}'.format(median(num_list)))
print('Mode:\t{}'.format(mode(num_list)))
