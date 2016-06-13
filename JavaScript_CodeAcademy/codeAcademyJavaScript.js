//Qual é o seu nome?
//Oi! Vamos nos conhecer melhor. Qual é o seu nome?
//Instruções
//Escreva seu nome entre aspas, assim: "Ryan", então clique em "Salvar e Enviar Código".
"Pippo"
---------------------------------------------
//Descubra o comprimento
//Muito bom!
//Qual seria o comprimento do seu nome?

//Instruções
//Para descobrir o comprimento do seu nome, escreva-o entre aspas.
//Então, escreva um ponto e a palavra length, assim: "yourName".length
//No meu caso (meu nome é Leng) isso seria "Leng".length
"Pippo".length
--------------------------------------------
//Matemática básica
//Bom trabalho! Agora, vamos fazer um pouco de matemática. Você pode fazer contas com programação!

//Instruções
//Some quaisquer dois números, assim: 3 + 4
10 + 50
-------------------------------------------
//Números e mais
//Vê o que aconteceu? Você pode usar a linha de comando para realizar operações matemáticas básicas. Tente fazer mais algumas.

//Instruções
//Você pode usar * para multiplicação e / para divisão se quiser. Entre outra expressão válida para encerrar esta lição.
------------------------------------------
//O que estou aprendendo?
//Este é o JavaScript (JS), uma linguagem de programação. Há muitas linguagens, mas o JS tem muitos usos e é fácil de aprender.

//Para que podemos usar o JavaScript?

//fazer websites responder à interação do usuário
//criar apps e jogos (por ex. blackjack)
//acessar informações na internet (por ex. descobrir as palavras mais mencionadas no Twitter por tópico)
//organizar e apresentar dados (por ex. automatizar o trabalho com planilhas, visualização de dados)
//Instruções
//Clique em Salvar e Enviar Código para ver um exemplo de como o JavaScript pode ser interativo!
confirm('Isto e um exemplo do uso de JS para criar interação em um website. Clique em OK para continuar!');
------------------------------------------
//JavaScript Interativo
//O que acabamos de ver foi um exemplo divertido de como o JavaScript pode ser interativo. Agora tente você!

//Exemplos:

confirm("Me sinto ótimo!");
confirm("Estou pronto para ir.");

//Essas caixas podem ser usados em websites para confirmar coisas com os usuários.
//Você provavelmente já as viu aparecer quando tenta apagar coisas importantes, ou sair de um website sem salvar modificações.
//Instruções
//Escreva sua própria mensagem para o que você quer que o usuário confirme.
confirm("Hoje é quarta-feira?")
----------------------------------------
//O que é programação?
//Programar é como escrever uma lista de instruções para o computador, para que ele possa fazer coisas leagais com suas informações.

//Programas ainda não podem fazer sua cama, mas podem fazer contas, manter o controle da sua conta bancária, ou mandar uma mensagem para um amigo.

//Para fazer qualquer uma dessas coisas, o programa precisa de uma entrada. Você pode pedir por uma entrada com um prompt.

//Exemplos:

1. prompt("Qual é o seu nome?");
2. prompt("O que é Ubuntu?");

//Instruções
//Use o comando prompt para perguntar ao usuário de onde ele é. Consulte os exemplos acima para saber como fazer isso!
prompt("Você já vui o sol?");
prompt("O sol estava quente?");
-------------------------------------
//Tipos de Dados I e II: Números e Strings
//Dados vêm em diversos tipos. Você já usou dois deles!

//a. números são quantidades, como você já está acostumado. Você pode fazer contas com eles.

//b. strings são sequências de caracteres, como as letras a-z, espaços, e até mesmo números. Todos esses são exemplos de strings: "Ryan", "4" e "Qual e o seu nome?" Strings são extremamente úteis como identificadores, nomes, e conteúdo para seus programas.

//Para criar um número em seu código, simplesmente escreva um número com algarismos sem aspas: 42, 190.12334.

//Para escrever uma string, coloque as palavras entre aspas: "Qual é o seu nome?"

//Instruções
//Escreva uma string com pelo menos 3 palavras. Leia os exemplos de strings acima.
//Encontre o comprimento da string escrevendo um ponto e a palavra length, assim:

