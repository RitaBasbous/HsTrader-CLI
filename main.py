from hstrader import HsTrader
from hstrader.models import CrtOrder,OrderType,SideType,Order,Position

def user():
    while True:
        try:
            id = input('Enter your id: ')
            secret = input('Enter your Client secret: ')
            client = HsTrader(id, secret)
            return client
        except ValueError:
            print('Incorrect password or username.')
            

def symbols(client):
    while True:
        symbol=input('Enter symbol name: ')
        try:
            x=client.get_symbol(symbol)
        except ValueError:
            print('symbol not found')
            continue
        else:
            symbol=client.get_symbol(symbol)
            return symbol
        
        
def order_types():
    order_mapping = {
        'BUY_LIMIT': OrderType.BUY_LIMIT,
        'MARKET_ORDER': OrderType.MARKET_ORDER,
        'BUY_STOP': OrderType.BUY_STOP,
        'SELL_LIMIT': OrderType.SELL_LIMIT,
        'SELL_STOP': OrderType.SELL_STOP,
        'BUY_STOP_LIMIT': OrderType.BUY_STOP_LIMIT,
        'SELL_STOP_LIMIT': OrderType.SELL_STOP_LIMIT
    }

    while True:
        order_type = input(f'Enter the order type you want from {list(order_mapping.keys())}: ')
        if order_type in order_mapping:
            return order_mapping[order_type]
        else:
            print('Invalid order type.')





def side_type(order_type):
    if order_type in (OrderType.BUY_LIMIT,OrderType.BUY_STOP_LIMIT,OrderType.BUY_STOP):
        return SideType.BUY
    elif order_type in (OrderType.SELL_LIMIT,OrderType.SELL_STOP,OrderType.SELL_STOP_LIMIT):
        return SideType.SELL
    else:
        while True:
            side=input('Enter the side (Buy or Sell): ')
               
            if side.upper()=='BUY':
                return SideType.BUY
            elif side.upper()=='SELL':
                return SideType.SELL
            else:
                 print('wrong value')



def Volume(symbol):
    while True:
        try:
            user_volume = eval(input('Enter the volume: '))  
        except NameError:
            print('Only numbers are allowed.')
        else:
            if user_volume < symbol.min_value:
                print(f'Rejected, the minimum amount is {symbol.min_value}')
            elif user_volume > symbol.max_value:
                print(f'Rejected, the maximum amount is {symbol.max_value}')
            else:
                return user_volume



def OrderPrice(order_type, side, symbol):
    if order_type == OrderType.MARKET_ORDER:
        if side == SideType.BUY:
            price = symbol.last_ask
            return price
        else:
            price = symbol.last_bid
            return price
    elif order_type == OrderType.BUY_LIMIT:
        while True:
            try:
                price = float(input('Enter the price: '))
            except ValueError:
                print('Only numbers are allowed.')
            else:
                if price >= symbol.last_ask:
                    print(f'Rejected, it must be less than {symbol.last_ask}')
                else:
                    return price
    elif order_type == OrderType.BUY_STOP_LIMIT:
        while True:
            try:
                price = float(input('Enter the price: '))
            except ValueError:
                print('Only numbers are allowed.')
            else:
                return price
        
    elif order_type == OrderType.BUY_STOP:
        while True:
            try:
                price = float(input('Enter the price: '))
            except ValueError:
                print('Only numbers are allowed.')
            else:
                if price <= symbol.last_ask:
                    print(f'Rejected, it must be more than {symbol.last_ask}')
                else:
                    return price
    elif order_type == OrderType.SELL_LIMIT:
        while True:
            try:
                price = float(input('Enter the price: '))
            except ValueError:
                print('Only numbers are allowed.')
            else:
                if price <= symbol.last_bid:
                    print(f'Rejected, it must be more than {symbol.last_ask}')
                else :
                    return price
        
    elif order_type == OrderType.SELL_STOP:
        while True:
            try:
                price = float(input('Enter the price: '))
            except ValueError:
                print('Only numbers are allowed.')
            else:
                if price >= symbol.last_bid:
                    print(f'Rejected, it must be less than {symbol.last_ask}')
                else :
                    return price
        
    elif order_type == OrderType.SELL_STOP_LIMIT:
        while True:
            try:
                price = float(input('Enter the price: '))
            except ValueError:
                print('Only numbers are allowed.')
            else:
                return price
        
    

