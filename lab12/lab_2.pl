% Sarah Samuel
% CS344, Lab12
% April 27, 2019


% Exercise 12. 2: 

% Part a) 

% i.

% 1. bread  =  bread, returns true.
% 2. ’Bread’  =  bread, returns false.
% 8. food(X)  =  food(bread), returns X = bread. 
% 9.food(bread,X)  =  food(Y,sausage), returns X = sausage Y = bread
% 14. meal(food(bread),X)  =  meal(X,drink(beer)), returns false. This is because there is nothing variable X can be that will satisfy 
% both food, and drink. 

% ii.

% ?-  magic(house_elf).  returns false. 
% ?-  wizard(harry).  returns “Procedure ‘wizard(A)’ does not exist”
% ?-  magic(wizard). returns false
% ?-  magic(’McGonagall’). Could not run the query due to a syntax error. I’m assuming that Prolog doesn’t like quotes around Parameters.
% ?-  magic(Hermione). Returns Hermione = dobby. I am assuming that it understands magic(x) :- house_elf(X), and then refers to house_elf
% (Dobby). Therefore it sees magic(Hermione) as Dobby. Also, I had to comment out magic(X) :-  wizard(X) because it is referring to an 
% undefined procedure. 


% Part b
% Inference in propositional logic does use unification by allowing two rules that overlap to be combined. When there are many statements
% with the same term on the left side of the inference, Prolog will allow unification from the first rule. 

% Part c 
% I believe that Prolog uses resolution in inference. I think this is because if you two clauses with the same elements in it, it can 
% result in one new clause from the two old clauses...

