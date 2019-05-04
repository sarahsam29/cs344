% Sarah Samuel 
% CS344, Lab13
% May 3, 2019


% Part a:
% Exercise 3.2: 

  directlyIn(olga, katarina).
  directlyIn(natasha, olga).
  directlyIn(irina, natasha).

  in(X,Y):- directlyIn(X,Y).
  in(X,Y):- directlyIn(X,Z),
              in(Z,Y).

  % -? directlyIn(natasha, katarina) returns false
  % -? in(natasha, katarina) returns true

% Exercise 4.5: 

 tran(eins,one). 
 tran(zwei,two). 
 tran(drei,three). 
 tran(vier,four). 
 tran(fuenf,five). 
 tran(sechs,six). 
 tran(sieben,seven). 
 tran(acht,eight). 
 tran(neun,nine).

  listtran([], []).
  listtran([G|TG], [E|TE]) :- tran(G, E), 
                           listtran(TG, TE). 

% Part b: 
% Yes, Prolog does support Modes Pones. Below is an example from last week’s lab: 

hasBroom(harry).
quidditchPlayer(X):- hasBroom(X).

% -? quidditchPlayer(harry) returns true
