programa {
  funcao inicio() {
 real raio, altura, area, volume, pi = 3.14

 escreva("Digite o raio: ")
 leia(raio)

 escreva("Digite a altura: ")  
 leia(altura)

 area = 2*pi* raio * (raio + altura )
 escreva( " A area é:", area )
 volume = pi * raio * altura 
 escreva(" O volume é :" , volume )
  }
}
