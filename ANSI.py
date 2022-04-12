#/033[Style;Text;Backgroundm
#/033[0;33;44m
# style texts:
# 0 --> None
# 1 --> Bold
# 4 --> Underline
# 7 --> Negative (Background-->Text;Text-->Background)
# Text types: 30-37
# Back types: 40-47
print('\033[1;31;40mSuck it')
print('\033[4;30;47mSuck it\033[m')
print('\033[32mSay \033[mmy \033[35mname')