Sarah Samuel
CS 344 Lab12
April 27, 2019


Part a:
Exercise 1.4: 

    % 1. butch is a killer: 
    killer(Butch).

    % 2. Mia and Marsellus are married:
    married(Mia, Marcellus)
    married(Marsellus, Mia)

    % 3. Zed is dead:
    dead(Zed)

    % 4. Marsellus kills everyone who gives Mia a foot massage:
    kills(Marsellus, X) :- givesFootMassage(X, Mia).

    % 5. Mia loves everyone who is a good dancer:
    loves(Mia, X) :- goodDancer(X).

    % 6. Jules eats anything that is nutritious or tasty.
    eats(Jules, X) :-
         nutritious(X);
         tasty(X).

Exercise 1.5: 

    % wizard(ron). Returns true
    % witch(ron). Returns “Procedure ‘witch(A)’ does not exist”
    % wizard(hermione). Returns false
    % witch(hermione). Returns “Procedure ‘witch(A)’ does not exist”
    % wizard(harry). Returns true
    % wizard(Y). Y = ron
    % witch(Y). Returns “Procedure ‘witch(A)’ does not exist” 

There is no fact “witch” in the knowledge base so Prolog lets us know that the procedure does not exist.
Because facts state that Harry has a wand and is a quidditch player, Harry satisfies the rule Hasbroom. Moreover, since Harry 
Hasbroom and HasWand, wizard(Harry) responds True. Wizard(Y) Returns Y = Ron because Ron is the first person declared as a wizard.


Part b: 

Yes, Prolog does use Modus Ponenes. An example of this is seen in Exercise 1.5 :
	hasBroom :- quidditchPlayer(Y), quidditchPlayer(Harry), thus hasBroom(Harry). 

Part c: 
A horn clause has at most one positive literal. 

Part d:

Yes, Prolog has a distinction. The facts that a user tells are stored in knowledge bases. Then the use can ask questions (queries) 
using a knowledge base to gain information. 


