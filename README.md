# Khan Academy CS thumbnail tvořítko

Soubor ``creator.py`` zařizuje tvorbu thumbnail. Jako parametr přijímá YouTube id daného videa. 

Z titulku videa se vezme pouze část před prvním | (svislítkem). Podpora pro různé barvy pro různé předměty je připravena, ale prozatím je všechno matematicky modré (prý to stačí). 

Pokud se titulek špatně zalomí, tak založte issue, zkusím doplnit nějaké manuální obcházedlo.

## Příklad

```
python creator.py DLzxrzFCyOs
```

![example](https://github.com/KhanovaSkola/KAThumbCreator/blob/master/example/DLzxrzFCyOs.png)