"string".length;
//Length conta quantos caracteres há na string, incluindo os espaços!
"Pippo bem legal".length
--------------------------------------
//Tipo de Dados III: Booleanos
//Bom trabalho! Agora vamos aprender sobre booleanos. Um booleano é verdadeiro (true) ou falso (false).

//Por exemplo, comparar dois números retorna um resultado true ou false:

23 > 10 é true
5 < 4 é false

//Instruções
//Vamos comparar dois números para retornar um resultado verdadeiro:

//Primeiro, escreva a string "Estou programando como um profissional"
//A seguir, encontre o comprimento da string usando .length
//Então, compare o comprimento da string para ver se ela tem mais do que 10 caracteres
"Estou programando como um profissional".length > 10
----------------------------------------
//Usando console.log
//Você pode ter notado que o interpretador não exibe tudo o que ele faz. Então, se quisermos saber o que você está pensando,
//às vezes temos que pedir a ele que fale conosco.

//console.log() tomará o que quer que esteja ente os parênteses o registrará (log) no console abaixo do seu código — é por isso que é chamado console.log()!

//Isso é comumente chamado exibição.

//Instruções
//Exiba as duas declarações console.log seguintes ao mesmo tempo. Digite uma na linha 1 e a outra na linha 2. Então, clique em Salvar e Submeter Código.

console.log(2 * 5)
console.log("Alô")
----------------------------------------
//Comparações
//Até agora aprendemos sobre três tipos de dados:

strings (por ex. "cachorros fazem au au!")
números (por ex. 4, 10)
booleanos (por ex. false, 5 > 4)
//Agora vamos aprender mais sobre operadores de comparação.

//Lista de operadores de comparação:

> Maior que
< Menor que
<= Menor ou igual a
>= Maior ou igual a
=== Igual a
!== Diferente de

//Instruções
//Tente usar cada um dos operadores acima.

//Selecione o operador correto de comparação para fazer cada uma das quatro exibirem true.
// Eis um exemplo de uso do operador maior que (>).
console.log(15 > 4); // 15 > 4 resulta em true, então true e exibido.

// Preencha com >, <, === de modo que o seguinte resulta em true:
console.log("Xiao Hui".length < 122);
console.log("Goody Donaldson".length > 8);
console.log(8*2 == 16);
-------------------------------------------
//Decisões, decisões
//Bom trabalho com as comparações! Agora vamos ver como podemos usar comparações para fazer perguntas com respostas "sim" ou "não".

//Digamos que queremos escrever um programa que pergunte se o seu nome tem mais do que 7 letras. Se a resposta for sim,
//podemos responder com "Seu nome é bem longo!" Podemos fazer isso com uma declaração if:

if( "myName".length >= 7 ) {
    console.log("Seu nome é bem longo!");
}

//Uma declaração if é composta pela palavra-chave if, uma condição como as que vimos antes, e um par de chaves { }.
//Se a resposta da condição for sim, o código dentro das chaves será executado.

//Instruções
//Examine a declaração if no editor.

//Na linha 1, adicione uma condição dentro dos parênteses ( ).
//Se a resposta à condição for sim, o código dentro das chaves será executado. Então use console.log na linha 2 para exibir uma string.
if ( "Pippo".length <= 5) {
    console.log( "Nome nananana!!" );
}
------------------------------------------
//Computadores são inteligentes
//Ótimo! Usamos uma declaração if para fazer algo se a resposta à condição for sim, ou verdadeira (true) como dissemos em JavaScript.

//Além de fazer algo quando a condição é true, podemos fazer outra coisa se a condição for false.
//Por exemplo, se seu nome tiver menos de 7 letras, podemos responder com "Seu nome é bem curto!" Podemos fazer isso usando uma declaração if / else:

if( "myName".length >= 7 ) {
    console.log("Seu nome é bem longo!");
}
else {
    console.log("Seu nome é bem curto!");
}

//Como antes, se a condição for true, então apenas o código dentro do primeiro par de chaves será executado. Caso contrário, a condição é false,
//então apenas o código dentro do segundo par de chaves depois da palavra-chave else será executada.

