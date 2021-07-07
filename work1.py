# %%
import random
ALPHA="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ALPHA_LENGTH=len(ALPHA)-1
NUM=200
def promote_codes (length):
    code=[]
    for j in range(length):
        n=random.randint(0,ALPHA_LENGTH)
        code.append(ALPHA[n])
    code="".join(code)
    return code

if __name__ == "__main__":
    for i in range(NUM):
        codes=promote_codes (5)
        print("The activation code for customer No.%d is %s."%(i,codes))
    