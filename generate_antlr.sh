#!/bin/bash

cd grammar/
antlr4 -Dlanguage=Python3 ToyLangLexer.g4  -o ./generated/
antlr4 -Dlanguage=Python3 ToyLangParser.g4 -o ./generated/

cd ..
rm -r src/toylang/generated/
cp -r grammar/generated/ src/toylang/generated/
rm -r grammar/generated/
