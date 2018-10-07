import random


# Parent class for all bots
class Bot:

    # Initialize starting hand
    def __init__(self):

        # All players will get one of each card from 1 to 13
        self.hand = list(range(1, 14))

        # Holds the value of the highest card in the hand
        self.max_card = 13

        # Holds the value of the lowest card in the hand
        self.min_card = 1

    # Return the name of the bot
    def __str__(self):
        return self.__class__.__name__

    # Play the selected card
    def play(self, selected_card):

        # If the card you want to play is not in your hand return 0
        if selected_card not in self.hand:
            return 0
        else:
            # Remove the selected card from your hand
            self.hand.remove(selected_card)

            # Update the max and min cards in the hand in case they have changed
            self.max_card = max(self.hand)
            self.min_card = min(self.hand)

            return selected_card

    # Add card to the hand (Used when there is a draw)
    def add_card(self, card):

        if card != 0:
            self.hand.append(card)

            # Update the max and min cards in the hand in case they have changed
            self.max_card = max(self.hand)
            self.min_card = min(self.hand)


# RandomBot - Returns a random card and doesn't even care if
# he has it in his hand or not.
class RandomBot(Bot):

    def select_card(self, opp_hand, player_count, ties):
        return random.randint(1, 13)


# Remove random element from a list
# Used to randomly select bots
def pop_random(lst):
    # Get a random number between 0 and the number of elements in the list
    index = random.randrange(0, len(lst))

    # Remove the selected item from the list and return it
    return lst.pop(index)


# Simulate the duel between the two selected bots
def duel(first_bot, second_bot):
    # Setup variables
    ties = 0
    first_card = 0
    second_card = 0

    # Run the duel between the bots
    while first_card == second_card:

        # If the ties are 3 or more end the duel without a winner
        if ties >= 3:
            return None

        # Get the first bot to select ExampleBota card
        first_selected_card = first_bot.select_card(second_bot.hand, player_count, ties)

        # Get the second bot to select a card
        second_selected_card = second_bot.select_card(first_bot.hand, player_count, ties)

        # Play the selected cards
        first_card = first_bot.play(first_selected_card)
        second_card = second_bot.play(second_selected_card)

        # Get the outcome
        # 0 if they have equal cards
        # 1 if first card is higher than second card
        # -1 if second card is higher than first card
        result = (first_card > second_card) - (first_card < second_card)

        # Decide the winner
        if result == 1:
            return first_bot
        elif result == -1:
            return second_bot
        else:

            # If it ended in a tie, return the cards to the hands of the bots
            first_bot.add_card(first_card)
            second_bot.add_card(second_card)

            # Increase the 'ties' counter
            ties = ties + 1


if __name__ == "__main__":

    # Create a list of all participating bots
    bot_list = [RandomBot(), RandomBot()]
    player_count = len(bot_list)

    # Run the game until there is only one bot standing
    while len(bot_list) > 1:

        # Run one round
        next_round = []
        while len(bot_list) > 1:

            # Select two random bots
            first_bot = pop_random(bot_list)
            second_bot = pop_random(bot_list)

            # Get winner
            winner = duel(first_bot, second_bot)

            # Add the bot for next round
            if winner is not None:
                next_round.append(winner)

        # Update the list of total bots to be only those which have survived
        bot_list = bot_list + next_round
        player_count = len(bot_list)

    # Display the result
    if len(bot_list) > 0:
        print("Winner: " + str(bot_list[0]))
    else:
        print("Tie")
