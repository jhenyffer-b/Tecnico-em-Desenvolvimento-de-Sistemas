ladoA = int(input("Digite o lado A: "))
ladoB = int(input("Digite o lado B: "))
ladoC = int(input("Digite o lado C: "))

if((ladoA + ladoB > ladoC)> ladoC and (ladoA+ladoC)>ladoB and (ladoB+ladoC)>ladoA):  
 if(ladoA == ladoB and ladoB == ladoC and ladoC == ladoA):
    print("Equilátero")
 elif(ladoA != ladoB and ladoB != ladoC and ladoC != ladoA):
    print("Escaleno")
 else:
   print("Isóceles")
else:  
  print("O triângulo não existe!") 
    
   

