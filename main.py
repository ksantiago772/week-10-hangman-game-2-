# from methods_help import method_help
# from functions import function
# from returnStuff import returnS
# from dynamic_functions import check_3Digits, all_positives
from function_interactions import mix_sticks, try_your_luck, verify_number
sticks = ["-", "--", "---", "----", "-----"]
my_mix = mix_sticks(sticks)
print(my_mix)
your_luck = try_your_luck()
print(your_luck)
verify= verify_number(my_mix, your_luck)
print(verify)
# method_help()
# function()
# returnS()
# sum = 526 + 345
# result = check_3Digits([55,99, 600])
# print(result)
# all_positives([50])