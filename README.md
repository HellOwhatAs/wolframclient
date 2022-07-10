# wwolframclient
Some changes for [WolframClientForPython](https://github.com/WolframResearch/WolframClientForPython)  

1. Enable `wl.a+wl.b` etc. while the origin module only allows `wl.Plus(wl.a,wl.b)` etc. by changing \_\_init\_\_.py  
2. Add `_repr_latex_` function for expressions (`wolframclient.language.expression.WLFunction` and `wolframclient.language.expression.WLSymbolFactory`) to display latex in jupyter notebook output  
3. Add expression.pyi for code completion (run __init__.py of wwolframclient)  
4. Add function `wplot`  
5. The expression actually evaluated when displayed in Jupyter output (in func *._repr_latex_)

# Install
```
pip install wwolframclient
```

# Usage Example  
```python
from wwolframclient import section,wplot,wl,wlexpr

a,b,c,x=wl.a,wl.b,wl.c,wl.x
solutions=section.evaluate(
    wl.Solve(
        a*x**2+b*x+c==0,
        x
    )
)
for i,solution in enumerate(solutions):
    print("Solution",i)
    for var in solution:
        print(section.evaluate(wl.ToString(var,wl.TeXForm)))
section.terminate() # have to stop manually
```
