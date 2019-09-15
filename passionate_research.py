import numpy as np

# determies frequency of player drawing
player_drawrates = [1.2, 1.0, 1.0, 1.0]
cards_drawn_until_game_end = 36
trials = 50000


# converts the draw rates to a draw probability
def drawrate_to_probability(draw_rates):
    return list(map(lambda x: x / sum(draw_rates), draw_rates))


draw_probabilities = drawrate_to_probability(player_drawrates)


# Function that checks if a card in a certain position is
# a hyper. Only pulls the card if it is a hyper.
# This function exists for passionate research functionality.
def check_hyper(Deck, position, player_drawing, hypers_drawn):
    if Deck[position] == "hyper":
        hypers_drawn[player_drawing] += 1
        Deck.pop(position)


def simulate_draws(draw_probabilities, passionates_in_deck, cards_drawn_until_game_end):
    # Initialize the deck
    Deck = [None] * 48
    hypers_drawn = np.array([0] * 4)
    # Fill deck with hypers and passionate researches
    for number in range(0, 8):
        Deck[number] = "hyper"
    for number in range(8, 8 + passionates_in_deck):
        Deck[number] = "passionate_research"

    np.random.shuffle(Deck)
    # Create a list of numbers from 0 to 3 the number
    # at a given position indicates which player draws
    # the card at the corresponding position.
    draw_order = list(np.random.choice(
        4, 48, p=draw_probabilities))

    while True:
        if len(Deck) <= 48 - cards_drawn_until_game_end:
            break
        # Determine which player is drawing, and the card drawn.
        player_drawing = draw_order[0]
        draw_order.pop(0)
        card = Deck[0]
        Deck.pop(0)

        if card == "hyper":
            hypers_drawn[player_drawing] += 1
        if card == "passionate_research":
            for index in range(1, 4):
                if index < len(Deck):
                    check_hyper(Deck, index, player_drawing, hypers_drawn)

    return hypers_drawn


passionate_bad = 0
no_pr_hyper_rate = 0
one_pr_hyper_count = 0

for _ in range(0, trials):
    no_pr_hyper_rate = no_pr_hyper_rate + \
        simulate_draws(draw_probabilities, 0, cards_drawn_until_game_end)
    one_pr_hyper_count = one_pr_hyper_count + \
        simulate_draws(draw_probabilities, 1, cards_drawn_until_game_end)

no_pr_hyper_rate = no_pr_hyper_rate / trials
one_pr_hyper_rate = one_pr_hyper_count / trials
print("With no pr, the average hypers distribution is:", no_pr_hyper_rate)
print("With one pr, the average hyper distribution is:", one_pr_hyper_rate)