//No exemplo acima a condição "myName".length >= 7 resulta em false já que "myName" tem apenas 6 letras.
//Como a condição é false, apenas o código dentro das chaves depois da palavra-chave else é executado, e exibe Seu nome é bem curto!.

Instruções
Na linha 1, preencha uma condição que resultará em false
Preencha a porção else com um trecho de código (isso será executado se a condição for false). Use console.log para esta parte.
if ( "Jaquirana do Sul".length > 100)
{
    console.log("Vamos percorrer a primeira estrada!");
}
else
{
    console.log("É perto vamos por aqui!");
    // O que devemos fazer a condicao for falsa? Escreva aqui:
}
---------------------------------------
//Mais prática com condicionais
//Agora vamos praticar, usando declarações if/else . Faça o máximo que puder por conta própria, mas se precisar de um lembrete,
//clique no botão "Problemas? Leia uma dica!" abaixo.

//Instruções
//Escreva uma declaração if/else como fizemos no último exercício. Eis como o código se parece:

if (condição)
{
    // se a condição for verdadeira
    // execute este código
}
else // "caso contrário"
{
    // execute este código
}
//Se sua condição for true, use console.log para exibir "A condição é verdadeira".

//Caso contrário (else) quando ela for false, use console.log para exibir "A condição é falsa".
//Tenha certeza de que sua condição seja false, para que seu programa exiba "A condição é falsa".

if (105 > "Estrada para o futuro") {

}
else {

}
--------------------------------------
//Matemática e o resto
//Vamos conhecer um símbolo interessante chamado resto. Quando % é usado entre dois números, o computador divide o primeiro pelo segundo, e então retorna o resto da divisão.

//Então, se fizermos 23 % 10, dividimos 23 por 10, o que é igual a 2 com resto 3. Então, 23 % 10 é igual a 3.

//Mais exemplos:

17 % 5 é igual a 2

13 % 7 é igual a 6

//Instruções
//Use console.log e resto três vezes para exibir o resto das seguintes equações:

//a. 14 / 3
//b. 99 / 8
//c. 11 / 3
// Abaixo há um exemplo da exibição do resto de 18/4 usando o operador resto:
// console.log(18 % 4);
console.log(14 % 3)
console.log(99 % 8)
console.log(11 % 3)
--------------------------------------
//Resto e if / else
//Então, porque aprender a calcular o resto? Para começar, ele é bom para testar a divisibilidade. Considere 30 % 10. O que ele retorna? Não há resto, então 0.

//E quanto a 9 % 3? Também 0.

//Podemos usar restos em comparações, assim:

//10 % 2 === 0 é true
//7 % 3 === 0 é false porque há um resto de 1.
//Instruções
//Vamos fazer a declaração if/else exibir "O primeiro número é par".

//Edite a linha 5 adicionando uma comparação que resulta em true.
//Na comparação, use um resto e um número par, como fizemos no exemplo acima.
if( "Pipo Pippo".length % 2 == 0 ) {
    console.log("O primeiro número é par");
} else {
    console.log("O primeiro número é impar");
}
-----------------------------------
//Substrings
//Aprendemos alguns meios de manipular números. E quanto a manipular strings?

//Às vezes você não quer exibir toda a string, apenas uma parte dela. Por exemplo, você pode configurar sua caixa de entrada do Gmail para exibir os primeiros 50 caracteres, de cada mensagem, para que possa ver do que se tratam. Esse trecho é uma substring da string original (a mensagem inteira).

//Código:

//"uma palavra".substring(x, y) em que x é onde você começa a cortar e y é onde você termina de cortar a string original.

//A parte dos números é um pouco estranha. Para selecionar o "he" em "hello", você escreve:

//"hello". substring(0, 2);
//Cada caractere é uma string e indexada a partir do 0, assim:

0 1 2 3 4
 | | | | |
 h e l l o
//A letra h está na posição 0, a letra e está na posição 1, e assim por diante.

//Portanto, se você começar na posição 0, e cortar na posição 2, tem só he

//Mais exemplos:

