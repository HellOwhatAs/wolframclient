# wolframclient
Some changes for [wolframclient](https://github.com/WolframResearch/WolframClientForPython)

1. Enable `wl.a+wl.b` etc. while the origin module only allows `wl.Plus(wl.a,wl.b)` etc. by changing \_\_init\_\_.py
2. Add `_repr_latex_` function for expressions (`wolframclient.language.expression.WLFunction` and `wolframclient.language.expression.WLSymbolFactory`) to display latex in jupyter notebook output
3. Add expression.pyi for code completion

**Usage:**
Install [wolframclient](https://github.com/WolframResearch/WolframClientForPython).  
Then replace \_\_init\_\_.py with the \_\_init\_\_.py file in this repository.
