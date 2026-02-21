import time
from game import Game, Deck, Player, Dealer

def play_round(deck, player, dealer):
    FIXED_BET = 50

    player.set_money(player.get_money() - FIXED_BET)
    print(f"\n--- NEW ROUND ---")
    print(f"Bet of ${FIXED_BET} placed. Remaining funds: ${player.get_money()}")

    game = Game(player, dealer, deck, FIXED_BET)

    # Clearing hands before game
    player.clear_hands()
    dealer.clear_hands()
    # Dealing hands
    player.receive_card(deck.deal())
    dealer.receive_card(deck.deal())
    player.receive_card(deck.deal())
    dealer.receive_card(deck.deal())

    print("-" * 30)
    dealer.print_hand(round_num=1)
    print("-" * 30)

    hand_index = 0 # for splits

    while hand_index < len(player.hands):
        current_hand = player.hands[hand_index]

        while True: # game starts 
            score = Game.calculate_hand(current_hand)

            print(f"\n--- PLAYING HAND {hand_index + 1} ---")
            player.print_hand(hand_index)
            print(f"Current Value: {score}")

            # check bust
            if score > 21:
                print(f"Bust! Hand {hand_index + 1} went over 21.")
                break
            # Stand at 21
            if score == 21:
                print(f"21! Moving to next hand/dealer.")
                break
            
            # Check if they have enough money for an EXTRA 50 to split
            can_split = game.can_split(current_hand) and player.get_money() >= FIXED_BET
            options = "(H)it, (S)tand" + (", S(p)lit" if can_split else "")

            choice = input(f"Action? {options}: ").lower()
            
            if choice == 'h':
                new_card = deck.deal()
                print(f"Dealt: {new_card}")
                player.receive_card(new_card, hand_index)
            
            elif choice == 's':
                print(f"Hand {hand_index + 1} stands at {score}.")
                break

            elif choice == "p" and can_split:
                print(f"Splitting hand... Deducting another ${FIXED_BET}")
                success = game.split_hand(hand_index)
                if success:
                    continue
                else:
                    print("Could not split.")
            else:
                print("Invalid input or not enough money to split.")
        hand_index += 1

    print("\n" + "=" * 30)
    print("PLAYER TURN ENDED. DEALER REVEALS.")
    print("=" * 30)

    game.determine_winner()

def main():
    print("Welcome to Blackjack!")
    deck = Deck()
    player = Player()
    dealer = Dealer()
    MIN_BET = 50

    # Game Loop: Only runs if player has at least 50
    while player.get_money() >= MIN_BET:
        play_round(deck, player, dealer)
        
        if player.get_money() < MIN_BET:
            print(f"\nYou have ${player.get_money()}. Not enough for the $50 bet. Game Over.")
            break
            
        again = input(f"\nYou have ${player.get_money()}. Play another round? (y/n): ").lower()
        if again != 'y':
            print(f"You left with ${player.get_money()}.")
            break
            
        # Reshuffle if deck is low
        if len(deck.cards) < 15:
            print("\nReshuffling deck...")
            deck = Deck()

if __name__ == "__main__":
    main()
