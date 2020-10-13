class Task (object):

    def __init__ (self, predec, following, duration, resources):
        self.p = predec # list
        self.f = following
        self.d = duration
        self.r = resources

    def maxtime (self):
        if self.p == None:
            return self.d
        ret = max([ prev.maxtime() for prev in self.p ])
        return self.d + ret

    def debut_plustot (self):
        if self.p == None:
            return 0
        return max([ prev.fin_plustot() for prev in self.p ])

    def fin_plustot (self):
        return self.debut_plustot() + self.d

    def fin_plustard (self):
        if self.f == None:
            return self.maxtime()
        return min([ fol.debut_plustard() for fol in self.f ])

    def debut_plustard (self):
        return self.fin_plustard() - self.d

    def marge_totale (self):
        return self.fin_plustard() - self.fin_plustot()

    def marge_libre (self):
        return min([ fol.debut_plustot() for fol in self.f ]) - self.fin_plustot()

T1 = Task ( None, [], 3, 2 )
T2 = Task ( [T1], [], 8, 1 )
T3 = Task ( [T1], [], 4, 2 )
T4 = Task ( [T1], [], 5, 1 )
T5 = Task ( [T3], [], 6, 2 )
T6 = Task ( [T3], [], 4, 1 )
T7 = Task ( [T4], [], 5, 2 )
T8 = Task ( [T2,T4], [], 4, 1 )
T9 = Task ( [T2,T5], [], 4, 3 )
T10 = Task ( [T5,T6], [], 3, 2 )
T11 = Task ( [T7], [], 4, 2 )
T12 = Task ( [T7,T8], [], 3, 1 )
T13 = Task ( [T9,T10], [], 4, 2 )
T14 = Task ( [T10], [], 4, 1 )
T15 = Task ( [T11,T12], [], 1, 1 )
T16 = Task ( [T13,T14], [], 4, 2 )
T17 = Task ( [T14,T15], [], 2, 2 )
T18 = Task ( [T16,T17], None, 3, 1 )

T1.f = [T2, T3, T4]
T2.f = [T8, T9]
T3.f = [T5, T6]
T4.f = [T7,T8]
T5.f = [T9, T10]
T6.f = [T10]
T7.f = [T11, T12]
T8.f = [T12]
T9.f = [T13]
T10.f = [T13, T14]
T11.f = [T15]
T12.f = [T15]
T13.f = [T16]
T14.f = [T16,T17]
T15.f = [T17]
T16.f = [T18]
T17.f = [T18]

arbre = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18]

#print( T11.marge_totale() )
#print( T15.marge_libre() )

"""
c = 0

for elem in arbre:
    if elem.fin_plustot() == elem.fin_plustard():
        c+=1
print(c)
"""

"""
c = 0
for T in arbre:
    if T.debut_plustot()+1 <= 8 and 8 <= T.fin_plustot():
        c += T.r
print(c)
"""
