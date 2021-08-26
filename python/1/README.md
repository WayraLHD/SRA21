# ¿Por Qué uso eq=sym.Eq(Vo,f(V1,V2)) y no directamente Vo=f(V1,V2)?
Porque cuando quiero reprecentar symbolicamente la expresion: dVo/dV1 
imprime directamente f'(V1,V2) pero yo solo queria la expresión dVo/dV1 no el resultado
particularmente quiero esa expresión para hacer el informe en latex, numericamente no aporta nada.
pero puedo acceder al resultado dVo/dV1 como d(eq.rhs)/dV1
