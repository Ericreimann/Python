a = "1;2;3;4;8;9;10"
b= "1;6;3;9;0"
c= "6;7;9;10"

def test(s):
    s = s.replace(";"," ")
    
    print(s)
    if s.isnumeric():
        anterior = s[0]
        print(anterior)
        for n in s:
            if n < anterior:
                return False
            else:
                anterior = n
        return True
    else:
        return False

print("Sequencia" if test(a) else "Não sequencial")
print("Sequencia" if test(b) else "Não sequencial")
print("Sequencia" if test(c) else "Não sequencial")