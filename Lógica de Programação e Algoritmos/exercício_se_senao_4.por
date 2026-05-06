programa {
  funcao inicio() {
    inteiro lado1, lado2, lado3

    escreva("Digite o lado um")
    leia(lado1)

    escreva("Digite o lado dois")
    leia(lado2)

    escreva("Digite o lado três")
    leia(lado3)

    se(lado1==lado2 e lado2==lado3 e lado3 ==lado1){
      escreva("Equilátero")
    }
    senao se(lado1==lado2 ou lado2==lado3 ou lado3==lado1){
      escreva("Isóceles")
    }
      senao se(lado3!=lado1 e lado2!=lado1 e lado3!=lado2){
    escreva("Escaleno")
    }
    }
}
