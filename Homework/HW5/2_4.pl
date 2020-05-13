word(astante,  a,s,t,a,n,t,e).
word(astoria,  a,s,t,o,r,i,a).
word(baratto,  b,a,r,a,t,t,o).
word(cobalto,  c,o,b,a,l,t,o).
word(pistola,  p,i,s,t,o,l,a).
word(statale,  s,t,a,t,a,l,e).

% Format: (horizontal position)x(letter position)w(vertical position)x(letter position)
crossword(H1, H2, H3, V1, V2,V3) :-
word(H1,_, H1xL2wV1xL2,_, H1xL4wV2xL2,_, H1xL6wV3xL2,_),
word(H2,_, H2xL2wV1xL4,_, H2xL4wV2xL4,_, H2xL6wV3xL4,_),
word(H3,_, H3xL2wV1xL6,_, H3xL4wV2xL6,_, H3xL6wV3xL6,_),
word(V1,_, H1xL2wV1xL2,_, H2xL2wV1xL4,_, H3xL2wV1xL6,_),
word(V2,_, H1xL4wV2xL2,_, H2xL4wV2xL4,_, H3xL4wV2xL6,_),
word(V3,_, H1xL6wV3xL2,_, H2xL6wV3xL4,_, H3xL6wV3xL6,_),
H1 \= V1, H2 \= V2, H3 \=V3. 