def StopLoss(order_type,side,price):
    if order_type == OrderType.MARKET_ORDER:
        if side == SideType.BUY:
            while True:
                try:
                    SL_input = input('Enter Stop Loss value (or type "None"): ')
                    if SL_input.lower() == 'none':
                        SL = None
                    else:
                        SL = float(SL_input)
                except ValueError:
                    print('Only numbers are allowed.')
                else:
                    if SL is not None:
                        if SL >= price:
                            print(f'Rejected, it must be less than {price}')
                        else:
                            return SL
                    else: return SL
        else:
            while True:
                try:
                    SL_input = input('Enter Stop Loss value (or type "None"): ')
                    if SL_input.lower() == 'none':
                        SL = None
                    else:
                        SL = float(SL_input)
                except ValueError:
                    print('Only numbers are allowed.')
                else:
                    if SL is not None:
                        if SL <= price:
                            print(f'Rejected, it must be more than {price}')
                        else:
                            return SL
                    else: return SL
    elif order_type  in (OrderType.BUY_STOP,OrderType.BUY_LIMIT,OrderType.SELL_LIMIT,OrderType.BUY_STOP_LIMIT):
        while True:
                try:
                    SL_input = input('Enter Stop Loss value (or type "None"): ')
                    if SL_input.lower() == 'none':
                        SL = None
                    else:
                        SL = float(SL_input)
                except ValueError:
                    print('Only numbers are allowed.')
                else:
                    if SL is not None:
                        if SL >= price:
                            print(f'Rejected, it must be less than {price}')
                        else:
                            return SL
                    else: return SL
    else:
        while True:
                try:
                    SL_input = input('Enter Stop Loss value (or type "None"): ')
                    if SL_input.lower() == 'none':
                        SL = None
                    else:
                        SL = float(SL_input)
                except ValueError:
                    print('Only numbers are allowed.')
                else:
                    if SL is not None:
                        if SL <= price:
                            print(f'Rejected, it must be more than {price}')
                        else:
                            return SL
                    else: return SL
    
    

def TakeProfit(order_type, side, price):
    if order_type == OrderType.MARKET_ORDER:
        if side == SideType.BUY:
            while True:
                try:
                    TP_input = input('Enter Take Profit value (or type "None"): ')
                    if TP_input.lower() == 'none':
                        TP = None
                    else:
                        TP = float(TP_input)
                except ValueError:
                    print('Only numbers are allowed.')
                else:
                    if TP is not None:
                        if TP <= price:
                            print(f'Rejected, it must be more than {price}')
                        else:
                            return TP
                    else: return TP
        else:
            while True:
                try:
                    TP_input = input('Enter Take Profit value (or type "None"): ')
                    if TP_input.lower() == 'none':
                        TP = None
                    else:
                        TP = float(TP_input)
                except ValueError:
                    print('Only numbers are allowed.')
                else:
                    if TP is not None:
                        if TP >= price:
                            print(f'Rejected, it must be less than {price}')
                        else:
                            return TP
                    else: return TP
    elif order_type in (OrderType.BUY_STOP,OrderType.BUY_LIMIT,OrderType.SELL_LIMIT,OrderType.BUY_STOP_LIMIT):
        while True:
                try:
                    TP_input = input('Enter Take Profit value (or type "None"): ')
                    if TP_input.lower() == 'none':
                        TP = None
                    else:
                        TP = float(TP_input)
                except ValueError:
                    print('Only numbers are allowed.')
                else:
                    if TP is not None:
                        if TP <= price:
                            print(f'Rejected, it must be more than {price}')
                        else:
                            return TP
                    else: return TP
    else:
        while True:
                try:
                    TP_input = input('Enter Take Profit value (or type "None"): ')
                    if TP_input.lower() == 'none':
                        TP = None
                    else:
                        TP = float(TP_input)
                except ValueError:
                    print('Only numbers are allowed.')
                else:
                    if TP is not None:
                        if TP >= price:
                            print(f'Rejected, it must be less than {price}')
                        else:
                            return TP
                    else: return TP



def main():
    client=user()
    symbol=symbols(client)
    order_type=order_types()
    side=side_type(order_type)
    volume=Volume(symbol)
    price=OrderPrice(order_type,side,symbol)
    take_profit=TakeProfit(order_type,side,price)
    stop_loss=StopLoss(order_type,side,price)
    client.create_order(CrtOrder(symbol_id=symbol,side=side,volume=volume,type=order_type,order_price=price,take_profit=take_profit,stop_loss=stop_loss))
    

if __name__ == "__main__":
    main()
