programa {
  funcao inicio() {
   inteiro num1, num2

   escreva("Receba dois números inteiros: ")
   leia(num1,num2)

   escreva("Digite o primeiro número: ")
   leia(num1)

   escreva("Digite o segundo número: ")
   leia(num2)

  se(num1>num2){
    escreva("Num1 é maior que num2")
  }
  senao se(num2>num1){
    escreva("Num2 é maior que num1")
  }
  senao se(num1==num2){
    escreva("Os dois números são iguais")
  }

  }
  }
}
