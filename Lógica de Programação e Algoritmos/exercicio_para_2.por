programa {
  funcao inicio() {
    inteiro inicio, fim, soma_pares = 0

   escreva("Digite o número inicial: ") 
   leia(inicio)

   escreva("Digite o número final: ")
   leia(fim)

   para(inteiro i=1;i<=10;i++){
    se(i%2 == 0){
      soma_pares = soma_pares + i
    }

   }
   escreva("A soma dos pares é:" ,soma_pares)
  }
}
