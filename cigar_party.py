def cigar_party(cigars,is_weekend):
    if is_weekend:
        return True
    if(cigars>=40 and cigars<=60):
        if is_weekend==False:
            return True
    else:
         return False

print(cigar_party(30,False))
print(cigar_party(50, False))
print(cigar_party(70, True))
print(cigar_party(60,False))
