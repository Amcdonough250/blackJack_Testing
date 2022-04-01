import game
import unittest




class TestCases(unittest.TestCase):
    deck = game.Deck()
    deck.create_deck()

    def setUp(self)->None:
        print("setUp")

    @classmethod
    def setUpClass(cls)->None:
        print("setUpClass")
        

    @classmethod
    def tearDownClass(cls)->None:
        print("tearDownClass")

    def test_create_deck(self):
        """Check the deck of created cards"""
        self.assertTrue(len(self.deck.cards) == 52)

    def test_pick_a_card(self):
        """Checking pickup of card"""
        self.assertTrue(len(self.deck.draw()) == 1)
        self.assertTrue(len(self.deck.draw(5)) == 5)

        self.assertTrue(0 < self.deck.draw()[0].cost < 14)

    def test_card_number(self):
        """Checking number and suit in the card"""
        sample_card = game.Card(7, 0)

        self.assertEqual(sample_card.number(), 7)
        self.assertEqual(sample_card.suits, '♣')

    def test_player_hit(self):
        """Checking hit function"""
        player = game.Player(False, self.deck)

        self.assertTrue(not player.hit())

        # call multiple time
        player.hit(), player.hit(), player.hit(), player.hit()
        player.hit(), player.hit(), player.hit(), player.hit()

        self.assertTrue(player.hit())

if __name__ == '__main__':
    unittest.main()

