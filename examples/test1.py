from wwolframclient import session,wplot,wl,wlexpr
a,b,c,d,e,x=wl.a,wl.b,wl.c,wl.d,wl.e,wl.x
Solve=session.function(wl.Solve)
print(Solve(a*x**2+b*x+c==0,x))
session.terminate()
