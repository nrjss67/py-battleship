class Deck:
    def __init__(self, row, column, is_alive=True):
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(self, start, end, is_drowned=False):
        self.decks = []
        if start == end:
            self.decks.append(Deck(*start))
        if start[1] < end[1]:
            for end_ in range(start[1], end[1] + 1):
                self.decks.append(Deck(start[0], end_))
        if start[0] < end[0]:
            for start_ in range(start[0], end[0] + 1):
                self.decks.append(Deck(start_, start[1]))
        self.is_drowned = is_drowned

    def get_deck(self, row, column):
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return self.decks.index(deck)

    def fire(self, row, column):
        index = self.get_deck(row, column)
        self.decks[index].is_alive = False
        if all(deck.is_alive for deck in self.decks):
            self.is_drowned = True


class Battleship:
    def __init__(self, ships):
        self.field = {}
        for coordinate in ships:
            ship = Ship(*coordinate)
            for deck in ship.decks:
                self.field[(deck.row, deck.column)] = ship

    def fire(self, location: tuple):
        if location not in self.field:
            return "Miss!"
        if location in self.field:
            ship = self.field.get(location)
            if sum(map(lambda x: x.is_alive, ship.decks)) == 1:
                ship.fire(*location)
                return "Sunk!"
            else:
                ship.fire(*location)
                return "Hit!"
