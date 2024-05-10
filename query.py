from subgrounds import Subgrounds, SyntheticField

# Set up the api key and subgraph id
API_KEY = '<API_KEY>'
SUBGRAPH_ID = '<SUBGRAPH_ID>'

url = f'https://gateway-arbitrum.network.thegraph.com/api/{API_KEY}/subgraphs/id/{SUBGRAPH_ID}'

# Load the subgraph and query the data
with Subgrounds() as sg:
    carbon = sg.load_subgraph(url)

    trade = carbon.Trade
    # Create a SyntheticField to format datetime
    trade.createdAtDatetime = SyntheticField.datetime_of_timestamp(trade.createdAtTimestamp)
    
    # FieldPath to query the oldest users 
    oldest_users = carbon.Query.users(
        first=10,
        orderBy='createdAtTimestamp',
        orderDirection='asc',
    )
    
    # Partial FieldPath to query the most recent trades from users
    recent_trades = oldest_users.trades(
        first=5,
        orderBy='createdAtTimestamp',
        orderDirection='desc',
    )
    
    # Define the fields to be queried  
    userFields = [
        oldest_users.id,
        recent_trades.id,
        recent_trades.createdAtDatetime,
        recent_trades.sourceAmount,
        recent_trades.targetAmount,
        recent_trades.tradingFeeAmount,
        recent_trades.pair.id,
        recent_trades.pair.token0.id,
        recent_trades.pair.token0.symbol,
        recent_trades.pair.token1.id,
        recent_trades.pair.token1.symbol,  
    ]    

    user_df = sg.query_df(userFields)
    user_df.to_csv('YOUR_FILE.csv', index=False)