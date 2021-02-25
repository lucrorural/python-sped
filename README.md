# SPED para python

![Build Status](https://github.com/lucrorural/python-sped/workflows/python-sped%20app/badge.svg)


Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para Python.

## Instalação

```sh
$ pip install python-sped
```

## Desenvolvimento

Criar seu ambiente virtual

```sh
$ virtualenv .venv
$ source .venv/bin/activate
```

Instalar as dependências
    
```sh
$ pip install -e .
```

## Testes
    
Execute
    
```sh
$ make test
```

## Objetivos do Projeto

A ideia inicial do projeto é unificar em uma única biblioteca módulos para facilitar a geração dos arquivos do SPED, diminuido o retrabalho necessário para isso e tentando ao máximo garantir que o arquivo gerado seja considerado válido pelo validador do SPED.

Não é objetivo deste projeto, remover a necessidade do programador em conhecer o SPED, bem como sua legislação e saber informar adequadamente todas as informações corretamente.

## Compatibilidade do Projeto

O projeto suportará Python 3.4+

## Contribuições para o Projeto

Contribuições são bem vindas ao projeto, exemplos de como você pode contribuir:
 * Usando o projeto e [apontando bugs](https://github.com/lucrorural/python-sped/issues)
 * [Sugestões de melhoria](https://github.com/lucrorural/python-sped/issues)
 * Enviando [pull requests](https://github.com/lucrorural/python-sped/pulls)
 * Auxiliando na [documentação](https://github.com/lucrorural/python-sped/wiki)
 * [Discutindo](https://github.com/lucrorural/python-sped/discussions) sobre o projeto

## Status do Projeto

| Módulo         |     Status    |
|----------------|:-------------:|
| ECD            |   Funcional   |
| ECF            |   Funcional   |
| EFD-PIS/COFINS |   Funcional   |
| EFD-ICMS/IPI   |   Funcional   |
| FCI            |   Funcional   |
| LCDPR          |   Funcional   |
