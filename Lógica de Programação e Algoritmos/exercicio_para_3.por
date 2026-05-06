programa {
  funcao inicio() {
    inteiro numero, fatorial=1

    escreva("Digite um número")
    leia(numero)

    para(inteiro i=numero;i>=1;i--){
      fatorial = fatorial * i 
    }
    escreva(numero,"! = ",fatorial)
  }
}
