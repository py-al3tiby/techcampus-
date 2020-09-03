print("##########################################")
print("#######################################")
print("####################################")
print("Crated by ./al3tiby0")
print("SN: mz511zm")
print("IG: _wwi")
print("####################################")
print("#######################################")
print("##########################################")
secret_code = 10

guess_counter =0

while guess_counter < 3:
    guess_number = int(input("Please Enter the guess number: "))
    if guess_number == secret_code :
        print("You win")
        break
    else:
        print("Try Agian")
    guess_counter = guess_counter + 1