//1. As 3 primeiras letras de "Batman"
"Batman".substring(0,3);

//2. Da 4a até a 6a letra de "laptop"
"laptop".substring(3,6);

//Instruções
//Encontre a 4a até 7a letras da string "wonderful day".
"wonderful day".substring(3,7);
--------------------------------------
//Mais prática com substrings
//Conseguir o posicionamento das letras na substring é complicado! Vamos garantir que entendemos tudo.

//Lembre-se que cada caractere em uma string é numerada a partir do 0. Então, para a palavra "hello", a letra h está na posição 0, a letra e está na posição 1 e assim por diante.

Instruções///
//Usando console.log, em três linhas separadas, exiba as substrings das seguintes strings.

//a. "Jan" em "Janeiro"
//b. "Melbourne e" em "Melbourne e otima" (note o espaço!)
//c. "burgers" em "Hamburgers"
console.log("Janeiro".substring(0,3));
console.log("Melbourne é otima".substring(0,11));
console.log("Hamburgers".substring(3,10));
-------------------------------------
//Variáveis
//Já aprendemos como fazer algumas algumas coisas: compor strings, encontrar o comprimento de strings, encontrar o caractere na n-ésima posição, fazer contas básicas. Nada mal para um dia de trabalho!

//Para criar programas mais complexos, precisamos de um modo de salvar os valores do seu código. Fazemos isso definindo uma variável com um nome específico e sensível à caixa alta/baixa. Depois que você cria (ou declara) uma variável como tendo um nome em particular, pode chamar esse valor digitando o nome da variável.

//Código:

//var varName = data;

//Exemplo:

//a. var myName = "Leng";
//b. var myAge = 30;
//c. var isOdd = true;

//Instruções
//Crie uma variável chamada myAge e digite sua idade.
var myAge = 15
console.log(myAge);
-------------------------------------
//Mais Prática com Variáveis
//Vimos como criar uma variável. Mas como as usamos? É interessante pensar que sempre que você digita o nome da variável, está pedindo ao computador para trocar o nome da variável pelo valor da variável.

//Por exemplo:

//var myName = "Steve Jobs";

//myName.substring(0,5)

//Examine a segunda linha acima. Você pediu ao computador para trocar myName por Steve Jobs, então

//myName.substring(0,5)

//se torna

//"Steve Jobs".substring(0,5)

//que resulta em Steve.

//Outro exemplo

//var myAge = 120;

//O que é

//myAge % 12 ? Leia a dica para verificar sua resposta.

//Então, a variável armazena o valor da variável, seja este um número ou uma string. Como você verá logo, isso torna escrever programas muito mais fácil!

//Instruções
//Siga as instruções nos comentários do código para continuar.

// Declare uma variável na linha 3 chamada
// myCountry e atribua a ela uma string.
myCountry = "Java é o the best!!"

// Use console.log para exibir o comprimento da variável myCountry.
console.log( myCountry.length );

// Use console.log para exibir as tres primeiras letras de myCountry.
console.log( myCountry.substring(0,3) );
----------------------------------------
//Mude os valores das variáveis
//Até agora, vimos
//a. como criar uma variável
//b. como usar uma variável

//Agora vamos ver como mudar o valor de uma variável. O valor de uma variável é mudado facilmente. Faça de conta que você está criando uma nova variável enquanto usa o mesmo nome da variável já existente!

//Exemplo:

//var myAge = "Trinta";
//digamso que eu fiz aniversário e quero mudar minha idade na variável.
//myAge = "Trinta e um";

//Agora o valor de myAge é "Trinta e um"!

//Instruções
//Siga as instruções na linha 1, linha 3, linha 5 e linha 8. Estamos usando esse método para mostrar a você a ordem na qual você diz ao computador o que fazer é muito importante.

// Na linha 2, declare uma variavel myName e atribua a ela seu nome.
myName = "Pippo The Best"
// Na linha 4, use console.log para exibir a variavel myName.
confirm("Meu nome completo é :" + myName);
console.log(myName);
// Na linha 7, mude o valor de myName para ser apenas as primeiras 2 letras do seu nome.
myName = myName.substring(0,2);

