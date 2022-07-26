#ifelse.py
score=int(input("점수 입력:"))

if 90<=score<=100:
    grace="A"
elif 80<=score<=90:
    grace="B"
elif 70<=score<=80:
    grace="C"
else:    
    grace="D"

print("등급은" , grace)
    
