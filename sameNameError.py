def spam():
    print(eggs)     #ERROR!
    eggs = "Spam local"

eggs = "global"
spam()