// Na linha 9, use console.log para exibir a variável myName.
confirm("As 2 primeiras letras do meu nome são: " + myName);
console.log(myName);
--------------------------------------
//Conclusão: Parte 1
//Vamos fazer uma revisão rápida!

//Tipos de dados

strings (por ex. "cachorros fazem au au!")
números (por ex. 4, 10)
booleanos (por ex. false, 5 > 4)
//Variáveis
//Armazenamos valores de dados em variáveis. Podemos trazer de volta os valores dessas variáveis digitando o nome da variável.

//Manipulando números e strings

//comparações (por ex. >, <=)
resto (%)
comprimento da string(por ex. "Emily".length;)
substrings (por ex. "oi".substring(0, 1);)
console.log( )
//Exibe no console o que quer que colocamos entre os parâmetros.

//Instruções
//Na linha 1, crie uma variável myColor e atribua a ela uma string.
//Na linha 2, exiba o comprimento de myColor no console.
myColor = "Marfim"
console.log(myColor.length);
---------------------------------
// Uma funcao tem esta aparencia:

var divideByThree = function (number) {
    var val = number / 3;
    console.log(val);
};

// Na linha 12, chamamos a funcao pelo nome
// Aqui, ela e chamada de 'dividebythree'
// Dizemos ao computador qual e o numero de entrada (ou seja, 6)
// O computador entao executa o codigo dentro da funcao!
divideByThree(-2);
--------------------------------
// Mostramos abaixo a função greeting!
// Veja a linha 7
// Podemos unir strings usando o sinal de mais (+)
// Leia a dica para mais detalhes sobre como isso funciona.

var greeting = function (name) {
    console.log("Que bom ver você," + " " + name);
};

// Na linha 11, chame a função greeting!
greeting("PippoLino!");
-------------------------------
// Escreva sua funcao foodDemand abaixo
// Última dica: no seu bloco reutilizável de código, finalize cada linha com um
// ponto e virgula (;)
var foodDemand = function(food){
    console.log("Quero comer" + " " + food);
    };
foodDemand("HotDog");
------------------------------
//Juntando tudo
//Por que o código está organizado como está nas linhas 2-5?

//O computador pode entender o código sem os espaços. Mas essa prática torna a edição muito mais fácil e é uma das melhores práticas.

//Eu devo colocar um ponto e vírgula no fim de cada linha de código depois de cada linha de código no bloco reutilizável? E no final da função toda?

//Sim. Adicione um ponto e vírgula no final de cada linha de código (dentro do { }) e depois da função toda (depois do { }). O ponto e vírgula age como um ponto em uma frase. Ele ajuda o computador a saber onde estão os pontos de parada do código.

//Instruções
//Uma parte importante da programação é a depuração. Isso significa encontrar que diabos deu errado com seu código. Por que ele não funcionou?

//Examine a linha 9.Ela contém muitos erros de sintaxe. Vê como a falta de espaçamento torna a depuração mais difícil?
//Conserte a função na linha 9. Tenha certeza de que a sintaxe está correta. Tenha certeza de que ela tem boa aparência.
//Chame a função greeting depois que ela estiver consertada! Não esqueça de passar para ela um nome específico.

// Funcao bem escrita:
var calculate = function (number) {
    var val = number * 10;
    console.log(val);
};

// Funcao mal escrita com erros de sintaxe!

var greeting = function(name){
    console.log(name)
};
greeting("HotDog");
------------------------------------
//Não Se Repita (N.S.R.)
//O princípio N.S.R. é realmente muito importante em programação. Nada de repetição!

//Sempre que você se encontrar digitar a mesma coisa mas modificando apenas uma pequena parte, provavelmente pode usar uma função.

//A pequena parte que você modifica será o parâmetro. E a parte que você fica repetindo será o código no bloco reutilizável - o código dentro de { }.

//Instruções
//Você é uma criatura de hábitos. Toda semana você compra 5 laranjas. Mas os preços das laranjas mudam o tempo todo!

