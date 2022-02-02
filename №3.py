for nums in range(1,101):
    new_list = list(str(nums))
    if int(new_list[-1]) == 1 and nums != 11:
        print('{} процент'.format(nums))
    elif int(new_list[-1]) > 1 and int(new_list[-1]) < 5:
        if nums > 10 and nums <15:
            print('{} процентов'.format(nums))
        else:
            print('{} процента'.format(nums))
    else:
        print("{} процентов".format(nums))