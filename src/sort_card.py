def sort_cards(deck):
    CARD_ORDER = list('A123456789TJQK')
    return [CARD_ORDER[y] for y in sorted([CARD_ORDER.index(x) for x in deck])]