//Você quer declarar uma função que calcule o custo de comprar 5 laranjas.
//Então, você quer calcular o custo das 5 juntas.
//Escreva uma função que faça isso, chamada orangeCost().
//Ela deve tomar um parâmetro, o preço de uma laranja, e multiplicá-lo por 5.
//Ela deve enviar o resultado da multiplicação para o console.
//Chame a função, com as laranjas custando 5 reais cada.

var orangeCost = function(cost){
	console.log(cost * 5);
}

orangeCost(1,30);
----------------------------------
var cities = ["Melbourne", "Amman", "Helsinki", "NYC",1,7,999,3003,600,77,55,"Take", "Speling"];

for (var i = 0; i < cities.length; i++) {
    console.log("I gostaria de visitar " + cities[i]);
}
---------------------------------------
/*Seu segundo laço "for"
Ok! Ultima etapa: adicione outro laço for, dessa vez dentro do corpo da sua declaração if (entrs os {}s do if).

Esse laço garantirá que cada caractere do seu nome seja empurrado (push) para o array final. A declaração if diz: "Se encontrarmos a primeira letra do nome, comece o segundo laço for!" Este laço diz: "Vou adicionar caracteres ao array até atingir o comprimento do nome do usuário". Então, se seu nome tiver 11 letras, seu laço deve adicionar 11 caracteres a hits se ele encontrar a primeira letra de myName em text.

Para seu segundo laço for, tenha o seguinte em mente:

Primeiro, você deve fazer o iterador do segundo laço começar no primeiro, para que ele comece onde o primeiro parou. Se seu primeiro laço começar em

for(var i = 0; // resto da configuracao do laco
seu segundo deve ser parecido com

for(var j = i; // resto da configuracao do laco
Segundo, pense bem em como seu laço deve ser interrompido. Leia a Dica se precisar de ajuda!

Finalmente, no corpo do seu laço, faça o programa usar o método .push() de hits. Assim como as strings e arrays têm um método .length, arrays têm um método .push() que adicione o que estiver entre parênteses para o fim do array. Por exemplo,

newArray = [];
newArray.push('alo');
newArray[0];   // e igual a 'alo'
Instruções
OK! Vá em frente e adicione o segundo laço for dentro do corpo da sua declaração if.*/



/*jshint multistr:true */
text = "Pippo Lontra Pippo Texto Piipo \
Pippo Lontra Texto Piipo Pippo Lontra \
Pipico Nanico Pippo Pipico ";
myName = "Pippo";
hits = [];

for (var x = 0;x <= text.length; x++){
    if (text[x] === myName[0]){
         for(var z = x;z < (myName.length + x); z++) {
         	if (text[z] === myName[z - x]){
         		hits.push(text[z]);
         	}
        }
    }
}

if(hits.length === 0){
    console.log("Seu nome nao foi encontrado");
    }
else {
    console.log(hits);
 }
-----------------------------------------------------------
//Já que estamos falando disso
//Bom trabalho com os laços "for"! Como lembrete, a sintaxe dos laços "for" é assim:

for (var i = start; i < end; i++) {
  // faça alguma coisa
}

//A variável de contagem "i" é inicializada em "start", e encerra o laço quando atinge "end."

//Mas e se você não soubesse antes quando o laço deve parar? Digamos, por exemplo, que você queira continuar escolhendo cartas de um baralho até conseguir uma carta de espadas. Você não sabe quantas cartas precisará escolher, então um laço "for" não vai servir.

//Em situações como essas, em que você não sabe com antecedência quando interromper o laço, podemos usar um laço "while".

//Observe o laço "while" no editor. Você pode adivinhar o que ele fará? Clique em "Salvar e Enviar Código" quando achar que já sabe! (A resposta está na Dica).

//Não se preocupe com a parte sobre "Math.floor" agora — vamos explicá-la logo!

var coinFace = Math.floor(Math.random() * 2);

while(coinFace === 0){
	console.log("Cara! Jogando de novo...");
	var coinFace = Math.floor(Math.random() * 2);
}
console.log("Coroa! Terminamos.");
-----------------------------------------------------------
//Sintaxe de while
//O laço while é ideal quando você quer usar um laço, mas não sabe quantas vezes precisará executar o laço.

