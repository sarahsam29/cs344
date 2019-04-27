% Sarah Samuel
% CS334, Lab12
% April 27, 2019

Exercise 3: 

witch(X):- burn(X);
     looksLikeWitch(X);
     turnsPeopleIntoNewt(X).
burn(X):- wood(X).
floats(X):-
	wood(X);
    apples(X);
    smallRocks(X); 
    cider(X); 
    cherries(X);
	duck(X).
wood(X):- weighsTheSameAsDuck(X).
looksLikeWitch(woman).
turnsPeopleIntoNewt(woman).
weighsTheSameAsDuck(woman).

% ?-witch(woman).
% true
