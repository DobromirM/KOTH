# Battle

King of the hill template for a game inspired by the card game "War".

### Rules:<br>

Every bot starts with a hand of cards with values from 1 to 13 (Ace being 1 and King being 13).
Every round the bots are randomly paired and must pick a card from their hand to play. The bot with 
higher card value wins the round and continues to the next, the other bot is removed from play. Once a card is played
it is removed from the hand of the bot that played it. In case of a tie, the cards are returned to the hands of the bots 
and the turn is repeated. If the turn is repeated 3 times and it is still a tie, both bots are eliminated from play. If a
bot plays an invalid card (a card that is not in his hand) his card for the turn will have a value of 0.
Last bot standing after all rounds is the winner!

### Task:

Create a new Bot class that returns a card from your hand (2 <= card_value <= 13). The Bot class must inherit the generic Bot class and define a 'select_card' function as shown bellow:


<pre>
class MyNameBot(Bot):
    # Return a card from your hand 
    
    def select_card(self, opp_hand, player_count, ties):
        # Place the logic of the bot here
</pre>

#### Parameters:

    self.hand - The card in your hand
    self.max_card - The highest card that you have in your hand
    self.min_card - The lowest card that you have in your hand
    opp_hand  - The cards that your current opponent has in his hand
    player_count - The count of all the players in the current round
    ties - number of ties for the current battle so far
    
    
#### Example: 
<pre>
class ExampleBot(Bot):
    # Example bot showing you how to make your own
    
    def select_card(self, opp_hand, player_count, ties):
        
        # If there are two ties already return the first card
        if ties >= 2:
            return self.hand[0]
            
        # If there is only one other player left use your highest card
        if player_count == 2:
            return self.max_card
           
        # If your opponent doesn't have a 13 in his hand give 13 
        if 13 not in opp_hand:
            return 13
         
        # If you don't have 6 in your hand give 5 
        if 6 not in self.hand:
            return 5
            
        #Else return the lowest card in your hand
        return self.min_card   
</pre>

#### Additional rules: 

1) All bots should follow the rules of the game and should not try to edit the internal state of the program
for example by adding more cards to their hand.

2) Bots should terminate in reasonable time.

3) Additional rules might be added to prevent loopholes.
