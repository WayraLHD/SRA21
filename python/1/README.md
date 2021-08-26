# ¿Por Qué uso eq=sym.Eq(Vo,f(V1,V2)) y no directamente Vo=f(V1,V2)?

Porque si hago display(dVo/dV1)  imprime directamente d(F(V1,V2))/dV1 pero yo solo quiero la expresión "dVo/dV1"... no el resultado!!
Particularmente hago esto para hacer el informe en latex, numericamente no aporta nada esa expresión pero si el resultado. 
Lo mismo puedo acceder al resultado dVo/dV1 haciendo d(eq.rhs)/dV1
