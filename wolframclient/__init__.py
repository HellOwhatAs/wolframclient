from __future__ import absolute_import, print_function, unicode_literals

from wolframclient.about import __author__, __name__, __version__

__all__ = ("__version__", "__name__", "__author__")



from wolframclient.language.expression import WLFunction,WLSymbolFactory
from wolframclient.language import wl
from wolframclient.evaluation import WolframLanguageSession
WLFunction.__add__=WLSymbolFactory.__add__=lambda*args:wl.Plus(*args)
WLFunction.__eq__=WLSymbolFactory.__eq__=lambda*args:wl.Equal(*args)
WLFunction.__floordiv__=WLSymbolFactory.__floordiv__=lambda*args:wl.Quotient(*args)
WLFunction.__ge__=WLSymbolFactory.__ge__=lambda*args:wl.GreaterEqual(*args)        
WLFunction.__gt__=WLSymbolFactory.__gt__=lambda*args:wl.Greater(*args)
WLFunction.__le__=WLSymbolFactory.__le__=lambda*args:wl.LessEqual(*args)
WLFunction.__lt__=WLSymbolFactory.__lt__=lambda*args:wl.LessThan(*args)
WLFunction.__mod__=WLSymbolFactory.__mod__=lambda*args:wl.Mod(*args)
WLFunction.__mul__=WLSymbolFactory.__mul__=lambda*args:wl.Times(*args)
WLFunction.__ne__=WLSymbolFactory.__ne__=lambda*args:wl.Unequal(*args)
WLFunction.__neg__=WLSymbolFactory.__neg__=lambda self:wl.Times(-1,self)
WLFunction.__pow__=WLSymbolFactory.__pow__=lambda*args:wl.Power(*args)
WLFunction.__radd__=WLSymbolFactory.__radd__=lambda*args:wl.Plus(*args)
WLFunction.__rfloordiv__=WLSymbolFactory.__rfloordiv__=lambda*args:wl.Quotient(*args)
WLFunction.__rmod__=WLSymbolFactory.__rmod__=lambda self,other:wl.Mod(other,self)
WLFunction.__rmul__=WLSymbolFactory.__rmul__=lambda*args:wl.Times(*args)
WLFunction.__rpow__=WLSymbolFactory.__rpow__=lambda self,other:wl.Power(other,self)
WLFunction.__rsub__=WLSymbolFactory.__rsub__=lambda self,other:wl.Plus(other,wl.Times(-1,self))
WLFunction.__rtruediv__=WLSymbolFactory.__rtruediv__=lambda self,other:wl.Times(other,wl.Power(self,-1))
WLFunction.__sub__=WLSymbolFactory.__sub__=lambda self,other:wl.Plus(self,wl.Times(-1,other))
WLFunction.__truediv__=WLSymbolFactory.__truediv__=lambda self,other:wl.Times(self,wl.Power(other,-1))
section=WolframLanguageSession()
WLFunction._repr_latex_=WLSymbolFactory._repr_latex_=lambda self:"$"+section.evaluate(wl.ToString(wl.Hold(self),wl.TeXForm))+"$"
