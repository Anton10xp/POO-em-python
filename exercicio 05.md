Exercício 5: folha de pagamento de uma empresa

Crie o arquivo `Ex05_Folha_pagamento.py`. Use o exercício 4 como referência, mas escreva uma implementação independente. O objetivo é revisar abstração, herança e encapsulamento e praticar composição: um objeto Empresa terá uma lista de objetos Funcionario.

Crie uma classe abstrata `Funcionario`, com nome e salário base. Use `@property` para consultar e alterar o salário base, mantendo o valor em um atributo privado. Escolha um único nome para a propriedade e use esse nome também no construtor. O nome não pode ficar vazio ou conter somente espaços, e o salário base não pode ser negativo. Valores inválidos devem gerar `ValueError`, tanto na criação quanto nas alterações, sem substituir um valor anterior válido.

Declare o método abstrato `salario_final(self)`. Ele deve retornar um número, sem imprimir mensagens. Não permita criar objetos diretamente de `Funcionario`.

Implemente duas subclasses. `Gerente` recebe um bônus fixo, e seu salário final corresponde ao salário base mais o bônus. `Vendedor` recebe a comissão por venda e a quantidade de vendas, e seu salário final corresponde ao salário base mais a comissão multiplicada pela quantidade. Bônus e comissão não podem ser negativos; a quantidade deve ser um inteiro maior ou igual a zero. Valide esses dados na criação. Neste exercício, eles podem ser propriedades somente de leitura.

Implemente `__str__` para apresentar nome, função e salário final com duas casas decimais. As propriedades devem ficar no corpo da classe, fora de `__init__`.

Crie a classe `Empresa`, com nome e uma lista de funcionários própria de cada instância. O método `adicionar_funcionario(funcionario)` deve aceitar instâncias de `Funcionario`, inclusive suas subclasses, e rejeitar outros objetos com `TypeError`. Considere que cada objeto será cadastrado uma única vez.

O método `total_folha()` deve retornar a soma dos salários finais. Use um laço ou `sum()` e chame `salario_final()` em cada funcionário. Não verifique se o funcionário é gerente ou vendedor para escolher a fórmula: cada subclasse deve resolver seu próprio cálculo. Uma empresa sem funcionários deve retornar zero.

No bloco `if __name__ == "__main__":`, cadastre Ana, gerente com salário base de R$ 5.000,00 e bônus de R$ 1.000,00, e Bruno, vendedor com salário base de R$ 2.000,00, comissão de R$ 50,00 e 10 vendas. Exiba os funcionários e o total da folha. Os resultados devem ser R$ 6.000,00, R$ 2.500,00 e R$ 8.500,00, respectivamente.

Confira também a empresa vazia, um salário negativo, um nome em branco e uma tentativa de cadastrar uma string. Use `try/except` nas demonstrações de erro para permitir que o programa continue. Execute com `python Ex05_Folha_pagamento.py`.

Ao terminar, explique em comentários por que `Empresa` usa composição e em qual trecho ocorre o polimorfismo. Como desafio opcional, acrescente `Estagiario`, cujo salário final é igual ao salário base, sem alterar `total_folha()`.
