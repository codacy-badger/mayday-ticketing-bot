from mayday import LogConfig
from mayday.constants import (CATEGORY_MAPPING, DATE_MAPPING, PRICE_MAPPING,
                              STATUS_MAPPING, conversations)
from mayday.helpers import Helper

flogger = LogConfig.flogger


class PostTicketHelper(Helper):

    def fill_in_wishlist(self, ticket, todos):
        for key in todos:
            if key == 'wish_date':
                ticket[key] = [x for x in DATE_MAPPING]
            if key == 'wish_price_id':
                ticket[key] = [x for x in PRICE_MAPPING]
            if key == 'wish_quantity':
                ticket[key] = [x for x in range(1, 5)]
        self.set_cache(user_id=ticket.get('user_id'), content=ticket)
        return ticket

    def update_cache(self, user_id, username, content):
        ticket = self.get_cache(user_id=user_id, username=username)
        last_choice = self.get_last_choice(user_id)
        if (content and last_choice in ['category_id', 'status_id', 'quantity',
                                        'price_id', 'date']):
            ticket[last_choice] = int(content)
        elif (content and last_choice in ['wish_date', 'wish_price_id', 'wish_quantity']):
            ticket[last_choice].append(int(content))
        else:
            ticket[last_choice] = content
        self.set_cache(user_id, ticket)
        return ticket

    def get_category_id_from_cache(self, user_id, username):
        category_id = self.get_cache(user_id, username).get('category_id')
        if category_id:
            return category_id
        else:
            # 1 is default keyboard and ticket setting
            return 1
