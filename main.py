print(r'''
      
 _____                                  _____  _         _                 
/  __ \                                /  __ \(_)       | |                
| /  \/  __ _   ___  ___   __ _  _ __  | /  \/ _  _ __  | |__    ___  _ __ 
| |     / _` | / _ \/ __| / _` || '__| | |    | || '_ \ | '_ \  / _ \| '__|
| \__/\| (_| ||  __/\__ \| (_| || |    | \__/\| || |_) || | | ||  __/| |   
 \____/ \__,_| \___||___/ \__,_||_|     \____/|_|| .__/ |_| |_| \___||_|   
                                                 | |                       
                                                 |_|                       
''')


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(message, shift):
    
    word = ''

    for char in message:
        if char.isalpha():
            new_position = letters.index(char) + shift 
        
        
        if new_position <= len(letters) and char.isalpha():   
             word += letters[new_position]
            #print(letters[new_position])

        elif char == " ":
            word += char
        
        else: 
            out_of_range_positions = new_position % 26
            
            word += letters[out_of_range_positions]
            #print(letters[out_of_range_positions])

    return word
      

def decrypt(message, shift):
        
        word = ''
        
        for char in message:
            if char.isalpha():  
                new_position1 = (letters.index(char) - shift) 
                new_position1 %= len(letters)
                word += letters[new_position1]
            elif char == " ":
                word += " "

        return word
    

while_loop_bool = True
while while_loop_bool:
    process_type = input("Type 'encode' to encypt, type 'decode' to decrypt: \n")

    message = input("Type your message: \n")

    shift = input("Type the shift number: \n")


    if process_type.lower() == 'encode':
        encry = encrypt(message, int(shift))
        print(f"Here is youre message encrypted: \n{encry}")

    elif process_type.lower() == 'decode':
        decry = decrypt(message, int(shift))
        print(f"Here is youre message encrypted: \n{decry}")

    

    restart = input("Type yes if you want to start again: \n")

    if restart.lower() != "yes":
        while_loop_bool = False