//No exemplo que acabou de ver, o computador jogou uma moeda aleatoriamente: enquanto (while) a moeda der cara (coin igual a 1), ele deve jogar de novo, e deve parar quando conseguir cara (coin igual a 0). Já que a jogada é aleatória, não sabemos com antecedência de quantos laços vamos precisar.

//A sintaxe se parece com isto:

while(condition){
    // Faca alguma coisa!
}

//Enquanto a condicao for verdadeira (true), o laço vao continuar. Assim que ela for falsa (false), ele parará (Quando você usa um número em uma condição como fizemos antes, o JavaScript entende que 1 é verdadeiro e 0 é falso.)

//Já que você já dominou os laços for, essa sintaxe mais simples deve ser moleza para você.

//Instruções
//Tente você mesmo — complete o laço while no editor, de modo que ele exiba "Estou aprendendo sobre lacos while!".
//Faça isso adicionando a condição entre os parênteses — não mude a linha 5, ou pode entrar em um laço infinito!

var understand = true;

while(understand === true){
	console.log("Estou aprendendo sobre laços while!");
	understand = false;
}
-------------------
//Brevidade é a alma da programação
//Você deve ter notado que quando atribuímos à uam variável o valor booleano true, verificamos essa variável diretamente — 
//não nos preocupamos com ===. Por exemplo,

var bool = true;
while(bool){
    //Faca alguma coisa
}
//é o mesmo que

var bool = true;
while(bool === true){
    //Faca alguma coisa
}
//mas a primeira e mais fácil de digitar. Adquira o hábito de digitar apenas o necessário, e nada mais!

//Se você estiver usando números, como fizemos antes, você poderia usar:

var myNumber = 1;
while(myNumber) {
    // Faca alguma coisa!
}

//Instruções
//Nós escrevemos a versão menos sucinta no editor. Transforme-a em uma versão mais elegante!
var bool = true;

while(bool){
    console.log("Menos e mais!");
    bool = false;
}
--------------------------
//A Prática traz a perfeição
//OK. Hora de criar um laço while do zero!

//Criamos uma função, loop na qual você deve escrever seu laço while, e também criamos o laço vazio.

//Lembre-se de estabelecer a condição que você está checando fora do laço — se você o fizer dentro do laço, ela continuará sendo reiniciada e o laço vai continuar para sempre!

//Instruções
//Escreva um laço while envie "Estou em um laco!" para o console três vezes. Você pode fazer isso de qualquer modo que quiser,
//mas NÃO chamado console.log três vezes.
//Leia a Dica se precisar de ajuda!
nXvezes = 0;

var loop = function(){
	while(nXvezes <> 3){
        console.log("Estou em um laço!");
        nXvezes++;
	}
};

loop();
--------------------------
//Voando solo
//Bom trabalho, vamos tentar outro. Dessa vez, sem ajuda! (Bem, um pouco de ajuda — leia a Dica se precisar de ajuda).

//Instruções
//Dentro da função soloLoop, escreva um laço while que tome uma condição inicial que seja true. Seu laço deve enviar "Repetiu uma vez!"
//para o console e então mudar a condição inicial para false.

//TENHA CERTEZA de igualar sua condição a false no corpo do laço. Caso contrário, ele se repetirá para sempre!
xSolo = true;

var soloLoop = function(){
  //Seu codigo vem aqui!
  while(xSolo){
  	console.log("Repetiu uma vez!");
  	xSolo = false;
  }

};

soloLoop();
--------------------------
//Quando usar `while` e quando usar `for`
//Como mencionamos, laços for são ótimos para repetir a mesma tarefa repetidamente quando você já sabe quantas vezes terá que repetir o laço.
//Por outro lado, laços while são ideais quando você precisar repetir, mas não sabe com antecedência quantas vezes.

//Mas, como você viu, você pode combinar um laço while com uma variável contador para fazer o mesmo tipo de trabalho que um laço for faz.
//Nesses casos, muitas vezes é uma questão de preferência.

//Instruções
//Escreva dois laços no editor: um while, um for. Não há restrições aqui;
//apenas tenha certeza de a sintaxe dos seus laços esteja correta, e tenha o cuidado de evitar os laços infinitos!
xWilhe = 0;
xFor = 5;

