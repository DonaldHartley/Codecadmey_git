def ces_cyp_decrypt(text, offset):
    alpha_l = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    spec_chars = " `~!@#$%^&*()_+-=[]\\{}|;\'\":,./<>?0123456789"
    decrypted_text=""
    for char in text:
        if char in spec_chars:
            decrypted_text += char
        elif char in alpha_l:
            index = alpha_l.find(char,26,53)
            decrypted_text += alpha_l[index+offset]
        elif char in alpha_u:
            index = alpha_u.find(char,26,53)
            decrypted_text += alpha_u[index+offset]
    return decrypted_text

def ces_cyp_encrypt(text, offset):
    alpha_l = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    spec_chars = " `~!@#$%^&*()_+-=[]\\{}|;\'\":,./<>?0123456789"
    encrypted_text=""
    for char in text:
        if char in spec_chars:
            encrypted_text += char
        elif char in alpha_l:
            index = alpha_l.find(char,26,53)
            encrypted_text += alpha_l[index-offset]
        elif char in alpha_u:
            index = alpha_u.find(char,26,53)
            encrypted_text += alpha_u[index-offset]
    return encrypted_text

vishals_tm = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for i in range(1,26):
    print(i, ces_cyp_decrypt(vishals_tm,i))

def vig_cyp_decrypt(text, keyword):
    alpha_l = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    spec_chars = " `~!@#$%^&*()_+-=[]\\{}|;\'\":,./<>?0123456789"
    decrypted_text=""
    key_index = 0
    offset = 0
    
    for char in text:
        if key_index == len(keyword):
            key_index = 0
            
        if keyword[key_index] in alpha_l:
            offset = alpha_l.find(keyword[key_index],0,26)
        elif keyword[key_index] in alpha_u:
            offset = alpha_u.find(keyword[key_index],0,26)
        
        if char in spec_chars:
            decrypted_text += char
        elif char in alpha_l:
            index = alpha_l.find(char,26,53)
            decrypted_text += alpha_l[index-offset]
        elif char in alpha_u:
            index = alpha_u.find(char,26,53)
            decrypted_text += alpha_u[index-offset]
        key_index +=1
    return decrypted_text

def vig_cyp_encrypt(text, keyword):
    alpha_l = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    spec_chars = " `~!@#$%^&*()_+-=[]\\{}|;\'\":,./<>?0123456789"
    encrypted_text=""
    key_index = 0
    offset = 0
    
    for char in text:
        if key_index == len(keyword):
            key_index = 0
            
        if keyword[key_index] in alpha_l:
            offset = alpha_l.find(keyword[key_index],0,26)
        elif keyword[key_index] in alpha_u:
            offset = alpha_u.find(keyword[key_index],0,26)
        
        if char in spec_chars:
            encrypted_text += char
        elif char in alpha_l:
            index = alpha_l.find(char,26,53)
            encrypted_text += alpha_l[index+offset]
        elif char in alpha_u:
            index = alpha_u.find(char,26,53)
            encrypted_text += alpha_u[index+offset]
        key_index +=1
        
    return encrypted_text

#add more logic to detect problems in keywords and special charcters
