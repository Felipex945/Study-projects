#!/bin/bash

echo "CÁCULO DE SOMAS E SUBTRAÇÃO "
echo "=========================="
echo "Digite o primeiro número: "
read numero_1

echo "Digite o segundo numero"
read numero_2

echo "Digite 1 para adição e 2 para subtração:"
read opcao

adicao=$(( numero_1 + numero_2 ))
subtracao=$(( numero_1 - numero_2 ))

if [ "$opcao" -eq 1 ]; then
	echo "$numero_1 + $numero_2 = $adicao"
elif [ "$opcao" -eq 2 ]; then
	echo "$numero_1 - $numero_2 = $subtracao"
else
	echo "Opção inválida!"
fi