var lWhile = function(LWnumber){
	while(LWnumber >= xWilhe){
		console.log("Laço While!!");
		LWnumber--;
	}
}

for (var lFort = xFor; lFort > 0; lFort--){
	console.log("Laço For!!");
}
lWhile(3);
--------------------
//O laço `do`/`while`
//Às vezes você vai querer garantir que seu laço rode pelo menos uma vez. Quando este for o caso, você quer um laço while modificado chamado laço do/while.

//Este laço diz: "Ei! Faça isso uma vez, e então verifique a condição para ver se devemos continuar com o laço". Depois disso, é apenas um whilenormal: o laço continuará enquanto a condição sendo avaliada for verdadeira.

//Instruções
//Clique Salvar e Enviar Código para ver o laço em ação. Ele roda uma vez porque do diz para ele fazer isso, mas não se repete, porque loopCondition é false!
loopCondition = false;

do {
	console.log("Vou interromper o laço porque minha condicao é " + String(loopCondition) + "!");
} while (loopCondition);
-----------------------------
//Para aprender, você precisa fazer
//Sua vez! Agora que viu como os laços do/while funcionam, você pode escreve um com facilidade (Leia a Dica se precisar refrescar a memória sobre a sintaxe!).

//Seu laço deve exibir uma string à sua escolha no editor uma vez.
//Lembre-se: tenha certeza de estabelecer sua condição while de modo que ela se torne false, ou o laço se repetirá para sempre!

//Instruções
//Escreva um laço do/while dentro da função que criamos para você, getToDaChoppa.
//A função deve exibir uma string à sua escolha no console. Faça (do) isso agora!
vValueChoppa = false;

var getToDaChoppa = function(){
	do{
		console.log("Fiz a primeira vez e irei fazer varias outras!");
	}
	while (vValueChoppa){
		vValueChoppa = true;
		}
};

getToDaChoppa();
---------------
//Revisão
//Excelente trabalho! Você aprendeu todos os laços que existem: for, while, e do.

//Instruções
//Para finalizar e provar que domina os laços, escreva três laços com sintaxe correta no editor: um for, um while e um do. Cuidado com os laços infinitos!

xWilhe = 0;
xFor = 5;
vValueChoppa = false;

var lWhile = function(LWnumber){
	while(LWnumber >= xWilhe){
		console.log("Laço While!!");
		LWnumber--;
	}
}

for (var lFort = xFor; lFort > 0; lFort--){
	console.log("Laço For!!");
}
lWhile(3);

var getToDaChoppa = function(){
	do{
		console.log("Fiz a primeira vez e irei fazer varias outras!");
	}
	while (vValueChoppa){
		vValueChoppa = true;
		}
};

getToDaChoppa();
----------------------
//O que você vai criar
//Agora que sabemos como usar laços "while", vamos combiná-los com outras declarações de controle de fluxo (como if/else) para criar um pequeno jogo em que combatemos um dragão.

//Nesse jogo, você vai combater um dragão. São precisos 4 golpes para matá-lo, e se você errar um só golpe, o dragão vai derrotá-lo!

//Instruções
//Observe o código no editor. Você entende como ele funciona? (Não se preocupe se não entender — vamos estudá-lo passo a passo!).

//Execute-o algumas vezes para ver como se sai contra o dragão!

var slaying = true;
// Um pouco de mágica matemática nova para calcular as chances
// de atingir o dragão. Vamos falar disso logo!
var youHit = Math.floor(Math.random() * 2);
var damageThisRound = Math.floor(Math.random() * 5 + 1);
var totalDamage = 0;

while (slaying) {
  if (youHit) {
    console.log("Você atingiu o dragão e causou " + damageThisRound + " de dano!");
    totalDamage += damageThisRound;

    if (totalDamage >= 4) {
      console.log("Você conseguiu! Voce matou o dragao!");
      slaying = false;
    } else {
      youHit = Math.floor(Math.random() * 2);
    }
  } else {
    console.log("Você foi derrotado pelo dragão! Ficou torrado.");
    slaying = false;
  }
}